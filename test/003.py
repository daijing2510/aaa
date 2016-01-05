'''
Created on 2015-11-3

@author: jingdai
'''
def g(n):
    for i in range(n):
        yield i **2

for x in g(5):
    print x,':',
print '\n'

t=g(5)
print t.next()
print t.next()
print t.next()
print t.next()
print t.next()
print t.next()


