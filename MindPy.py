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
    # highlighted element
    hl = None
    root = None
    win = Canvas(1000,1000)
    v = core.visitor.Visitor(win)

    # Main program loop
    while True:
        # window reponsible for interaction with human
        hmi = curses.newwin(1,(curses.COLS-1), curses.LINES-1, 0)
        ch = stdscr.getch()
        if ch == ord(':'):
            hmi.erase()
            hmi.addstr(chr(ch))
            curses.echo()

            user_input = hmi.getstr().decode('utf-8').split(' ', maxsplit=1)
            if user_input[0] == 's':
                if len(user_input) < 2 or user_input[-1]=='':
                    continue
                # calculate position of root element
                pad_size = win.size
                y = pad_size[0]//2-1
                x = pad_size[1]//2-1 - len(user_input[1])//2 -1

                # create root element
                root = Root(y, x)
                root.data = user_input[1]

                # use Visitor design pattern to print out tree
                root.accept(v)
                hl = v.highlight(root)

                curses.noecho()
                hmi.clear()
                hmi.refresh()

                # move cursor to new position
                win.pad.move(y,x)
                win.refresh()

            elif user_input[0] == 'a' and root:
                if len(user_input) < 2 or user_input[-1]=='':
                    continue
                # set cursos position
                y, x = win.pad.getyx()
                win.pad.move(y, x)
                win.refresh()     
                
                # print instruction
                hmi.addstr('Set cursor position using arrow keys. Hit p to put text.')
                hmi.refresh()
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
                    win.refresh()                    
                    curses.noecho()
                    cpos = stdscr.getch()

                # create new RecordOnScreen
                c = RecordOnScreen(y,x)
                c.data = user_input[1]

                # add child to highlihted element
                hl.add_child(c)
                root.accept(v)

                hmi.erase()
                hmi.refresh()
                # highlight new child
                hl = v.highlight(c, ch)
                win.pad.move(y, x)
                win.refresh()

            elif user_input[0] == 'd' and root:
                hmi.clear()
                hmi.refresh()
                hl.delete(v)
                root.accept(v)
                hl = v.highlight(root)
                curses.noecho()

            elif user_input[0] == 'e' and root:
                data = user_input[1]
                hmi.clear()
                hmi.refresh()
                hl.edit(v, data)
                root.accept(v)
                curses.noecho()

            elif user_input[0] == 'w':
                logging.warning('W')
                logging.warning(root.toJSON())

            elif user_input[0] == 'h':
                hmi.erase()
                hmi.addstr("Hit q to quit help.")
                hmi.refresh()
                win.print_help()
                curses.noecho()
                q = stdscr.getch()
                while(q != ord('q')):
                    q = stdscr.getch()
                win.pad.clear()
                win.refresh()
                hmi.erase()
                hmi.refresh()
                if root:
                    root.accept(v)

            elif user_input[0] == 'q':
                return 0

            else:
                curses.noecho()
                hmi.clear()
                hmi.addstr("You have to create root first (:s)!")
                hmi.refresh()
                
        elif ch == curses.KEY_RIGHT:
            root.accept(v)
            hl = v.highlight(hl, ch)

        elif ch == curses.KEY_UP:
            root.accept(v)
            hl = v.highlight(hl, ch)

        elif ch == curses.KEY_DOWN:
            root.accept(v)
            hl = v.highlight(hl, ch)  

        elif ch == curses.KEY_LEFT:
            root.accept(v)
            hl = v.highlight(hl, ch)  
        
        # keys responsible for moving the pad
        elif ch == ord('j'):
            win.y -= 1
            if root:
                root.accept(v)

        elif ch == ord('k'):
            win.y += 1
            if root:
                root.accept(v)

        elif ch == ord('h'):
            win.x -= 1
            if root:
                root.accept(v)

        elif ch == ord('l'):
            win.x += 1
            if root:
                root.accept(v)

        else:
            hmi.addstr('Incorrect command. Type :h for list of possible commands.')
            hmi.refresh()


if __name__=='__main__':
    logging.basicConfig(filename='mindpy.log')
    parser = argparse.ArgumentParser()
    parser.add_argument('--draw')
    args = parser.parse_args()
    if args.draw == 'diagonal':
        Path._diagonal = True
    curses.wrapper(main)
