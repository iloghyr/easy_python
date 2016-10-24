#---------------------------------------------------------
# Name:        URL Unique mapper
#--------------------------------------------------------

import sys
import re
import md5


m1 = re.compile('(([\w]+\.){1,}[\w]+/.*?)\?')
m2 = re.compile('[&]([^ ]+?)=')
m3 = re.compile('[\?]([^ ]+?)=')
hash_url = {}
for line in sys.stdin:
	try:
		line = line.strip()
		if line[0:1] == '-' or line[0:3] == 'hm.':
			continue
		url_head = m1.match(line).group(1)
		var_list = m2.findall(line)
		var_list.append(m3.findall(line)[0])
		url_hash = md5.new(url_head+str(sorted(var_list))).hexdigest()
		if hash_url.has_key(url_hash) == False:
			hash_url[url_hash] = line

	except Exception,e:
		pass
for i in hash_url:
	print '%s\t%s'%(i,hash_url[i])
