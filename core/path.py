from core.record import RecordOnScreen
import curses

class Path:
    """Class to representing path between RecordOnScreen
    """

    _diagonal = False
    _vertical = '|'
    _horizontal = '-'
    _rdiagonal = '/'
    _ldiagonal = '\\'
    _plus = '+'

    @staticmethod
    def print_path(rec1: RecordOnScreen, rec2: RecordOnScreen, win):
        """Simple function which computes and write paths.
        By deafault paths are drawed like follows:
                    -----Child
                    | 
                Base|

        if _diagonal is set path are drawed with diagonal lines:
                    + Child
                  +  
                +
                Base
        """
        if Path._diagonal:
            if rec2.y > rec1.y and rec2.x > rec1.x:
                invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
                curx = rec2.x
                for coordinate in range(rec2.y, rec1.y, -1):
                    win.pad.addch(coordinate, curx, Path._plus)
                    rec2.path.append((coordinate, curx))
                    win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
                    curx -= invslope
            if rec2.y > rec1.y and rec2.x < rec1.x:
                invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
                curx = rec2.x
                for coordinate in range(rec2.y, rec1.y, -1):
                    win.pad.addch(coordinate, curx, Path._plus)
                    rec2.path.append((coordinate, curx))
                    win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
                    curx -= invslope
            elif rec2.y < rec1.y and rec2.x > rec1.x:
                invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
                curx = rec2.x
                for coordinate in range(rec2.y, rec1.y):
                    win.pad.addch(coordinate, curx, Path._plus)
                    rec2.path.append((coordinate, curx))
                    win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
                    curx += invslope
            elif rec2.y < rec1.y and rec2.x < rec1.x:
                invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
                curx = rec2.x
                for coordinate in range(rec2.y, rec1.y):
                    win.pad.addch(coordinate, curx, Path._plus)
                    rec2.path.append((coordinate, curx))
                    win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
                    curx += invslope
        
        else:
            if rec2.y >= rec1.y and rec2.x > rec1.x:
                for y in range(rec1.y, rec2.y):
                    win.pad.addch(y, rec1.x+len(rec1.data), Path._vertical)
                    rec2.path.append((y, rec1.x+len(rec1.data)))
                for x in range(rec1.x+len(rec1.data), rec2.x):
                    win.pad.addch(rec2.y, x, Path._horizontal)
                    rec2.path.append((rec2.y, x))
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
            if rec2.y >= rec1.y and rec2.x < rec1.x:
                for y in range(rec1.y+1, rec2.y):
                    win.pad.addch(y, rec1.x, Path._vertical)
                    rec2.path.append(((y, rec1.x)))
                for x in range(rec2.x+len(rec2.data), rec1.x+1):
                    win.pad.addch(rec2.y, x, Path._horizontal)
                    rec2.path.append((rec2.y, x))
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
            elif rec2.y < rec1.y and rec2.x > rec1.x:
                for y in range(rec1.y-1, rec2.y, -1):
                    win.pad.addch(y, rec1.x+len(rec1.data), Path._vertical)
                    rec2.path.append((y, rec1.x+len(rec1.data)))
                for x in range(rec1.x+len(rec1.data), rec2.x):
                    win.pad.addch(rec2.y, x, Path._horizontal)
                    rec2.path.append((rec2.y, x))
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
            elif rec2.y < rec1.y and rec2.x < rec1.x:
                for y in range(rec1.y-1, rec2.y, -1):
                    win.pad.addch(y, rec1.x, Path._vertical)
                    rec2.path.append((y, rec1.x))
                for x in range(rec2.x+len(rec2.data), rec1.x):
                    win.pad.addch(rec2.y, x, Path._horizontal)
                    rec2.path.append((rec2.y, x))
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)

        
        
