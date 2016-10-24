#coding=utf-8
import md5

print md5.new("hehhe").hexdigest()


def md5(s):
    import hashlib
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

print md5('hehhe')


import os
url = "http://mars.baidu.com/logo.a.gif"
print os.path.splitext(url)