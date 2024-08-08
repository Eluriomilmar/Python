import curses
from curses import wrapper
import time

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(f"{a}")
    stdscr.refresh()
    stdscr.clear
    stdscr.getch()
    stdscr.refresh()
    time.sleep(3)

wrapper(main)