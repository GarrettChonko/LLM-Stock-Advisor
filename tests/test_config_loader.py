import pytest

from stock_llm.config import (
    ConfigError,
    ModelConfig,
    TokenizerConfig,
    TrainingConfig,
    load_model_config,
    load_tokenizer_config,
    load_training_config,
)


def test_load_valid_tokenizer_config() -> None:
    config = load_tokenizer_config("tokenizer_tiny.yaml")

    assert isinstance(config, TokenizerConfig)
    assert config.name == "tokenizer_tiny"
    assert config.vocab_size == 8000
    assert config.lowercase is True


def test_load_valid_model_config() -> None:
    config = load_model_config("model_tiny.yaml")

    assert isinstance(config, ModelConfig)
    assert config.name == "model_tiny"
    assert config.context_length == 256
    assert config.dropout == pytest.approx(0.1)


def test_load_valid_training_config() -> None:
    config = load_training_config("training_tiny.yaml")

    assert isinstance(config, TrainingConfig)
    assert config.name == "training_tiny"
    assert config.batch_size == 16
    assert config.learning_rate == pytest.approx(0.0003)


def test_missing_config_file_gives_clear_error() -> None:
    with pytest.raises(ConfigError, match="Config file not found"):
        load_tokenizer_config("missing_tokenizer.yaml")


def test_invalid_config_gives_clear_error() -> None:
    invalid_config = "tests/fixtures/invalid_model.yaml"
    with pytest.raises(ConfigError, match="field 'n_heads' must be an integer"):
        load_model_config(invalid_config)
