import os
import codecs
path = "E:\\lrc"
destfile = "E:\\all_py.txt"
print os.path.splitext(destfile)[1]
files = os.listdir(path)
w = codecs.open(destfile,"a",'utf-8')
try:
    for a in files:
        handle = codecs.open(path+"\\"+a,'r','utf-8')
        print "doing---"+a
        w.write(handle.read())
        handle.close()
except:
    pass

w.close()
print "done"
