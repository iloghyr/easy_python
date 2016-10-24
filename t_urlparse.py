#coding=utf-8
from urlparse import urlparse
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re



url = 'http://www.google.com.lyhttp://www.google.com.ly/search?tbo=d&filter=0&nfpr=1&source=hp&num=100&btnG=Search&q=inurl%3a.fr%2fpayment-and-terms-of-use.aspx+boast'
print url[0:7]
ret =  urlparse(url)
print ret
print ret[1]+ret[2]
#page_content = urlopen('http://news.baidu.com')
#beautiful_content = BeautifulSoup(page_content.read())
# for a_tag in beautiful_content.find_all('a'):
# 	print a_tag.get('href')
