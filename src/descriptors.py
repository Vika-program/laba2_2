from src.errors import InvalidTypeError, EmptyFieldError, PriorityError
from typing import Type, Any


class StringField:
    """Data descriptor"""
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        """
        Устанавливаем имя и переменную для хранения данных storage_name
        :param owner: класс, где используется дескриптор
        :param name: имя
        :return: None
        """
        self.name = name
        self.storage_name = f"_{name}"

    def __set__(self, instance: Any, value: str) -> None:
        """
        Устанавливаем значение, если оно подходит, иначе вызываем ошику
        :param instance: экземпляр класса
        :param value: значение, кторое хотим установить
        :return:
        """
        if not isinstance(value, str):
            raise InvalidTypeError(f"{self.name} должно быть строкой")
        if value.strip() == "":
            raise EmptyFieldError(f"Поле {self.name} не может быть пустым")
        setattr(instance, self.storage_name, value)

    def __get__(self, instance: Any, owner: Type[Any]) -> str:
        """
        Получаем значение атрибута
        :param instance: экземпляр класса
        :param owner: класс, где используется дескриптор
        :return: значение атрибута
        """
        if instance is None:
            return self
        if getattr(instance, self.storage_name, None) is None:
            raise AttributeError(f"{self.name} не установлен в init")
        return getattr(instance, self.storage_name, '')


class PriorityField:
    """Data descriptor"""
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        """
        Устанавливаем имя и переменную для хранения данных storage_name
        :param owner: класс, где используется дескриптор
        :param name: имя
        :return: None
        """
        self.name = name
        self.storage_name = f"_{name}"

    def __set__(self, instance: Any, value: int) -> None:
        """
        Устанавливаем значение, если оно подходит, иначе вызываем ошику
        :param instance: экземпляр класса
        :param value: значение, кторое хотим установить
        :return:
        """
        if not isinstance(value, int) or value <= 0 or value > 5:
            raise PriorityError(f"{self.name} должен быть от 1 до 5")
        setattr(instance, self.storage_name, value)

    def __get__(self, instance: Any, owner: Type[Any]) -> int:
        """
        Получаем значение атрибута
        :param instance: экземпляр класса
        :param owner: класс, где используется дескриптор
        :return: значение атрибута
        """
        if instance is None:
            return self
        if getattr(instance, self.storage_name, None) is None:
            raise AttributeError(f"{self.name} не установлен в init")
        return getattr(instance, self.storage_name, '')



class NotChange:
    """Non-data descriptor"""
    def __init__(self):
        """Инициализация"""
        self.data = {}

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        """
        Устанавливаем имя
        :param owner: класс
        :param name: имя
        :return:
        """
        self.name = name

    def __get__(self, instance: Any, owner: Type[Any]) -> str:
        """
        Возвращаем значение атрибута
        :param instance: экземпляр
        :param owner: класс
        :return: значение атрибута
        """
        if instance is None:
            return self
        return self.data.get(instance, 'created')

    def _set_value(self, instance: Any, value: str) -> None:
        """
        Устанавливаем значение
        :param instance: экземпляр класса
        :param value: значение
        """
        self.data[instance] = value
