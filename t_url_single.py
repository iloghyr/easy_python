#!/usr/bin/python     
#coding=utf-8  

import sys
import re
import md5



re_host = '([^ ]+\.[^ ]+\.[^ ]+/.*)\?'
re_var = '[\?|&]([^ ]+?)='



m1 = re.compile(re_host)
m2 = re.compile(re_var)
hash_url = {}
count = 1
count_no = 1
fno = open('noMatch','w')
for line in open('url'):
	try:
		count += 1
		url_head = m1.match(line).group(1)
		url_hash = md5.new(url_head+str(sorted(m2.findall(line)))).hexdigest()
		if hash_url.has_key(url_hash) == False:
			hash_url[url_hash] = line

	except Exception,e:
		url_hash = md5.new(line).hexdigest()
		if hash_url.has_key(url_hash) == False:
			hash_url[url_hash] = line
			print line
			fno.write(line)
			count_no += 1

print "before:",count
fout = open('afterDeal.txt','w')
count = 1
for i in hash_url:
	fout.write(hash_url[i])
	count+=1
fout.close()
print 'after:',count
print 'noMatch:',count_no
print "done"