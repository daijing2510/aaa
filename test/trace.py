'''
Created on 2015-12-10

@author: jingdai
'''
class wrapper:
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self,attrname):
        print 'Trace',attrname
        return getattr(self.wrapped,attrname)
    
if __name__=="__main__":
    x=wrapper([1,2,3])
    x.append(4)
    
    y=wrapper({"a":1,"b":2})
    y.keys()