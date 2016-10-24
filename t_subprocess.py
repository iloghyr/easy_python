#coding:utf-8

import subprocess
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
pp = subprocess.Popen('ls -al', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while pp.poll() is None:
	print pp.poll()
	time.sleep(2)
stdout, stderr = pp.communicate()
print stdout, stderr
print pp.poll()
out = subprocess.call("ls -l", shell=True)
