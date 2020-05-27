import curses
from core.record import RecordOnScreen
from core.root import Root
import logging
import core.visitor
import sys
import argparse
from core.path import Path

def main(stdscr):
    # Clear screen
    root = None
    # highlighted element
    hl = None
    win = curses.newwin(curses.LINES - 1, curses.COLS - 1)
    v = core.visitor.Visitor(win)
    stdscr.clear()
    stdscr.refresh()
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
                y = ty//2-1
                x = tx//2-1 - len(st[2:])//2 -1
                logging.warning('s')
                root = Root(y, x, win)
                root.data = st[2:]
                root.accept(v)
                hl = v.highlight(root)
                #root.highlight_selected()
                curses.noecho()
                b.clear()
                b.refresh()
                win.move(y,x)
                win.refresh()
                #win.refresh()   
                #a.getkey()
                # Let the user edit until Ctrl-G is struck.
                #box.edit()

                # Get resulting contents
                #message = box.gather()

                #print(message)
            elif st[0] == 'a':
                b.clear()
                b.refresh()
                logging.warning('a')
                y, x = win.getyx()
                logging.warning('{0}, {1}'.format(y,x))
                win.move(y, x)
                win.refresh()
                cpos = stdscr.getch()
                while(cpos != ord('h')):
                    if cpos == curses.KEY_RIGHT:
                        win.move(y, x+1)
                        x += 1
                    elif cpos == curses.KEY_UP:
                        win.move(y-1, x)
                        y -= 1
                    elif cpos == curses.KEY_DOWN:
                        win.move(y+1, x) 
                        y += 1
                    elif cpos == curses.KEY_LEFT:
                        win.move(y, x-1) 
                        x -= 1
                    win.refresh()
                    curses.noecho()
                    cpos = stdscr.getch()
                c = RecordOnScreen(y,x)
                c.data = st[2:]
                # add child to highlihted element
                hl.add_child(c)
                logging.warning('{0}'.format(hl.children))
                root.accept(v)
                #win.refresh()
                hl = v.highlight(c, ch)
                win.move(y, x)
                win.refresh()
            elif st[0] == 'd':
                b.clear()
                b.refresh()
                hl.delete(v)
                root.accept(v)
                hl = v.highlight(root)
            elif st[0] == 'e':
                data = st[2:]
                b.clear()
                b.refresh()
                hl.edit(v, data)
                root.accept(v)

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
    parser = argparse.ArgumentParser()
    parser.add_argument('--draw')
    args = parser.parse_args()
    if args.draw == 'diagonal':
        Path._diagonal = True
    curses.wrapper(main)
