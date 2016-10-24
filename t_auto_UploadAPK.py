#c70e5e7fdf776b48de33312777c9e731
#coding=utf-8
import urllib2
import random 
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import os
import time
import json
import cookielib
import urllib
start = time.time()
users = []
for line in open('users'):
	users.append(line.strip())
def doLogin(user):
	head = {
	    'Referer':'https://login.ijinshan.com/fireeye/login.html?service=https%3A%2F%2Ffireeye.ijinshan.com%2Faccount%2Flogin',
	    'Host':'login.ijinshan.com',
	    'Connection':'Connection',
	    'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
	    'Accept-Encoding':'gzip, deflate',
	    'Accept':'*/*',
	    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0',
	    'X-Requested-With':'XMLHttpRequest'
	}
	str1 = str(time.time())
	url = 'https://login.ijinshan.com/glt?_lt='+str1
	r = urllib2.Request(url,headers=head)
	ckjar =  cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
	res = opener.open(r)
	#print res.info()
	print '------------'
	#登入 step 1
	loginurl = 'https://login.ijinshan.com/login'
	data = {
	    'cc':'',	
	    'cn':'e6c5aeba967a9e286b083044629c6091',
	    'pwd':'bf8fcf8f58466941d03091f73ff46e0c',
	    'rm':'1',
	    'service':'https://fireeye.ijinshan.com/account/login',
	    'user':''
	}
	data['user'] = user
	data = urllib.urlencode(data)
	res = opener.open(loginurl,data)
	res_json =  json.loads(res.read().strip())
	#登入 step 2 并获得最后登入成功后的cookie
	url = res_json['url']
	#获取session
	res = opener.open(url)
	return ckjar

head = {'Host':'fireeye.ijinshan.com',
                'Referer':'https://fireeye.ijinshan.com/',
                'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                'Connection':'Keep-Alive',
                'Cache-Control':'no-cache',
                'Accept-Language':'zh-CN',
                'Accept-Encoding':'gzip, deflate',
                'Accept':'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
                }
#r = urllib2.Request(post_url,headers=head)
# 需要动态修改的部分
limit = 0
apk_dir = 'apk'
for apk_file in os.listdir(apk_dir):
    #try:
    #if os.path.isfile(apk_file) == False:
	apk_start_time = time.time()
	if limit < len(users)*15:
		user = users[limit/15]
	else:
		break
	ckjar = doLogin(user)
	opener = register_openers()
	opener.add_handler(urllib2.HTTPCookieProcessor(ckjar))
	print '[ACTION]:Uploading ',(limit+1),' of ',len(os.listdir(apk_dir)),'User:',user,' ',(limit%15+1),' of 15.',
	uid = ''
	for i in range(32):
    		uid += hex(int((random.random()*16)))[-1::]
	print 'file:',apk_file,' size:',os.path.getsize('./'+apk_dir+'/'+apk_file)/1024,'KB'
	post_url = 'https://fireeye.ijinshan.com/upload?X-Progress-ID='+uid
	#head['Cookie'] ='__utma=214684160.8459916.1365512217.1365560804.1365563483.3; __utmz=214684160.1365512217.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JSESSIONID=aaaNXN3Eb8PTv42YdXX3t; __utmc=214684160; __utmb=214684160.14.10.1365563483'
	r = urllib2.Request(post_url,headers=head)
	apk_file = './'+apk_dir+'/'+apk_file
        datagen, headers = multipart_encode({"file": open(apk_file, "rb")})
        r.add_header('Content-Length',headers['Content-Length'])
        r.add_header('Content-Type',headers['Content-Type'])
        res = urllib2.urlopen(r,datagen)
        res =  res.read()
#	print '[RESULT]:',res,'---------------',
	limit += 1
	if len(res)>80:
       		print 'done in ',time.time()-apk_start_time,'s.'
		os.system('mv '+apk_file+' ./apk_bak')
		print 'To sleep 1s....'
		time.sleep(1)
	else:
		print 'Upload limit'
		limit = (limit/15+1)*15
		print '[DEBUG]',res
    #except:
print 'All Done total time:',time.time()-start
