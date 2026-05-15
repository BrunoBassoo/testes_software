from __future__ import annotations

from typing import Any


class InMemoryStorage:
    """Armazenamento em memória (dicionário)."""

    def __init__(self) -> None:
        self._data: dict[int, Any] = {}

    def add(self, id: int, item: Any) -> None:
        self._data[id] = item

    def get(self, id: int) -> Any | None:
        return self._data.get(id)

    def get_all(self) -> list[Any]:
        return list(self._data.values())

    def delete(self, id: int) -> bool:
        if id not in self._data:
            return False
        del self._data[id]
        return True

    def clear(self) -> None:
        self._data.clear()
