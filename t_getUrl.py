#i = 1
#for i in range(0,10):
    #print "%d"%i,
    
#list1= ["d",'b','c']
#list1.reverse()
#print list1
#print list1[0:1:1]

#×ÖµäÅÅÐò
#d1 = {'a':'apple','b':'banana','c':'orange'}
#print d1.get('a','abcd')
#print sorted(d1.items(),key=lambda d:d[0])

#str = 'hello'
#print str[::-1]
#print range(1,3)
#print 'a'+str(1)
#print 'abcd'.index('abc')
#str1 = 'abc'
#print '..'.join(['apple','banana'])
import urllib2
url = 'http://www.baidu.com/link?url=niM4GJqjJ4zBBpC8yDF8xDh8vibi0V2fEXEUr9UP2dqqP6sxWns8aRxuL8Gpoz8C3ou_0lKoxohm2kYsPP_RAyCzWWl2'
r = urllib2.Request(url)
r = urllib2.urlopen(r)
call = r.geturl()
print call

