#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import threading
import re
import md5
import time
import sys
from urlparse import urlparse
from bs4 import BeautifulSoup


LIST_MUTEX_LOCK = threading.Lock()
SET_MUTEX_LOCK = threading.Lock()
IMG_HASH_SET = set()
IMG_DIR = './imgs-4493/'
DOWNLOAD_COUNT = 0


def getHttpResponse(url, timeout=15):
	try:
		r = urllib2.Request(url)
		r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36')
		res = urllib2.urlopen(r, timeout=15)
		return res
	except Exception,e:
		print e
		return None

def download(url):
	try:
		global DOWNLOAD_COUNT
		global IMG_HASH_SET
		print '[download]:', url
		res = getHttpResponse(url)
		fileSize = res.info()["Content-Length"]	
		if(int(fileSize) < 1024 * 50):
			print '\t[fileSize too small]:only ',int(fileSize)/1024,' kb'
			return
		content = res.read()
		filename = md5.new(content).hexdigest()
		if(filename in IMG_HASH_SET):
			print '\t[already exists]'
		else:
			IMG_HASH_SET.add(filename)
		file(IMG_DIR+filename+url[url.rfind('.'):], 'wb').write(content)
		DOWNLOAD_COUNT += 1
		print '','*'*10,'[success]:'+str(DOWNLOAD_COUNT),'*'*10
	except Exception, e:
		print '\t[error]:',e


class Crawler(object):
	def __init__(self, root, maxImgNum=1000, maxDepth=1500000):
		self.need_crawl_url = set([root])
		self.crawled_url = set()
		self.crawled_img = set()
		self.urlExclude = re.compile(r'javascript:', re.I)
		self.imgAccept  = re.compile(r'.*\.(jpg|png)$', re.I)
		self.crawl_depth_count = 0
		self.crawl_img_count = 0
		self.img_max_num = maxImgNum
		self.url_max_depth = maxDepth


	def _addCrawledImg(self, img):
		self.crawled_img.add(img)

	def _addCrawledUrl(self, url):
		self.crawled_url.add(url)

	def getCrawledImg(self):
		return self.crawled_img

	def getCrawledUrl(self):
		return self.crawled_url

	def crawl(self):
		flag = True
		while flag:
			try:
				crawling_url = self.need_crawl_url.pop()
				print '[crawling]:\t',crawling_url
				print '[need_crawl_url:%s, crawled_url:%s ,crawled_img:%s,download_img:%s]' % (len(self.need_crawl_url), self.crawl_depth_count, self.crawl_img_count, DOWNLOAD_COUNT)
				try:
					res = getHttpResponse(crawling_url)
					page_content = res.read()
					parsed_url = urlparse(crawling_url)
				except Exception, e:
					print e
					continue
					
					#print e
				self.crawl_depth_count += 1
				#获取到静态网页源代码，bs分析
				soup = BeautifulSoup(page_content)
				#取到所有的超链接
				for a_tag in soup.findAll('a'):
					link = a_tag.get('href')
					if link:
						if link.strip() == '/':
							continue
						if link.startswith('/'):
							link= 'http://%s%s' % (parsed_url[1], link) 
						elif link.find(parsed_url[1]) == -1:
							continue
						elif self.urlExclude.match(link):
							continue
						#print '[href]:', link
						self.need_crawl_url.add(link)
				#取到静态源码图片地址
				for img_tag in soup.findAll('img'):
					link = img_tag.get('src')
					if link:
						if not self.imgAccept.match(link):
							continue
						if link.startswith('/'):
							link= 'http://%s%s' % (parsed_url[1], link) 
						elif self.urlExclude.match(link):
							continue
						#print '[img]:', link
						if link not in self.crawled_img:
							self.crawl_img_count += 1
							self._addCrawledImg(link)
							download(link)

				if DOWNLOAD_COUNT > self.img_max_num or self.crawl_depth_count > self.url_max_depth:
					return
				self._addCrawledUrl(crawling_url)
				time.sleep(1)
				if(len(self.need_crawl_url) == 0):
					flag = False
			except Exception, e:
				print e


if __name__ == '__main__':
	if len(sys.argv) == 5:
		url = sys.argv[1]
		IMG_DIR = sys.argv[2]
		if IMG_DIR[-1] != '/':
			IMG_DIR += '/'
		maxImgNum = int(sys.argv[3])
		maxDepth = int(sys.argv[4])
		crawler = Crawler(url, maxImgNum, maxDepth)
		crawler.crawl()
	else:
		print 'missing args: url dir [maxImgNum maxDepth]'


