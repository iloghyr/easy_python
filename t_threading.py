#!/usr/bin/env python
#coding:utf-8
# Author:  
# Purpose:
# Created: 2013年3月27日
import threading
import time
st = [3,4]
#多线程1
class MyThread1(threading.Thread):
	def __init__(self,func,i,sec):
		threading.Thread.__init__(self)
		self.func  = func
		self.sec = sec
		self.i = i
	def run(self):
		apply(self.func,(self.i,self.sec))

def loop(i,sec):
	print 'start %d loop'%i
	time.sleep(sec)
	print 'end %d loop'%i

def main1():
	print "start",time.ctime()
	threadcount = []
	irange = range(len(st))
	for i in irange:
		threadcount.append(MyThread1(loop,i,st[i]))
	for i in irange:
		threadcount[i].start()
	for i in irange:
		threadcount[i].join()
	print 'done',time.ctime()


#多线程 2 竞争条件
num = 0
mutex = threading.Lock()
class MyThread2(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		pass
	def run(self):
		time.sleep(1)
		global num;
		mutex.acquire(1)
		num += 1
		mutex.release()
		print self.name,'num:',str(num)

def main2():
	for i in xrange(10):
		t = MyThread2()
		t.start()


main1()
#main2()


