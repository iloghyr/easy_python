#coding:utf-8


import urllib2

try:
	response = urllib2.urlopen('http://www.baidu.com/img/bdlogo.png',timeout=1)
	print response.info()['Content-Length']
	print response.getcode()
except urllib2.HTTPError, e:
	print e.code
except urllib2.URLError, e:
	print e.__dict__


def sendHttp(api=None, data='',timeout=30):
	try:
		req 	= urllib2.Request(api)
		if data is not None:
			data 	= urllib.urlencode(data)
			ret   	= urllib2.urlopen(req, data, timeout).read()
		else:
			ret   	= urllib2.urlopen(req, timeout=timeout).read()
		return True, ret
	except Exception, e:
		LogHelper(LEVEL_ERROR, 'sendHttp%s' % str(e))
		return False, str(e)


def test():
	try:
		return "a"
		raise Exception("h")
	except Exception, e:
		return 'b'
	finally:
		return 'f'

print test()

