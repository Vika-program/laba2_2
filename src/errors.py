
class InvalidTypeError(Exception):
    """Неверный тип"""
    pass

class EmptyFieldError(Exception):
    """Пустое поле"""
    pass

class PriorityError(Exception):
    """Ошибка в поел приоритета"""
    pass

class InvalidChangeStatus(Exception):
    """Некорректное изменение статуса"""
    pass

class ChangeReadOnlyError(Exception):
    """Изменение поля, предназначенного только для чтения"""
    pass
