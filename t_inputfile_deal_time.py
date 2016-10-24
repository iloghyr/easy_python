# _*_coding=utf-8 _*_

import fileinput
import re
import sys


mon = {'Mar':'03','Apr':'04'}
p = re.compile(r'"(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)" "(.*)"')
count = 1
for line in fileinput.input('deal.txt',inplace=1):
    count += 1
    if count%5000 == 0:
        print count,
    r= re.search(p,line)
    #time = r.group(2)
    #time1 = time.split(' ')[0].split('/')
    #t = time1[2][0:4]+'-'+mon[time1[1]]+'-'+time1[0]+' '+time1[2][5::]
    #line = re.sub('[\d]{2}/[\w]*/[\d]{4}[^"]*',t,line)
    print 'heooo'
    sys.stdout.write("asdf")
    print line,

print 'done'