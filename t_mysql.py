import MySQLdb
 
try:
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='gif',port=3306)
    cur=conn.cursor()
    res = cur.execute('select * from t_gif')
    ret = []
    for i in cur.fetchall():
        ret.append(i)
    print ret
    # res = cur.fetchone()
    # print res
    # res = cur.fetchone()
    # print res
    # for i in res:
    # 	print i
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])