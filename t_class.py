#!/usr/bin/python
#coding:utf-8
#---------------------------------------------------------
class Base(object):
    def __init__(self):
        self._age = 1
        print 'init'

    def test(self):
        print 'this is Base class'

    def __del__(self):
        print 'Parent Del'

    @property
    def age(self):
        print 'get age'
        return self._age

    @age.setter
    def age(self, value):
        print 'set age', value
        self._age = value

b = Base()
b.age = 3
print b.age

exit()




class Child(Base):
    count = 1
    def test(self):
        print 'this is Child class'

    def __del__(self):
        print 'Child Del'

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float),\
            'Value must be float'
        self.value = round(val, 2)




Child.count += 1
print Child.count

print '*'*20, 'Base Start', '*'*20
baseObj = Base()
baseObj.test()
print type(baseObj)
print '*'*20, 'Base End', '*'*20

print '*'*20, 'Child Start', '*'*20
child = Child()
child.test()
child.count += 1
print Child.count
print child.count
print '*'*20, 'Child End', '*'*20

