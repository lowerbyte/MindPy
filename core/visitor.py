from core.record import RecordOnScreen
from box import Box, RootBox
import core.root
import logging
import curses

class Visitor:
    """ Visitor class - mainly used to print the Root
    """
    def __init__(self, win):
        self.vwin = win

    def visit(self, rec: RecordOnScreen):        
        rec.win.addstr(rec.y, rec.x, rec.data)
        rec.win.refresh()
        child_no = len(rec.children)
        
        if not rec.children:
            return

        # get longest data from children to create a new subwindow
        longest_child = max(len(rec.data) for rec in rec.children)

        # create subwin of size (no_of_children+1, longest_data) at
        # (relative_parent.y + parent.y-half_of_children (to center output), relative_parent.x+parent.x+parent.data+1)
        # Why this is done like this? Because for weach children list there is new window created
        # and Records inside it holds relative positions to it's origin.
        # relative_parent provides coordinates realtive to whole screen
        tmp_win = self.vwin.subwin(len(rec.children)+1, longest_child+1,
                rec.win.getparyx()[0] + rec.y - len(rec.children)//2, (rec.win.getparyx()[1] + rec.x + len(rec.data)) + 1)
        for idx, row in enumerate(rec.children):
            # assign parent to children
            row.parent = rec
            # coordinates relative to new subwindow
            x = 0
            y = 0 + idx
            row.x = x
            row.y = y
            row.win = tmp_win
            row.win.clear()
        
        for child in rec.children:
            child.accept(self)
        
    @classmethod
    def highlight(self, rec, key_code=None):
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
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        rec.win.attron(curses.color_pair(1))
        rec.win.addstr(rec.y, rec.x, rec.data)
        rec.win.attroff(curses.color_pair(1))
        rec.win.refresh()
        return rec