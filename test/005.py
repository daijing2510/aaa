'''
Created on 2015-11-18

@author: jingdai
'''
def squares(n):
    res=[]
    for i in range(n):res.append(i**2)
    return res
for x in squares(5):print x,':',
print '\n'



for x in [n**2 for n in range(5)]:
          print x,':',
print '\n'



for x in map((lambda x:x**2),range(5)):
    print x,':',
print '\n'