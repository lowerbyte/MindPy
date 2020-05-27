from core.record import RecordOnScreen
from core.visitor import Visitor

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class Root(Singleton, RecordOnScreen):
    """ Class representing mind Root.
    As there can be only one Root, Singleton pattern is used.
    """
    def __init__(self, y: int, x: int):
        super(Root, self).__init__(y, x)

    def print(self):
        v = Visitor()
        self.accept(v)
