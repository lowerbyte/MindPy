import curses
from core.record import Record
from core.tree import Tree
import logging
import box
import core.visitor

def main(stdscr):
    # Clear screen
    root = None
    v = core.visitor.Visitor()
    stdscr.clear()
    stdscr.refresh()
    win = curses.newwin(curses.LINES - 1, curses.COLS - 1,0,0)
    box.Box.init_window(win)
    while True:
        ch = win.getkey()
        if ch == ':':
            b = win.derwin(1,(curses.COLS-1), curses.LINES-2, 0)
            b.erase()
            #b.move(curses.LINES-2, 0)
            b.addstr(ch)
            curses.echo()
            logging.info(ch)
            st = b.getstr().decode('utf-8')
            if st[0] == 's':
                logging.warning('s')
                root = Tree()
                root.data = st[2:]
                curses.noecho()
                b.clear()
                b.refresh()
                win.refresh()   
                #a.getkey()
                # Let the user edit until Ctrl-G is struck.
                #box.edit()

                # Get resulting contents
                #message = box.gather()

                #print(message)
            elif st[0] == 'a':
                logging.warning('a')
                c = Record()
                c.data = st[2:]
                root.add_child(c)
                curses.noecho()
                win.refresh()
                b.clear()
                b.refresh()
        root.accept(v)


if __name__=='__main__':
    logging.basicConfig(filename='mindpy.log')
    curses.wrapper(main)
