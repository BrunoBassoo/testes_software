"""Testes de componente: TaskRepository com storage mockado (Aula 09)."""

import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock

from task_manager.repository import TaskRepository
from task_manager.task import Priority, Task


@pytest.fixture
def mock_storage():
    return Mock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Desc", Priority.BAIXA, prazo)


def test_save_atribui_id_estado_e_interacao(repo, task):
    """Após save(), task.id definido (estado + sequência save → id)."""
    resultado = repo.save(task)
    assert resultado.id == 1
    assert task.id == 1


def test_save_chama_storage_add_uma_vez(repo, task, mock_storage):
    """Mock: storage.add chamado exatamente uma vez com (id, task)."""
    repo.save(task)
    mock_storage.add.assert_called_once()
    mock_storage.add.assert_called_once_with(1, task)


def test_find_by_id_stub_retorno_do_storage(repo, task, mock_storage):
    """Stub: get.return_value configurado; repositório delega e retorna o objeto."""
    mock_storage.get.return_value = task
    assert repo.find_by_id(1) is task
    mock_storage.get.assert_called_once_with(1)


def test_sequencia_save_depois_find_by_id(repo, task, mock_storage):
    """Interação entre métodos: salvar e recuperar o mesmo recurso."""
    salva = repo.save(task)
    mock_storage.get.return_value = salva
    encontrada = repo.find_by_id(salva.id)
    assert encontrada is salva
    mock_storage.add.assert_called_once()
    mock_storage.get.assert_called_once_with(1)


def test_find_all_lista_vazia_quando_storage_vazio(repo, mock_storage):
    """Isolamento: get_all vazio → find_all retorna []."""
    mock_storage.get_all.return_value = []
    assert repo.find_all() == []


def test_delete_delega_storage(repo, mock_storage):
    """delete repassa id ao storage e propaga retorno booleano."""
    mock_storage.delete.return_value = True
    assert repo.delete(3) is True
    mock_storage.delete.assert_called_once_with(3)


def test_pytest_mocker_wraps_add_em_storage_real(mocker, task):
    """
    pytest-mock: registra chamadas a add mantendo o comportamento real (wraps).

    Usamos patch.object + wraps em vez de spy em método de instância, pois em
    alguns ambientes spy() não acumula chamadas de forma confiável quando o
    repositório invoca self.storage.add(...).
    """
    from task_manager.storage import InMemoryStorage

    storage = InMemoryStorage()
    add_real = storage.add
    add_rastreado = mocker.patch.object(storage, "add", wraps=add_real)
    repo = TaskRepository(storage)
    repo.save(task)
    add_rastreado.assert_called_once_with(1, task)
    assert storage.get(1) is task
