# _*_ coding=utf-8 _*_
import urllib2
import urllib
import time
import random

articleId = '676347775'
comment = '支持支持'
refer = 'http://family.baidu.com/core/index.jsp?chc=2110383119'
louceng = 800
cookie = 'BAIDUID=BCBA4E98FBA48088699C9F8DC9C2EEC7:FG=1; BAIDU_WISE_UID=bd_1355996712_805; Hm_lvt_e5c8f30b30415b1fc94d820ba9d4d08c=1363777708,1363843253,1363847202,1363931239; Hm_lvt_7a0fab0a2251879edfeb6f84c8a28964=1363165250,1363771226,1363847486; BDUSS=jZHcTVtbks1YnZRRXZFa2FlMVZhQU8tYTZSSjgtakppRy11UWlDalBWZUwwU1ZSQVFBQUFBJCQAAAAAAAAAAAEAAAAIwoYpaWxvZ2h5cgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAItE~lCLRP5QT; BDREFER=%7Burl%3A%22http%3A//news.baidu.com/%22%2Cword%3A%22%22%7D; JSESSIONID=9674AB7EF6A989D9FC3FE7C0FD057E8D.worker1; Hm_lpvt_e5c8f30b30415b1fc94d820ba9d4d08c=1363931307'

def doPost(articleId = '', refer = '' , comment = ''):
    try:
        global cookie
        r = urllib2.Request('http://family.baidu.com/comment/comment/addComment.do')
        r.add_header('Host','family.baidu.com')
        r.add_header('Cookie',cookie)
                                           
        r.add_header('Referer',refer)
        r.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
        r.add_header('X-Requested-With','XMLHttpRequest')
        data = {'articleId':articleId,'commentContent':comment,'from':'load','replyTo':'0'}
        data = urllib.urlencode(data)
        urllib2.urlopen(r,data)   
        #print res.read()
    except:
        print 'POST ERROR!'
    print "POST OK"

def doCheck(articalId='',refer=''):
    try:
        global cookie
        r = urllib2.Request('http://family.baidu.com/comment/comment/load.do?1=1')
        r.add_header('Host','family.baidu.com')
        r.add_header('Cookie',cookie)
        r.add_header('Referer',refer)
        r.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
        r.add_header('X-Requested-With','XMLHttpRequest')
        data = {'articleId':articalId,'path':'/评论/文章评论','requestType':'ajax','targetMenu':''}
        data = urllib.urlencode(data)
        res = urllib2.urlopen(r,data)
        content =  res.read()
        index = content.find('楼')
        if index  > 0:
            return content[index-5:index].strip()
    except:
        print "connect error....",time.strftime('%H:%M:%S,%Y-%m-%d',time.localtime())
    return -1
    

while True:
    count = doCheck(articleId,refer) 
    print "[",time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime()),']',' checking....,now:',str(count)
    if int(count) == (louceng-1) :
        #doPost(articleId, refer, comment)
        break;
    elif count == -1:
        print "[",time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime()),']',' checking....,now: 0'
    
    if louceng - int(count) > 10:
        time.sleep(5+random.random()*10)
    if louceng - int(count) < 4:
        time.sleep(1)
    if 4 <= louceng - int(count) <= 10 :
        time.sleep(5+random.random()*5)
    
    