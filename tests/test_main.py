from src.task import Task
from src.main import main

def test_main(capsys):
    task3 = Task(3, 'Task 3', 5)
    task4 = Task(4, 'Task 4')
    task5 = Task(5, 'Task 5', 2)
    tasks = [task3, task4, task5]
    tasks.sort(reverse = True, key = lambda task: task.priority)
    assert tasks[0] == task3
    assert tasks[1] == task5
    assert tasks[2] == task4
    main()
    captured = capsys.readouterr()
    assert "1 done" in captured.out
    assert "2 done" in captured.out
    assert "3 done" in captured.out
    assert "4 done" in captured.out
    assert "5 done" in captured.out
