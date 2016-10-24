import urllib2
import cookielib
import time
import urllib
import json

#实现自动登入
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
url = 'https://login.ijinshan.com/glt?_lt=1365748700338'
print url
r = urllib2.Request(url,headers=head)
ckjar =  cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
res = opener.open(r)
print res.info()
print '------------'
#登入 step 1
loginurl = 'https://login.ijinshan.com/login'
data = {
    'cc':'',	
    'cn':'e6c5aeba967a9e286b083044629c6091',
    'pwd':'bf8fcf8f58466941d03091f73ff46e0c',
    'rm':'1',
    'service':'https://fireeye.ijinshan.com/account/login',
    'user':'fireeye005@163.com'
}
data = urllib.urlencode(data)
res = opener.open(loginurl,data)
res_json =  json.loads(res.read().strip())
#登入 step 2 并获得最后登入成功后的cookie
url = res_json['url']
res = opener.open(url)
print ckjar._cookies
print '~'*10
print 'done'