import curses
from core.record import RecordOnScreen


class Canvas:

    def __init__(self, nrows: int, ncols: int):
        self._pad = curses.newpad(nrows, ncols)
        self._size = (nrows, ncols)
        # current pad y position (to center root element)
        self._pad_y = nrows//2 - curses.LINES//2
        # current pad x position
        self._pad_x = ncols//2 - curses.COLS//2

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

    @property
    def size(self):
        return self._size

    # lu stands for left upper, rl stands for right lower
    # see documentation of refresh in curses
    def refresh(self):
        # LINES-2 due to hmi window (responsible for getting user input)
        self.pad.refresh(self.y, self.x, 0, 0, curses.LINES-2, curses.COLS-1)

    def print_help(self):
        help_text = [
            'Use h (left), j (up), k (down), l (right) to scroll screen',
            'Usage:',
            ' :<command> <text>',
            ' Commands: ',
            '    - s (start) - start map mind, creates root element,',
            '    - a (add) - add child to highlighted element,',
            '    - e (edit) - edit highlighted element,',
            '    - d (del) - delete highlighted element,',
            '    - w (write) - write to file,',
            '    - h (help) - print help',
            '    - l (load) - load serilized mind map'
        ]

        self.pad.clear()
        for i in range(len(help_text)):
            self.pad.addstr(self.y+i, self.x, help_text[i])
        self.pad.refresh(self.y, self.x, 0, 0, curses.LINES-2, curses.COLS-1)

    def highlight(self, rec: RecordOnScreen):
        # initialize color pair
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # turn color pair on
        self.pad.attron(curses.color_pair(1))
        self.pad.addstr(rec.y, rec.x, rec.data)
        # turn color off
        self.pad.attroff(curses.color_pair(1))
        self.refresh()
