#!coding=utf-8 
import urllib2
import urllib
import time
import random

articleId = '694685841'
content = '我是NS测试部的黄佑榕，我的安全我做主'
refer = 'http://family.baidu.com/portal/newsDetail?articleId=683782630'
louceng = 150
cookie = 'BAIDUID=DC4F0E8FCCB21A52F91934FFEFCE106A:FG=1; BDUSS=ozaDlRU1VrVWFtaUt3fk5Sdzh1YXJNQmFTNkExVEwwMkVETVByN3V6QmJ6M0JUQVFBQUFBJCQAAAAAAAAAAAEAAACROWQ4YmRzZWMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFtCSVNbQklTTl; _ga=GA1.2.1971478939.1399461096; express.sid=s%3Ax7VN%2BIllno3oU0k8akzX7u%2BX.ntIepxzmgL5liZzpqHAukK9MoYrRUZe5TTwQszYptbc; Hm_lvt_e5c8f30b30415b1fc94d820ba9d4d08c=1402381659; Hm_lpvt_e5c8f30b30415b1fc94d820ba9d4d08c=1402384207; JSESSIONID=CCA50420E4A52DCB47C252BCE7ED49C3.worker6'


def getTime():
    return "[%s]" % time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime())

def getBDhttp(url, data=None):
    try:
        r = urllib2.Request(url)
        r.add_header('Host','family.baidu.com')
        r.add_header('Cookie',cookie)
        r.add_header('Referer',refer)
        r.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0')
        r.add_header('X-Requested-With','XMLHttpRequest')
        r.add_header('Connection', 'keep-alive')
        #r.add_header('Accept-Encoding', 'gzip, deflate')
        r.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.7,zh-TW;q=0.6,pt;q=0.4,es;q=0.3,th;q=0.1')
        r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        if data is not None:
            data = urllib.urlencode(data)
            # data = urllib2.urlopen(r,data) 
            res = urllib2.urlopen(r,data)
        else:
            res = urllib2.urlopen(r)
        return res.read()
    except:
        print getTime(),'http error'

def doPost(articleId = '', content = ''):
    try:
        api = 'http://family.baidu.com/portal/newsdetail/commentlist'
        data = {'articleId':articleId,'content':content,'replyToUser':'','replyToComment':''}
        res = getBDhttp(api, data)  
        print res.read(),
    except Exception, e:
        print 'POST ERROR!'
    print "POST OK"

def doCheck(articalId=''):
    try:
        api = 'http://family.baidu.com/portal/comments?articleId=%s' % articalId
        content = getBDhttp(api)
        index = content.find('楼')
        if index  > 0:
            tipContent = content[index-5:index]
            return int(tipContent[tipContent.find('>')+1:].strip())
    except Exception, e:
        print e
        print "connect error....",time.strftime('%H:%M:%S,%Y-%m-%d',time.localtime())
    return -1


while True:
    print 'lou：',louceng
    count = doCheck(articleId) 
    print "[",time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime()),']',' checking....,now:',str(count)
    if int(count) == (louceng-1) :
        doPost(articleId, content)
        break;
    elif count == -1:
        print "[",time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime()),']',' checking....,now: 0'
    if louceng - int(count) > 10:
        time.sleep(5+random.random()*10)
    if louceng - int(count) < 4:
        time.sleep(1)
    if 4 <= louceng - int(count) <= 10 :
        time.sleep(2+random.random()*5)
    
print 'success!'