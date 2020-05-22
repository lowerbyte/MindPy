from typing import List

class Record:
    """ Class representing basic unit in MindPy tree.
    """

    def __init__(self):
        self._data: str = None
        self._children: List = []
    
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

