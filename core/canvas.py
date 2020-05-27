import curses
from core.record import RecordOnScreen

class Canvas:

    def __init__(self, nrows: int, ncols: int):
        self._pad = curses.newpad(nrows, ncols)
        # current pad y position
        self._pad_y = 0
        # current pad x position
        self._pad_x = 0

    @property
    def y(self):
        return self._pad_y

    @y.setter
    def y(self, y: int):
        self._pad_y = y

    @property
    def x(self):
        return self._pad_x

    @x.setter
    def x(self, x: int):
        self._pad_x = x

    @property
    def pad(self):
        return self._pad

    # lu stands for left upper, rl stands for right lower
    # see documentation of refresh in curses
    def refresh(self, ylu: int, xlu: int, yrl: int, xrl: int):
        self.pad.refresh(self.y, self.x, ylu, xlu, yrl, xrl)




