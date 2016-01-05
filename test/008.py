'''
Created on 2015-11-18

@author: jingdai
'''
import time, sys
reps=1000
size=10000

def tester(func,*args):
    startTime=time.time();
    for i in range(reps):
        func(*args)
    elapsed=time.time()-startTime
    return elapsed

def forStatement():
    res=[]
    for x in range(size):
        res.append(abs(x))
        
def listComprehension():
    res=[abs(x) for x in range(size)]
    
def mapFunction():
    res=map((lambda x:abs(x)),range(size))
    
def generatorExpression():
    res=list(abs(x) for x in range(size))

print sys.version
tests=(forStatement,listComprehension,mapFunction,generatorExpression)
for testfunc in tests:
    print testfunc.__name__.ljust(20),'=>',tester(testfunc)