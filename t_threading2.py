#!/usr/bin/env python
#coding:utf-8
# Author:  
# Purpose:
# Created: 2013年3月27日
import threading
import time
def worker(i=1):
    print "test:",i
    time.sleep(2)
    print 'after'
 
for i in xrange(5):
    t = threading.Thread(target=worker,args=[2])
    t.start()
time.sleep(5)

print "current has %d threads" % (threading.activeCount() - 1)
