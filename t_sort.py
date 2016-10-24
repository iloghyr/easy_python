# _*_ coding=utf-8 _*_


al = [('a', 0.1), ('b', 0.3), ('c', 0.2)]

#method-1
al.sort(key=lambda x:x[1], reverse=True)
print al

#method-2
al.sort(lambda x,y:cmp(x[1],y[1]))
print al



tl = (1,2,4,3)
print list(tl)


di = {'a':1,'b':3,'c':2}
print [(k, di[k]) for k in sorted(di.keys())]
print di.items()
print sorted(di.items(), key=lambda x:(x[1]))
print sorted(di.items(), lambda x,y:cmp(x[1],y[1]))


# for v1 in (v for v in sorted(di.values())):
# 	print v1

# print sorted(di.values())


