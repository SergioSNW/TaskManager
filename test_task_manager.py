import json
import pytest
from task_manager import TaskManager

def make_manager(tmp_path, monkeypatch):
    path = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, "FILENAME", str(path))
    return TaskManager()


def test_complete_task_marks_existing_task_complete(tmp_path, monkeypatch):
    manager = make_manager(tmp_path, monkeypatch)
    manager.add_task("Write tests")
    manager.complete_task(1)

    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 1
    assert manager._tasks[0].completed is True

    with open(manager.FILENAME, "r") as f:
        data = json.load(f)
    assert data[0]["completed"] is True
    assert data[0]["description"] == "Write tests"


def test_complete_task_nonexistent_id_no_changes(tmp_path, monkeypatch, capsys):
    manager = make_manager(tmp_path, monkeypatch)
    manager.complete_task(42)

    assert manager._tasks == []
    captured = capsys.readouterr()
    assert "Task with id #42 not found." in captured.out


def test_complete_task_id_does_not_affect_other_tasks(tmp_path, monkeypatch):
    manager = make_manager(tmp_path, monkeypatch)
    manager.add_task("Task one")
    manager.add_task("Task two")

    manager.complete_task(2)

    assert manager._tasks[0].completed is False
    assert manager._tasks[1].completed is True


def test_complete_task_already_completed_stays_completed(tmp_path, monkeypatch):
    manager = make_manager(tmp_path, monkeypatch)
    manager.add_task("Repeat complete")
    manager.complete_task(1)
    manager.complete_task(1)

    assert manager._tasks[0].completed is True
    with open(manager.FILENAME, "r") as f:
        data = json.load(f)
    assert data[0]["completed"] is True
