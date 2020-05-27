import curses
from core.record import RecordOnScreen
from core.root import Root
import logging
import core.visitor
import sys
import argparse
from core.path import Path
from core.canvas import Canvas

def main(stdscr):
    # Clear screen
    root = None
    # highlighted element
    hl = None
    win = Canvas(1000,1000)
    v = core.visitor.Visitor(win)
    stdscr.clear()
    stdscr.refresh()
    while True:
        ch = stdscr.getch()
        if ch == ord(':'):
            b = curses.newwin(1,(curses.COLS-1), curses.LINES-2, 0)
            b.erase()
            #b.move(curses.LINES-2, 0)
            b.addstr(chr(ch))
            curses.echo()
            logging.info(ch)
            st = b.getstr().decode('utf-8')
            if st[0] == 's':
                y = 1000//2-1
                x = 1000//2-1 - len(st[2:])//2 -1
                logging.warning('s')
                root = Root(y, x)
                root.data = st[2:]
                win.y = 500-curses.LINES//2
                win.x = 500-curses.COLS//2
                root.accept(v)
                hl = v.highlight(root)
                #root.highlight_selected()
                curses.noecho()
                b.clear()
                b.refresh()
                win.pad.move(y,x)
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
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
                y, x = win.pad.getyx()
                logging.warning('{0}, {1}'.format(y,x))
                win.pad.move(y, x)
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
                cpos = stdscr.getch()
                while(cpos != ord('p')):
                    if cpos == curses.KEY_RIGHT:
                        win.pad.move(y, x+1)
                        x += 1
                    elif cpos == curses.KEY_UP:
                        win.pad.move(y-1, x)
                        y -= 1
                    elif cpos == curses.KEY_DOWN:
                        win.pad.move(y+1, x) 
                        y += 1
                    elif cpos == curses.KEY_LEFT:
                        win.pad.move(y, x-1) 
                        x -= 1
                    win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
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
                win.pad.move(y, x)
                win.refresh(0, 0, (curses.LINES-1), curses.COLS-2)
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
        elif ch == ord('j'):
            win.y -= 1
            root.accept(v)
        elif ch == ord('k'):
            logging.warning('K')
            win.y += 1
            root.accept(v)
        elif ch == ord('h'):
            logging.warning('H')
            win.x -= 1
            root.accept(v)  
        elif ch == ord('l'):
            logging.warning('L')
            win.x += 1
            root.accept(v)
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
