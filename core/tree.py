from core.record import Record
from core.visitor import Visitor

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Tree(Singleton, Record):
    """ Class representing mind tree.
    As there can be only one tree, Singleton pattern is used.
    """
    def __init__(self):
        super(Tree, self).__init__()

    def print(self):
        v = Visitor()
        self.accept(v)

'''
if __name__ == '__main__':
    a = Tree()
    a.data = 'aaa'
    b = Record()
    b.data = 'bbb'
    c = Record()
    c.data = 'ccccc'
    a.add_child(b)
    a.add_child(c)
    d = Record()
    d.data = 'ddd'
    e = Record()
    e.data = 'eeeee'
    b.add_child(d)
    b.add_child(e)
    a.print() 
    print('\n')
    b.remove_child(e)
    a.remove_child(c)
    a.print()
'''