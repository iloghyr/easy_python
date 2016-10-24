#coding:utf-8

import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("t_configParser.cfg")
# 返回所有的section
s = cf.sections()
print 'section:', s

o = cf.options("db")
print 'options:', o

v = cf.items("db")
print 'db:', v

print '-'*60
#可以按照类型读取出来
db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")
print cf.get("db", "db_host")
cf.set("db", "db_detail", 'a')
cf.write(open("t_configParser.cfg", 'w'))