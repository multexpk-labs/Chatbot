"""Small dependency-free conversation session example."""

from dataclasses import dataclass, field


@dataclass
class ChatSession:
    conversation_id: str
    messages: list[dict[str, str]] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        if role not in {"user", "assistant", "system"}:
            raise ValueError("unsupported role")
        if not content.strip():
            raise ValueError("message cannot be empty")
        self.messages.append({"role": role, "content": content})

    def recent(self, limit: int = 10) -> list[dict[str, str]]:
        if limit < 1:
            raise ValueError("limit must be positive")
        return self.messages[-limit:]
