from core.record import RecordOnScreen


class Path:
    """Class to representing path between RecordOnScreen
    """

    _vertical = '|'
    _hotizontal = '-'
    _rdiagonal = '/'
    _ldiagonal = '\\'
    _plus = '+'

    @staticmethod
    def print_path(rec1: RecordOnScreen, rec2: RecordOnScreen, win):
        """To calculate route simple Pitagors equation is used.
        """
        if rec2.y > rec1.y and rec2.x > rec1.x:
            invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
            curx = rec2.x
            for coordinate in range(rec2.y, rec1.y, -1):
                win.addch(coordinate, curx, Path._plus)
                rec2.path.append((coordinate, curx))
                win.refresh()
                curx -= invslope
        if rec2.y > rec1.y and rec2.x < rec1.x:
            invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
            curx = rec2.x
            for coordinate in range(rec2.y, rec1.y, -1):
                win.addch(coordinate, curx, Path._plus)
                rec2.path.append((coordinate, curx))
                win.refresh()
                curx -= invslope
        elif rec2.y < rec1.y and rec2.x > rec1.x:
            invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
            curx = rec2.x
            for coordinate in range(rec2.y, rec1.y):
                win.addch(coordinate, curx, Path._plus)
                rec2.path.append((coordinate, curx))
                win.refresh()
                curx += invslope
        elif rec2.y < rec1.y and rec2.x < rec1.x:
            invslope = (rec2.x - rec1.x) // (rec2.y - rec1.y)
            curx = rec2.x
            for coordinate in range(rec2.y, rec1.y):
                win.addch(coordinate, curx, Path._plus)
                rec2.path.append((coordinate, curx))
                win.refresh()
                curx += invslope

        
        
