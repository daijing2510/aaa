'''
Created on 2015-11-18

@author: jingdai
'''
print (x**2 for x in range(5))
print '\n'

G=(x**2 for x in range(5))
print G.next()
print G.next()
print G.next()
print G.next()
print G.next()
print '\n'

for i in (x**2 for x in range(5)):
    print '%s,%s'%(i,i/2.0)
print '\n'