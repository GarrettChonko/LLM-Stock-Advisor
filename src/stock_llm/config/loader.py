"""Helpers for loading YAML configs into typed dataclasses."""

from dataclasses import MISSING, fields, is_dataclass
from pathlib import Path
from typing import Any, TypeVar, get_args, get_origin

import yaml

from stock_llm.config.schema import ModelConfig, TokenizerConfig, TrainingConfig

ConfigT = TypeVar("ConfigT")


class ConfigError(ValueError):
    """Raised when a config file cannot be loaded or validated."""


def load_config(
    config_name: str | Path,
    schema: type[ConfigT],
    config_dir: str | Path = "configs",
) -> ConfigT:
    """Load a YAML config from disk into a typed schema."""
    config_path = _resolve_config_path(config_name, config_dir)

    if not config_path.exists():
        raise ConfigError(f"Config file not found: {config_path}")

    try:
        raw_data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ConfigError(f"Invalid YAML in config file {config_path}: {exc}") from exc

    if raw_data is None:
        raise ConfigError(f"Config file is empty: {config_path}")
    if not isinstance(raw_data, dict):
        raise ConfigError(
            f"Config file must contain a top-level mapping for {schema.__name__}: {config_path}"
        )

    try:
        return _build_dataclass(schema, raw_data)
    except ConfigError as exc:
        raise ConfigError(f"Invalid {schema.__name__} in {config_path}: {exc}") from exc


def load_tokenizer_config(
    config_name: str | Path,
    config_dir: str | Path = "configs",
) -> TokenizerConfig:
    """Load a tokenizer config from the configs directory."""
    return load_config(config_name, TokenizerConfig, config_dir)


def load_model_config(
    config_name: str | Path,
    config_dir: str | Path = "configs",
) -> ModelConfig:
    """Load a model config from the configs directory."""
    return load_config(config_name, ModelConfig, config_dir)


def load_training_config(
    config_name: str | Path,
    config_dir: str | Path = "configs",
) -> TrainingConfig:
    """Load a training config from the configs directory."""
    return load_config(config_name, TrainingConfig, config_dir)


def _resolve_config_path(config_name: str | Path, config_dir: str | Path) -> Path:
    path = Path(config_name)
    if path.is_absolute() or path.parent != Path("."):
        return path
    return Path(config_dir) / path


def _build_dataclass(schema: type[ConfigT], raw_data: dict[str, Any]) -> ConfigT:
    if not is_dataclass(schema):
        raise ConfigError(f"Schema must be a dataclass type, got {schema!r}")

    field_map = {field_info.name: field_info for field_info in fields(schema)}
    unknown_keys = sorted(set(raw_data) - set(field_map))
    if unknown_keys:
        formatted = ", ".join(unknown_keys)
        raise ConfigError(f"unexpected fields: {formatted}")

    values: dict[str, Any] = {}
    for field_info in fields(schema):
        if field_info.name not in raw_data:
            if field_info.default is not MISSING or field_info.default_factory is not MISSING:
                continue
            raise ConfigError(f"missing required field: {field_info.name}")

        value = raw_data[field_info.name]
        values[field_info.name] = _coerce_value(field_info.name, value, field_info.type)

    try:
        return schema(**values)
    except TypeError as exc:
        raise ConfigError(str(exc)) from exc
    except ValueError as exc:
        raise ConfigError(str(exc)) from exc


def _coerce_value(field_name: str, value: Any, expected_type: Any) -> Any:
    origin = get_origin(expected_type)

    if is_dataclass(expected_type):
        if not isinstance(value, dict):
            raise ConfigError(f"field '{field_name}' must be a mapping")
        return _build_dataclass(expected_type, value)

    if origin is list:
        if not isinstance(value, list):
            raise ConfigError(f"field '{field_name}' must be a list")
        item_type = get_args(expected_type)[0]
        return [_coerce_value(f"{field_name}[]", item, item_type) for item in value]

    if expected_type is bool:
        if not isinstance(value, bool):
            raise ConfigError(f"field '{field_name}' must be a boolean")
        return value

    if expected_type is int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ConfigError(f"field '{field_name}' must be an integer")
        return value

    if expected_type is float:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ConfigError(f"field '{field_name}' must be a float")
        return float(value)

    if expected_type is str:
        if not isinstance(value, str):
            raise ConfigError(f"field '{field_name}' must be a string")
        return value

    return value
