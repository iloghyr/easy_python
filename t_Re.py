import re

m = re.compile('\w\w\w-\d\d\d')
m = re.findall(m,'aaa-000-123-aaa-002')
if m is not None:
	print m

print '*' * 10
re_url = r'(?!(index\.php))(.*)'
url1 = "Monitor/PkgMonitor.html"
url2 = "index.php/Monitor/PkgMonitor.html"

m1 = re.compile(re_url)
print m1.findall(url2)

print '*' * 10

re_host = '([^ ]+\.[^ ]+\.[^ ]+/.*)\?'
re_var = '[\?|&]([^ ]+?)='


url = 'wenku.bxaidu.com/tongji/view.html?type=jsonload&t=1374595009015&doc_id=ec6f38d4195f312b3169a573&v=6&time=7062&bcs=1&pn=1'

m1 = re.compile(re_host)
print m1.match(url).group(1)
m2 = re.compile(re_var)
print m2.findall(url)


# m = re.compile(r'(.+?)/.*')

# for con in open('bfe_result_attack.txt'):
# 	domain = re.match(m,con).group(1)
	
#import json

# s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
# print s
# print s.keys()
# print s["name"]
# print s["type"]["name"]
# print s["type"]["parameter"][1]


# json_str = "{'name':'bob','age':'b'}"
# a =  json.loads('{"name":"bob","age":"b"}')
# print a['name']






#fobj = open('a.txt','r')
#fout = open("b.txt",'w')
#line = fobj.readline()
#while line:
#    line = line.split(' ')[1]
#   fout.write(line)
#    print line
#    line = fobj.readline()
#print '..'.join(['apple','banana']) 
#apple..banana
# import copy


# l1 = ['tom',['saving','100.0']]
# l2 = copy.deepcopy(l1)
# l1[0] = 'bob'

# print l1
# print l2
# import copy
# d1 = {}.fromkeys(['host','name'],80)
# d1['host'] = 'localhost'
# d2 = d1.copy()
# d2['host'] = 'bob'
# print 'host %(name)s' %d1
# print str(d1)
# print str(d2)
# print hash('123')
# l1 = ['a','b']
# print l1.pop()
# print l1
# import copy
# d1 = {}.fromkeys(['host','name'],80)
# d1['host'] = 'localhost'
# d2 = copy.deepcopy(d1)
# d2['name'] = 90
# print d1
# print d2
# s = set('abcdefghijklmnopqrstuvwxyz')
# s2 = set('aaaabc')
# print s2

