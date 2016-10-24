#!/bin/evn python
#coding:utf-8

import os
import time
import signal


'''
    kill -HUP pid
'''


def hander_signal_hup(signum, frame):
    print 'receive hup signal'
    print signal, frame


def hander_signal_usr1(signum, frame):
    print 'receive usr1 signal'


def init_signal():
    signal.signal(signal.SIGHUP, hander_signal_hup)
    signal.signal(signal.SIGUSR1, hander_signal_usr1)


if __name__ == '__main__':
    init_signal()
    while True:
        print 'pid', os.getpid()
        time.sleep(10)