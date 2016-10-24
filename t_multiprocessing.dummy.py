#!/bin/evn python
#coding:utf-8
import urllib2 
import time
import os
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
    'http://www.baidu.com/a',
    'http://www.baidu.com/b', 
    'http://www.baidu.com/c', 
    'http://www.baidu.com/d', 
    'http://www.baidu.com/e', 
    'http://www.baidu.com/f',  
    'http://www.baidu.com/g', 
    'http://www.baidu.com/d', 
    'http://www.baidu.com/d', 
    'http://www.baidu.com/aa', 
    'http://www.baidu.com/aaaa', 
    'http://www.baidu.com/aaaa', 
    'http://www.baidu.com/index.html', 
    'http://www.baidu.com/index.php', 
    'http://www.baidu.com', 
    'http://www.qq.com'
    ]

def worker(url):
    print url, os.getpid()
    urllib2.urlopen(url)
    time.sleep(2)

# Make the Pool of workers
pool = ThreadPool(8) 
# Open the urls in their own threads
# and return the results
start = time.time()
results = pool.map(worker, urls)
#close the pool and wait for the work to finish 
pool.close() 
pool.join() 
print time.time() - start
