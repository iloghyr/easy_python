#coding=utf-8
import time
a = '10/Oct/2013:15:25:12'
ret = time.strptime(a,'%d/%b/%Y:%H:%M:%S')
print ret
print time.strftime('%Y-%m-%d %H:%M:%S', ret)

a = '2016-03-25 17:01:01'
ret = time.strptime(a, '%Y-%m-%d %H:%M:%S')
print time.mktime(ret)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.mktime(ret)))

print time.strftime("%Y%m%d", time.localtime(1453046400))



a = '20160328170540'
ret = time.strptime(a, '%Y%m%d%H%M%S')
print time.mktime(ret)