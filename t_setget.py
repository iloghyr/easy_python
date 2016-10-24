#!/usr/bin/python
#coding:utf-8


class Child(object):
    count = 1


    def test(self):
        print 'this is Child class'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        print 'set'


    def __del__(self):
        print 'Child Del'



a = Child()
a.age = 1
print a.age
a.age = 2
print a.age

