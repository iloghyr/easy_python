#coding:utf-8


import httplib2
#获取HTTP对象
h = httplib2.Http()
#发出同步请求，并获取内容
resp, content = h.request("http://www.baidu.com/")
print resp
print content