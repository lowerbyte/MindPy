import curses
from core.record import RecordOnScreen
from core.root import Root
import logging
import box
import core.visitor

def main(stdscr):
    # Clear screen
    root = None
    # highlighted element
    hl = None
    win = curses.newwin(curses.LINES - 1, curses.COLS - 1)
    v = core.visitor.Visitor(win)
    stdscr.clear()
    stdscr.refresh()
    box.Box.init_window(win)
    while True:
        ch = stdscr.getch()
        if ch == ord(':'):
            b = win.derwin(1,(curses.COLS-1), curses.LINES-2, 0)
            b.erase()
            #b.move(curses.LINES-2, 0)
            b.addstr(chr(ch))
            curses.echo()
            logging.info(ch)
            st = b.getstr().decode('utf-8')
            if st[0] == 's':
                ty, tx = win.getmaxyx()
                y = ty//2
                x = tx//2 
                logging.warning('s')
                root = Root(y, x, win)
                root.data = st[2:]
                root.accept(v)
                hl = v.highlight(root)
                #root.highlight_selected()
                curses.noecho()
                b.clear()
                b.refresh()
                #win.refresh()   
                #a.getkey()
                # Let the user edit until Ctrl-G is struck.
                #box.edit()

                # Get resulting contents
                #message = box.gather()

                #print(message)
            elif st[0] == 'a':
                logging.warning('a')
                c = RecordOnScreen()
                c.data = st[2:]
                # add child to highlihted element
                hl.add_child(c)
                logging.warning('{0}'.format(hl.children))
                root.accept(v)
                curses.noecho()
                #win.refresh()
                hl = v.highlight(c, ch)
                b.clear()
                b.refresh()
        elif ch == curses.KEY_RIGHT:
            logging.warning('KEY RIGHT')
            root.accept(v)
            hl = v.highlight(hl, ch)
        elif ch == curses.KEY_UP:
            logging.warning('KEY UP')
            root.accept(v)
            hl = v.highlight(hl, ch)
        elif ch == curses.KEY_DOWN:
            logging.warning('KEY DOWN')
            root.accept(v)
            hl = v.highlight(hl, ch)   
        elif ch == curses.KEY_LEFT:
            logging.warning('KEY LEFT')
            root.accept(v)
            hl = v.highlight(hl, ch)  
        #hl = v.highlight(hl)
        #root.highlight_selected()


if __name__=='__main__':
    logging.basicConfig(filename='mindpy.log')
    curses.wrapper(main)
