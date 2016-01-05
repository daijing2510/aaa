'''
Created on 2015-11-3

@author: jingdai
'''
def intersect(seq1,seq2):
    res=[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1='spam'
s2='scam'
s3=intersect(s1,s2)
print s3

x=intersect([1,2,3],(2,3))
print x

