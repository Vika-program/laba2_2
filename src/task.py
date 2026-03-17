from src.descriptors import StringField, PriorityField, NotChange
from src.errors import InvalidChangeStatus, ChangeReadOnlyError, InvalidTypeError
from datetime import datetime
from time import sleep


class Task:
    description: str = StringField()
    priority: int = PriorityField()
    _status_descr = NotChange()


    def __init__(self, id: int, description: str, priority: int = 1) -> None:
        """Инициализиция"""
        self._id = id
        self._time_created = datetime.now()
        self.description = description
        self.priority = priority
        Task._status_descr._set_value(self, 'created') #non-data descriptor


    @property
    def status(self):
        """Поле для просмотра статуса"""
        return Task._status_descr.__get__(self, Task)

    def set_status(self, new_status: str) -> None:
        """
        Изменяем статус, если это не противоречит правилам
        :param new_status: новый статус
        """
        states = ['created', 'ready', 'running', 'done', 'failed']
        if new_status not in states:
            raise InvalidChangeStatus(f"Статус должен быть {states}")
        changes = {
            'created' : 'ready',
            'ready' : 'running',
            'running' : 'done'
        }
        if new_status != changes[self.status]:
            raise InvalidChangeStatus(f"Не возможно перейти из {self.status} в {new_status}")
        Task._status_descr._set_value(self, new_status)

    @property
    def id(self):
        """Поле для просмотра id"""
        return self._id

    @property
    def time_created(self) -> datetime:
        """Поле для просмотра времени создания"""
        return self._time_created

    def __setattr__(self, name, value):
        """Запрещаем изменение _id и _time_created
        :param name: имя
        :param value: значение
        """
        # если значение ещё не установлено (при инициализации)
        if (name == '_id' and not hasattr(self, '_id') and
                (not isinstance(value, int) or not value > 0)):
            raise InvalidTypeError("id должен быть положительным числом!")
        # уже установлено, пытаемся изменить
        if name == '_id' and hasattr(self, '_id'):
            raise ChangeReadOnlyError("Нельзя изменить id!")
        if name == '_time_created' and hasattr(self, '_time_created'):
            raise ChangeReadOnlyError("Нельзя изменить _time_created!")
        super().__setattr__(name, value)

    def start(self) -> None:
        """запускаем задачу"""
        self.set_status('running')
        sleep(2)

    def complete(self) -> None:
        """Завершаем задачу"""
        self.set_status('done')

    def is_ready(self):
        """Прорверяем, готова ли задача"""
        return self.status == 'ready'

    def change_priority(self) -> None:
        """Меняем приоритет задачи"""
        if self.priority < 5:
            if (datetime.now() - self._time_created).seconds % 5 == 0:
                self.priority += 1


