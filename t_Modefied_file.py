# _*_coding=utf-8 _*_
import fileinput
import re

p = re.compile(r'http[s]?://[w]{3}\.baidu\.com')

for line in fileinput.input(r'a.txt',inplace=1):
	if re.search(p,line) is not None:
		print line.strip()+'\n',
	else:
		print line,


print 'hello world'
	 

