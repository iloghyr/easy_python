import getopt
import sys

if __name__ == '__main__':
	short_opt = 'hi:o:'
	long_opt  = ['help', 'input=', 'output=']
	opts, args = getopt.getopt(sys.argv[1:], short_opt, long_opt)
	for opt, val in opts:
		print opt, ':', val