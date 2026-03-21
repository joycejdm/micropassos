import pytest
from src.tracker import TaskTracker


@pytest.fixture
def tracker(tmp_path):
    test_file = tmp_path / "test_data.db"
    return TaskTracker(filepath=str(test_file))


def test_adicionar_tarefa_com_sucesso(tracker):
    task = tracker.add_task("Estudar", ["Ler docs", "Exercícios"])

    assert task["name"] == "Estudar"
    assert len(task["steps"]) == 2
    assert tracker.get_tasks()[0]["id"] == 1


def test_adicionar_tarefa_invalida(tracker):
    msg_erro = "A tarefa precisa de um nome e pelo menos um passo."
    with pytest.raises(ValueError, match=msg_erro):
        tracker.add_task("   ", ["Passo 1"])

    with pytest.raises(ValueError):
        tracker.add_task("Estudar", [])


def test_calculo_de_progresso(tracker):
    tracker.add_task("Limpar casa", ["Sala", "Cozinha"])

    assert tracker.get_progress(task_id=1) == 0.0

    tracker.complete_step(task_id=1, step_index=0)
    assert tracker.get_progress(task_id=1) == 50.0

    tracker.complete_step(task_id=1, step_index=1)
    assert tracker.get_progress(task_id=1) == 100.0
