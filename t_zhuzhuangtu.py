import MySQLdb
import datetime
import time

start = time.time()
show_time = datetime.datetime.now()+datetime.timedelta(days=-1)
show_time = show_time.strftime('%Y-%m-%d')

format_day = '%Y-%m-%d'
time_interval = 3600
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='res',port=3306)
cursor=conn.cursor()
result = {}
sql = "SELECT product,COUNT(1) AS num FROM res where DATE_FORMAT(access_time,'%s')='%s' GROUP BY product"%(format_day,show_time)
print sql
cursor.execute(sql)
res = cursor.fetchall()
print res
for i,j in res:
    result[i.lower()] = j
#print result
result['other'] = result['-']
result['time'] = show_time

sql = "insert into zhuzhuangtu values(0,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(show_time,result['iknow'],result['columbus'],result['mp3'],result['video'],result['image'],result['wiki'],result['forum'],result['hao123'],result['wenku'],result['wise'],result['holmes'],result['other'])
cursor.execute(sql)
conn.commit()
cursor.close()
end = time.time()-start
print 'Done in ',end/60000,' min.'
