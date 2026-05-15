# Atividade 09 — Task Manager (CC8550)

Sistema simples de gerenciamento de tarefas em Python com testes alinhados à **Aula 09** (testes orientados a objetos e componentes): estado do objeto, fixtures (setup), isolamento com **stub** e **mock**, sequência de operações e distinção entre teste **unitário** (`Task`) e de **componente** (`TaskRepository` com `InMemoryStorage` substituído por mock).

## Estrutura

```text
lab9/
  pytest.ini
  requirements.txt
  README.md
  task_manager/
    __init__.py
    task.py          # Task, Priority, Status
    storage.py       # InMemoryStorage
    repository.py    # TaskRepository
    service.py       # TaskService (bônus)
  tests/
    test_task.py         # unitário: sem mocks
    test_repository.py   # componente: mock no storage
```

## Instalação

```bash
cd lab9
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Testes

```bash
pytest -v
```

Cobertura (opcional):

```bash
pytest --cov=task_manager -v
```

## Conceitos (Aula 09)

| Conceito | Onde aparece |
|----------|----------------|
| Teste de estado | `test_task.py`: atributos após criação e após mudar `status` |
| Setup / fixture | `task_valida`, `repo`, `mock_storage`, `task` |
| Mock + assert de chamada | `test_save_chama_storage_add_uma_vez` |
| Stub (`return_value`) | `test_find_by_id_stub_retorno_do_storage`, `test_find_all_lista_vazia` |
| Interação entre métodos | `test_sequencia_save_depois_find_by_id` |
| Unitário vs componente | `test_task.py` sem colaboradores; `test_repository.py` com lógica real do repositório e storage mockado |
| `pytest-mock` | `test_pytest_mocker_spy_em_storage_real` (`mocker.spy` em `InMemoryStorage.add`) |

## Uso rápido (integração manual)

```python
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.storage import InMemoryStorage
from task_manager.repository import TaskRepository

storage = InMemoryStorage()
repo = TaskRepository(storage)
prazo = datetime.now() + timedelta(days=5)
task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
task.validar()
salva = repo.save(task)
```
