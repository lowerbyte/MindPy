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
        self.vwin.pad.addstr(rec.y, rec.x, rec.data)
        self.vwin.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
        
        if not rec.children:
            return

        for idx, row in enumerate(rec.children):
            row.parent = rec
            core.path.Path.print_path(rec, row, self.vwin)
  
        for child in rec.children:
            child.accept(self)


    def delete(self, rec: RecordOnScreen):            
        if rec.parent:
            for cor in rec.path:
                self.vwin.pad.delch(*cor)
                self.vwin.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
            rec.parent.remove_child(rec)
            self.vwin.pad.erase()
        else:
            pass

        # iterate trough copy of the list as we are removing items while iterating
        for child in rec.children[:]:
            child.delete(self)

    def edit(self, rec: RecordOnScreen, data: str):            
        if rec.children:
            for child in rec.children:
                for cor in child.path:
                    self.vwin.pad.delch(*cor)
                    self.vwin.refresh(0, 0, (curses.LINES-1), curses.COLS-2)

            self.vwin.pad.clear() 
            rec.data = data
        else:
            pass
        

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
        self.vwin.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
        return rec