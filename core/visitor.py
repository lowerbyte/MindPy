from core.record import RecordOnScreen
import core.root
import logging
import curses
import core.path

class Visitor:
    """ Visitor class - used to print the tree
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
       