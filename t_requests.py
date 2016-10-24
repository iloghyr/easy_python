#!/usr/bin/env python
#coding:utf-8
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

r = requests.get('http://www.baidu.com')
print r.text
print r.content
print r.status_code
print dir(r)

print 

s = requests.Session()
s.get('https://www.baidu.com')
print s.cookies


