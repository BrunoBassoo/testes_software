from __future__ import annotations

from datetime import datetime

from task_manager.repository import TaskRepository
from task_manager.task import Priority, Status, Task


class TaskService:
    """Orquestra criação, listagem e atualização de status (bônus)."""

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def criar_tarefa(
        self,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
    ) -> Task:
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> list[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Task:
        task = self.repository.find_by_id(id)
        if task is None:
            raise ValueError("Tarefa não encontrada")
        task.status = status
        return task
