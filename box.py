"""This modul represents basic unit of MindMap - graphical representation of
Record.
"""

import curses
from core.record import Record
import logging

class Box:
    w = None
    y, x = 0, 0
    def __init__(self, rec: Record, y_pos: int, x_pos: int) -> None:
        self._data_size = len(rec.data)
        self._parent_win = Box.w
        self._win_size = (1, self._data_size)
        self._box_pos = (y_pos, x_pos-(self._data_size)//2)
        self._win = Box.w
        self._rec = rec
    
    def print(self):
        #logging.warning(self._rec.data)
        self._win.addstr(*self._box_pos, self._rec.data)
        self._win.refresh()

    @staticmethod
    def init_window(win):
        Box.w = win
        ty, tx = win.getmaxyx()
        Box.y = ty//2
        Box.x = tx//2 

    # Method required by Visitor design pattern.
    def accept(self, visitor):
        visitor.visit(self)

class RootBox(Box):
    """Class representing graphicaly root of the tree
    """
    def __init__(self, root) -> None:
        super().__init__(root, Box.y, Box.x)
        self._data_size = len(root.data)
        self._root = root
        #self._win = self._parent_win.derwin(*self._win_size, *self._box_pos)

    def get_win_pos_and_size(self):
        ty, tx = self._box_pos
        return ty, tx, self._data_size



