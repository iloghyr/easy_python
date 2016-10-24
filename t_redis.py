#coding:utf-8
import redis
#客户端 : redis-py-master
#-----------1------------
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)
r.set('foo', 'hello')
#r.rpush('mylist', 'one')
#print r.get('foo')
#print r.rpop('mylist')
print r.get('foo')
#r.flushdb()
exit(0)


#------------2-----------
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
#r.set('one', 'first1',ex=100)
r.setnx('one', 'first1')
r.set('two', 'second')
r.set('int', 'second')

r.expire('one', 10)
print r.delete('one')
print r.get('one')
print r.get('two')

print r.keys()

print r.exists('one')
print r.ttl('one')

print r.client_list()
