#coding:utf-8
import win32api
import time
import httplib2
from urllib import urlencode
import json
import random
import sys
import winsound


symbol = ['ltc_cny','ifc_cny']


apiUrl = "http://cn.bter.com/json_svr/query/?u=1&c=303877"
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

def alert(msg='', level=None):
	timeStr = time.strftime("%Y%m%d %H:%M:%S")
	print timeStr
	msg 	= timeStr+'\t'+ str(msg)
	winsound.PlaySound('alert',winsound.SND_ASYNC)
	win32api.MessageBox(0, msg.encode("gbk"), level.encode("gbk"), 4096)

def getRate(count,symbol):
	try:
		print '['+time.strftime("%Y%m%d %H:%M:%S")+']',count,':',
		data = {"type":"ask_bid_list_table","symbol":symbol}
		h 	 = httplib2.Http()
		resp, cont 	= h.request(uri=apiUrl,method="POST" , headers=header, body=urlencode(data))
		conObj 		= json.loads(cont)
		result 		= conObj['result']
		rate_sell 	= conObj['bid_rate0']
		rate_buy  	= conObj['ask_rate0']
		#print result
		print u'卖出:'.encode('gbk'),rate_sell,u'买入'.encode('gbk'),rate_buy
		#print rate_buy
		return result, float(rate_sell), float(rate_buy)
	except:
		return False, None, None

rate_sell_hole = 0.0000

def main(type, low , high):
	count = 1
	while True:
		result, rate_sell, rate_buy = getRate(count, symbol[int(type)])
		if result and rate_sell > high:
			alert(rate_sell,"HIGH")
		if result and low > rate_sell:
			alert(rate_sell,"LOW")
		count += 1
		time.sleep(random.random()*5+5)
if __name__ == '__main__':

	if len(sys.argv) == 4:
		main(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
	else:
		print 'input low and high value: python %s 1 0.00055 0.00062\n1:ifc,0:ltc' % __file__
		exit(1)




	