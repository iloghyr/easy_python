#coding:utf-8
import win32api
import time
import httplib2
from urllib import urlencode
import json

apiUrl = "http://cn.bter.com/json_svr/query/?u=1&c=105032"
header = {
	"Host": "cn.bter.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0",
	"Accept": "*/*",
	"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
	"Accept-Encoding": "gzip, deflate",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"X-Requested-With": "XMLHttpRequest",
	"Referer": "http://cn.bter.com/trade/ifc_cny",
	"Content-Length": "38",
	"Cookie": "lasturl=%2Ftrade%2Fifc_cny; captcha=c46126b773ab5298f2f3b37065c9a657",
	"Connection": "keep-alive",
	"Pragma": "no-cache",
	"Cache-Control": "no-cache",
}

def alert(msg=''):
	timeStr = time.strftime("%Y%m%d %H:%M:%S")
	print timeStr
	msg = timeStr+'\t'+ msg
	win32api.MessageBox(0, msg.encode("gbk"), u'提示', 4096)
data = {"type":"ask_bid_list_table","symbol":"ifc_cny"}
h = httplib2.Http()
resp, cont = h.request(uri=apiUrl,method="POST" , headers=header, body=urlencode(data))
print resp
print cont



	