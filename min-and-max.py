#!/usr/bin/env python

import sys


def hello():
	print "Hello, World !"


def usage():
	print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
	if len(sys.argv) != 2:
		print "Number of arguments must be 1 !"
		usage()
		sys.exit(1)

	try:
		fp = open(sys.argv[1], "r")
	except IOError, e:
		print >> sys.stderr, "Argument is not a valid filename"
		usage()
		sys.exit(1)

	for idx, line in enumerate(list(fp)):
		print "%d : %s" %(idx+1, line),

if __name__ == "__main__":
	sys.exit(main())
