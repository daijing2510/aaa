'''
Created on 2015-12-10

@author: jingdai
'''
class Lister:
    def __repr__(self):
        return ("<instance of %s,address %s:\n %s") % (self.__class__.__name__,id(self),self.attrnames())
    
    def attrnames(self):
        result=''
        for attr in self.__dict__.keys():
            if attr[:2]=='__':
                result=result+"\tname %s=<built in>\n" %attr
            else:
                result=result+"\tname %s=%s\n" % (attr,self.__dict__[attr])
        return result
    
class super(Lister):
    def __init__(self):
        self.data1='spam'
        
class sub(super):
    def __init__(self):
        super.__init__(self)
        self.data2='egg'
        self.data3='apple'
        
if __name__=='__main__':
    X=super()
    print X
    print "******************"
    Y=sub()
    print Y