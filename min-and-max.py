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
	students = []
	for line in list(fp):
		#print "%d : %s" %(idx+1, line),
		tokens = line.strip().split(';')
		#print tokens
		student = {
		'first_name': tokens[0],
		'last_name': tokens[1],
		'group': tokens[2],
		'grade': int(tokens[3])
		}

		students.append(student)
	#print students

	grade_min = 11;
	grade_max = -1;
	student_bun = []
	student_prost = []

	for s in students:
		if grade_max < s['grade']:
			grade_max = s['grade']
			student_bun = s 
		if grade_min > s['grade']:
			grade_min = s['grade']
			student_prost = s 
	print "Min grade is: %d", grade_min
	print "Max grade is: %d", grade_max
	print "Best student :", student_bun
	print "Wors fuking student:", student_prost
	
if __name__ == "__main__":
	sys.exit(main())
