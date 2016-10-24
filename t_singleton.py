#coding:utf-8

class Singleton(object):
	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton,cls).__new__(cls,*args,**kw)
		return cls._instance

class MyClass(Singleton):
	"""docstring for ClassName"""
	a = 1
print dir(Singleton)
print dir(MyClass)
a = MyClass()
b = MyClass()
print dir(MyClass)
