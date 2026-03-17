from src.task import Task
from time import sleep
from random import randint


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    task1 = Task(1, 'Task 1', 3)
    task2 = Task(2, 'Task 2', 4)
    task3 = Task(3, 'Task 3', 5)
    task4 = Task(4, 'Task 4')
    task5 = Task(5, 'Task 5', 2)
    tasks = [task1, task2, task3, task4, task5]
    tasks.sort(reverse=True, key=lambda task: task.priority)

    while tasks:
        for task in tasks[:]:
            if task.is_ready():
                task.start()
                print(task.id, task.status)
                task.complete()
                print(task.id, task.status)
                tasks.remove(task)
            if task.status == 'created':
                task.change_priority()
                if task.priority >= 3:
                    task.set_status('ready')

if __name__ == "__main__":
    main()
