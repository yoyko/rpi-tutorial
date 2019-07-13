#!/usr/bin/env python
import curses
import time

def main(stdscr):
	stdscr.nodelay(1)
	lt = time.time()
	while True:
		c = stdscr.getch()
		if c != -1:
			t = time.time()
			stdscr.addstr("key %d %.3f\n" % (c, t-lt))
			lt = t
		time.sleep(0.001)


curses.wrapper(main)
