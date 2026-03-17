import pytest
from src.descriptors import StringField, PriorityField, NotChange

def test_1():
    class A:
        x = StringField()
        def __init__(self):
            pass
    a = A()
    with pytest.raises(AttributeError):
        print(a.x)

    class B:
        x = PriorityField()
        def __init__(self):
            pass
    b = B()
    with pytest.raises(AttributeError):
        print(b.x)

    class C:
        _status_descr = NotChange()
        def __init__(self):
            C._status_descr._set_value(self,'test')
    c = C()
    C._status_descr._set_value(c, 'ss')
    assert C._status_descr.__get__(c, C) == 'ss'

