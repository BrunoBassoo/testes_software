from __future__ import annotations

from datetime import datetime
from enum import Enum, IntEnum


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    """Tarefa com validação e controle de status (ciclo de vida)."""

    def __init__(
        self,
        id_: int | None,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
        status: Status | None = None,
    ) -> None:
        self.id = id_
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self._status = Status.PENDENTE if status is None else status

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: object) -> None:
        if not isinstance(value, Status):
            raise ValueError("Status inválido: use um membro de Status.")
        self._status = value

    def validar(self) -> None:
        """Garante título com 3+ caracteres e prazo não passado."""
        if self.titulo is None or len(self.titulo) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres")
        if self.prazo < datetime.now():
            raise ValueError("Prazo não pode estar no passado")
