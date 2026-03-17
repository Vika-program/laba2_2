from src.task import Task
from src.errors import ChangeReadOnlyError, PriorityError, InvalidChangeStatus, InvalidTypeError
import pytest
from time import sleep

def test_id():
    task = Task(1, 'test', 3)
    with pytest.raises(AttributeError):
        task.id = 2
    with pytest.raises(ChangeReadOnlyError):
        task._id = 2
    with pytest.raises(InvalidTypeError):
        task2 = Task(-1, 'test', 3)
    with pytest.raises(InvalidTypeError):
        task3 = Task('hh', 'test', 3)

def test_time():
    task = Task(1, 'test', 3)
    with pytest.raises(AttributeError):
        task.time_created = 2
    with pytest.raises(ChangeReadOnlyError):
        task._time_created = 2

def test_priority():
    task = Task(1, 'test', 3)
    with pytest.raises(PriorityError):
        task.priority = 0
    with pytest.raises(PriorityError):
        task.priority = ''
    task.priority = 1
    assert task.priority == 1

def test_status():
    task = Task(1, 'test', 3)
    with pytest.raises(AttributeError):
        task.status = "hhh"
    with pytest.raises(AttributeError):
        task.status = "ready"
    with pytest.raises(InvalidChangeStatus):
        task.set_status("done")
    with pytest.raises(InvalidChangeStatus):
        task.set_status("dhhh")
    task.set_status("ready")
    assert task.status == "ready"

def test_status2():
    task = Task(1, 'test', 3)
    assert task.status == "created"
    assert task.is_ready() is False
    task.set_status("ready")
    assert task.is_ready() is True
    task.start()
    assert task.status == "running"
    task.complete()
    assert task.status == "done"

def test_priority2():
    task = Task(1, 'test', 3)
    sleep(5)
    task.change_priority()
    assert task.priority == 4

