"""Testes unitários da classe Task (sem mocks, foco em estado e ciclo de vida)."""

import pytest
from datetime import datetime, timedelta

from task_manager.task import Priority, Status, Task


@pytest.fixture
def task_valida():
    """Setup: tarefa com prazo futuro e título válido."""
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python e testes", Priority.ALTA, prazo)


def test_estado_inicial_atributos_e_status_padrao(task_valida):
    """Após criação válida, atributos corretos e status padrão PENDENTE (teste de estado)."""
    task_valida.validar()
    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python e testes"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.id is None
    assert task_valida.status == Status.PENDENTE


def test_titulo_curto_invalido():
    """Título com menos de 3 caracteres → ValueError ao validar."""
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError, match="3 caracteres"):
        task.validar()


def test_prazo_no_passado_invalido():
    """Prazo no passado → ValueError (contrato temporal)."""
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Titulo ok", "Desc", Priority.MEDIA, prazo)
    with pytest.raises(ValueError, match="passado"):
        task.validar()


def test_ciclo_vida_transicao_valida(task_valida):
    """Transição explícita de estado PENDENTE → EM_PROGRESSO."""
    assert task_valida.status == Status.PENDENTE
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO


def test_ciclo_vida_status_fora_do_enum(task_valida):
    """Valor que não é membro de Status → ValueError no setter."""
    with pytest.raises(ValueError, match="Status"):
        task_valida.status = "pendente"  # type: ignore[assignment]


def test_validar_nao_altera_estado_em_sucesso(task_valida):
    """validar() bem-sucedido não muda status nem demais campos."""
    task_valida.status = Status.EM_PROGRESSO
    task_valida.validar()
    assert task_valida.status == Status.EM_PROGRESSO
