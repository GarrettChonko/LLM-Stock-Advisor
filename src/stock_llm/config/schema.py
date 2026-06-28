"""Typed configuration schemas for the project."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class TokenizerConfig:
    """Settings for future tokenizer experiments."""

    name: str
    vocab_size: int
    lowercase: bool = False
    min_frequency: int = 2
    special_tokens: list[str] = field(default_factory=lambda: ["<pad>", "<bos>", "<eos>", "<unk>"])

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if self.vocab_size <= 0:
            raise ValueError("vocab_size must be greater than 0")
        if self.min_frequency <= 0:
            raise ValueError("min_frequency must be greater than 0")
        if not self.special_tokens:
            raise ValueError("special_tokens must contain at least one value")
        if any(not token.strip() for token in self.special_tokens):
            raise ValueError("special_tokens must not contain empty strings")


@dataclass(slots=True)
class ModelConfig:
    """Settings for future tiny-model experiments."""

    name: str
    vocab_size: int
    context_length: int
    n_layers: int
    n_heads: int
    hidden_size: int
    dropout: float = 0.0

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if self.vocab_size <= 0:
            raise ValueError("vocab_size must be greater than 0")
        if self.context_length <= 0:
            raise ValueError("context_length must be greater than 0")
        if self.n_layers <= 0:
            raise ValueError("n_layers must be greater than 0")
        if self.n_heads <= 0:
            raise ValueError("n_heads must be greater than 0")
        if self.hidden_size <= 0:
            raise ValueError("hidden_size must be greater than 0")
        if not 0.0 <= self.dropout <= 1.0:
            raise ValueError("dropout must be between 0.0 and 1.0")


@dataclass(slots=True)
class TrainingConfig:
    """Settings for future training runs."""

    name: str
    batch_size: int
    learning_rate: float
    max_steps: int
    eval_interval: int
    checkpoint_interval: int
    seed: int = 42

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if self.batch_size <= 0:
            raise ValueError("batch_size must be greater than 0")
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be greater than 0")
        if self.max_steps <= 0:
            raise ValueError("max_steps must be greater than 0")
        if self.eval_interval <= 0:
            raise ValueError("eval_interval must be greater than 0")
        if self.checkpoint_interval <= 0:
            raise ValueError("checkpoint_interval must be greater than 0")
