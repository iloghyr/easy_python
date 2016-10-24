#encoding=utf-8
##print "s:%s,%d"%("hello world",len("hello"))
##dict = {"a":"apple","b":"banana","o":"orange"}
##for k in dict:
##    print "dict[%s]:"%k,dict[k]
##
##dict = {"a":"apple","b":"banana","o":"orange"}
##for k in dict.values():
##    print k
##print 'heh'
##d1 = {'a':'apple','b':'banana'}
##d2 = {'a':'cc'}
##d1.update(d2)
##for (k,v) in d1.items():
##    print k,d1[k]
##for k, v in d1.keys(),d1.values():
##    print k,':',v
##print zip((1,2,3),['a','b','c'])
#def fun(**args):
#    print args
#fun(1,2,3,4)

# func = lambda x,y:x+x
# print func(1,2)

# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# str1 = 'a拦截d信'
# print str1.find('拦截短信')


import hashlib

f = open('a.apk','rb')
sh = hashlib.sha256()
sh.update(f.read())
print sh.hexdigest()

di1 = {'a':1}
di2 = {'b':2}
di1.update(di2)
print di1