#c70e5e7fdf776b48de33312777c9e731
#coding=utf-8
import urllib2
import json
import xlrd
import sys
from xlutils.copy import copy
import time

start = time.time()
#设置系统编码
reload(sys)
sys.setdefaultencoding( "utf-8" )

rb = xlrd.open_workbook('jinshan.xls')
cur_row = rb.sheet_by_index(0).nrows
print 'current row:',cur_row
wb = copy(rb)
def doWrite(row,col,cont):
	global wb
	ws = wb.get_sheet(0)
	ws.write(row,col,cont.decode('utf-8'))

cookies = []
for line in open('cookie'):
	cookies.append(line.strip())

head = {'Host': 'fireeye.ijinshan.com',
                'Referer':'https://fireeye.ijinshan.com/',
                'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                'Connection':'Keep-Alive',
                'Cache-Control':'no-cache',
                'Accept-Language':'zh-CN',
                'Accept-Encoding':'gzip, deflate',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                #'Cookie':'__utma=214684160.447770654.1365401413.1365564436.1365575572.9; __utmz=214684160.1365401413.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=214684160; JSESSIONID=aaaRuM7aQ4JbGbN5xYX3t; __utmb=214684160.24.10.1365575572'
                'Cookie':''
}
num_cookie = len(cookies)
for i in range(num_cookie):
	head['Cookie'] = cookies[i]
	print '[Dealing]: ',i
	md5_list = []
	sha1_list = []
	
	#==========================获取列表==========================
	url = 'http://fireeye.ijinshan.com/secure/VsampleBehavStat?pageSize=10000'
	r = urllib2.Request(url,headers=head)
	print 'get list: ',
	res = urllib2.urlopen(r).read()
	res_json = json.loads(res)
	for i in res_json['store']:
		md5_list.append(i['md5'])
		sha1_list.append(i['sha1'])
	
	print ' done'
	#head['Cookie'] = '__utma=214684160.447770654.1365401413.1365564436.1365575572.9; __utmz=214684160.1365401413.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=214684160; JSESSIONID=aaaRuM7aQ4JbGbN5xYX3t; __utmb=214684160.6.10.1365575572'
	for i in range(len(md5_list)):
		print 'Dealing ',(i+1),' of ',len(md5_list)
		md5 = md5_list[i]
		sha1 = sha1_list[i]
		print '**********************************************************************'
		print 'dealing :',md5
		
	
		#==========================基本信息==========================
		url = 'http://fireeye.ijinshan.com/secure/isAnalysised?md5='+md5+'&sha1='+sha1
	
		r = urllib2.Request(url,headers=head)
		print 'basic info: ',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print res_json  
		#print json.dumps(res_json,ensure_ascii=False)
		App_name = ''
		App_version = ''
		try: 
			App_name =  res_json['store'][0]['appName']
		except:
			print 'appName Not Define'
		try:
			App_md5 =  res_json['store'][0]['md5']
			App_sha1 = res_json['store'][0]['sha1']
		except:
			continue
		try: 
			App_version = res_json['store'][0]['version']
		except:
			print 'version Not Define'
		cont = '文件名：'+App_name+'\nmd5='+App_md5+'\nsha1='+App_sha1+'\n版本：'+str(App_version)
		doWrite(cur_row,0,cont)
		print ' done'
	
		#==========================权限列表==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apkpermop'
		r = urllib2.Request(url,headers=head)
		print 'quanxian:',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
			for res in res_json['store']:
				isused = '已使用' if res['is_used'] == 1 else '未使用'
				cont += res['permDesc']+'  '+res['permName']+'  '+isused+'\n'
			#print cont
		doWrite(cur_row,3,cont)
		print 'done '
	
	
	
		#==========================广告相关==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apkadop'
		r = urllib2.Request(url,headers=head)
		print 'ad:',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
			for res in res_json['store']:
				cont += res['adName']+'('+res['adDesc']+')\n'
			#print cont
		doWrite(cur_row,5,cont)
		print 'done '
	
		#==========================危险行为==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apkbehva&blevel=1'
		r = urllib2.Request(url,headers=head)
		print 'dangerbehva :',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
				for res in res_json['store']:
					cont += '行为描述:'+res['behavDesc']+'\n附加信息:'+res['content']+'\n\n'
		doWrite(cur_row,1,cont)
		print 'done '
	
	
		#==========================其他行为==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apkbehva&blevel=2'
		r = urllib2.Request(url,headers=head)
		print 'other  :',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
			for res in res_json['store']:
				detail = ''
				try:
					for d1 in res['contents']:
						detail += d1+'\n'
					cont += '行为描述:'+res['behavDesc']+'\n详细:\n'+detail+'\n\n'
				except:
					pass	
			#print cont
		doWrite(cur_row,2,cont)
		print 'done '
	
	
	
		#==========================文件操作==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apkfileop'
		r = urllib2.Request(url,headers=head)
		print 'file :',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
			for i in res_json['store'][0]:
				for j in res_json['store'][0][i]:
					cont += i+'  '+j['tgtFile']+'\n'
		#print cont 
	
		doWrite(cur_row,6,cont)
		print 'done '
	
	
	
		#==========================启动方式==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apkstarttype'
		r = urllib2.Request(url,headers=head)
		print 'apk start :',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
			for i in res_json['store']:
				cont += '启动方式：'+i['starttypeDesc']+'\n启动对象：'+i['content']+'\n\n'
	
		#print cont 
	
		doWrite(cur_row,4,cont)
		print 'done '
	
	
		#==========================网络监控==========================
		url = 'http://fireeye.ijinshan.com/secure/apkReport?md5='+md5+'&sha1='+sha1+'&action=apknetop'
		r = urllib2.Request(url,headers=head)
		print 'net start :',
		res = urllib2.urlopen(r).read()
		res_json = json.loads(res)
		#print json.dumps(res_json,ensure_ascii=False)
		cont = ''
		if res_json['header'] == '800':
			for i in res_json['store']:
				method = '[POST]:' if i['opType']=='0' else '[GET]:'
				cont += method+str(i['tgtUrl'])+'\n'
		#print cont 
		doWrite(cur_row,7,cont)
		print 'done'
		cur_row += 1
	

wb.save('jinshan.xls')
end = time.time()
print 'Total time:',end-start,'s'
print 'SUCCESS'