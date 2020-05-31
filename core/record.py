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
        chld.parent = self
        self._children.append(chld)
        
    def remove_child(self, chld: 'Record') -> List['Record']:
        """ Function responsible for removing new child to Record.
        Children can be removed only one at a time.
        """
        self._children.remove(chld)

    # Method required by Visitor design pattern.
    def accept(self, visitor):
        visitor.visit(self)

    def delete(self):
        # method used to delete whole branches of the tree
        if self.parent:           
            self.parent.remove_child(self)
        else:
            pass

        # iterate trough copy of the list as we are removing items while iterating
        for child in self.children[:]:
            child.delete()

    def edit(self, data: str):
        self.data = data
        

class RecordOnScreen(Record):
    """Class representing position of the Record on the screen
    """

    def __init__(self, y: int=0, x: int=0):
        super().__init__()
        # x and y represent coordinates of window containing text!
        self._y = y
        self._x = x

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

    @staticmethod
    def select(rec: 'RecordOnScreen', key_code: int=None):
        if key_code == curses.KEY_RIGHT:
            if rec.children:
                rec = rec.children[0]
        elif key_code == curses.KEY_DOWN:
            if rec.parent:
                idx = rec.parent.children.index(rec)
                if idx >= len(rec.parent.children)-1:
                    pass
                else:
                    rec = rec.parent.children[idx+1]
        elif key_code == curses.KEY_UP:
            if rec.parent:
                idx = rec.parent.children.index(rec)
                if idx <= 0:
                    pass
                else:
                    rec = rec.parent.children[idx-1]
        if key_code == curses.KEY_LEFT:
            if rec.parent:
                rec = rec.parent
                       
        return rec

    def toJSON(self):
        json_dict = {
            'data':str(self.data),
            'y': self.y,
            'x': self.x,
            'children': [child.toJSON() for child in self.children]
        }
        return json_dict
