#!coding:utf-8
import os
import subprocess
os.system('dir')
tmp = os.popen('dir').readlines()
print tmp

p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
