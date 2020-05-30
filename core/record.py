from typing import List
import curses
import json

class Record:
    """ Class representing basic unit in MindPy Root.
    """

    def __init__(self):
        self._data: str = None
        self._children: List = []
        self._parent = None
    
    def __eq__(self, rec: 'Record'):
        return self.data == rec.data and self.children == rec.children

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, str_data: str):
        self._data = str_data

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, chldrn: List['Record']):
        self._children = chldrn

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add_child(self, chld: 'Record') -> List['Record']:
        """ Function responsible for adding new child to Record.
        Children can be added only one at a time.
        """
        self._children.append(chld)

    def remove_child(self, chld: 'Record') -> List['Record']:
        """ Function responsible for removing new child to Record.
        Children can be removed only one at a time.
        """
        self._children.remove(chld)

    # Method required by Visitor design pattern.
    def accept(self, visitor):
        visitor.visit(self)

    # Visitor method to delete Records and clear screen
    def delete(self, visitor):
        visitor.delete(self)

    def edit(self, visitor, data: str):
        visitor.edit(self, data)

class RecordOnScreen(Record):
    """Class representing position of the Record on the screen
    """

    def __init__(self, y: int=0, x: int=0, parent=None):
        super().__init__()
        # x and y represent coordinates of window containing text!
        self._y = y
        self._x = x
        # holds the list of coordinates on the path
        # used to delete routes after deleting objects
        # those coordinates are writen on main window
        self._path = []

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    @y.setter
    def y(self, y: int):
        self._y = y

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def toJSON(self):
        json_dict = {
            'data':str(self.data),
            'y': self.y,
            'x': self.x,
            'children': [child.toJSON() for child in self.children]
        }
        return json_dict
