from core.record import RecordOnScreen
import core.root
import logging
import curses
import core.path

class Visitor:
    """ Visitor class - mainly used to print the Root
    """

    def __init__(self, win):
        # screen instance
        self.vwin = win

    def visit(self, rec: RecordOnScreen): 
        # reposnsible for drawing the tree
        self.vwin.pad.addstr(rec.y, rec.x, rec.data)
        self.vwin.refresh()        
        if not rec.children:
            return

        for idx, row in enumerate(rec.children):
            core.path.Path.print_path(rec, row, self.vwin)
  
        for child in rec.children:
            child.accept(self)


    def highlight(self, rec: RecordOnScreen, key_code: int=None):
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
        # initialize color pair
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # turn color pair on
        self.vwin.pad.attron(curses.color_pair(1))
        self.vwin.pad.addstr(rec.y, rec.x, rec.data)
        # turn color off
        self.vwin.pad.attroff(curses.color_pair(1))
        self.vwin.refresh()        
        return rec