#coding=utf-8
#---------------------------------------------------------
# Name:        谛听系统更新数据库
# Author:      loghyr
# Created:     09-08-2013
#------------------------------------------------------
import MySQLdb
import datetime
import time
start = time.time()
show_time = datetime.datetime.now()+datetime.timedelta(days=-1)
show_time = show_time.strftime('%Y-%m-%d')
result = {}
time_interval = 3600
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='res',port=3306)
cursor=conn.cursor()
type_sql = ['SQL','XSS','WEBDIR','COM','WEBSHELL']
product_list = ['columbus','iknow','video','image','wiki','mp3','forum','news','hao123','wenku','-','wise','holmes']
for product in product_list:
    print product
    
    for type in type_sql:
        temp = ''
        print ' '
        print type
        for i in range(24):
            print i,
            i = 24-i
            sql = "select count(type) from res where DATE_FORMAT(access_time,'%%Y-%%m-%%d')='%s' AND product='%s' and type='%s' AND (UNIX_TIMESTAMP('%s')-UNIX_TIMESTAMP(access_time)+86400)<%s AND (UNIX_TIMESTAMP('%s')-UNIX_TIMESTAMP(access_time)+86400)>%s"%(show_time[0:10],product,type,show_time,time_interval*i,show_time,time_interval*(i-1))
            #print sql
            cursor.execute(sql)
            res = cursor.fetchall()
            temp += str(res[0][0])+'|'
        result[type] = temp
    if product == '-':
        product = 'other'
    sql = "insert into  attack_tongji values(0,'%s','%s','%s','%s','%s','%s','%s')"%(show_time,product,result['SQL'],result['XSS'],result['WEBDIR'],result['COM'],result['WEBSHELL'])
    res = cursor.execute(sql)
    try:
        conn.commit()
    except Exception,e:
        print e
cursor.close()
end = time.time()-start
print 'Done in ',end/60000,' min.'
