import urllib2
def download(url):
    req = urllib2.Request(url)
    r   = urllib2.urlopen(req)
    fname = r.info()['Content-MD5']
    fname = "./apk/"+fname
    fobj = open(fname,'wb')
    fobj.write(r.read())
    fobj.close()
print "begin"
fobj = open('b.txt')
line = fobj.readline()
while line:  
    download(line)
    print "downloading",line
    line = fobj.readline()
    
print "done"