'''
Created on 2015-12-10

@author: jingdai
'''
class Employee:
    def __init__(self,name,salary=0):
        self.name=name
        self.salary=salary
    def giveRaise(self,percent):
        self.salary=self.salary+(self.salary*percent)
    def work(self):
        print self.name,"does stuff"
    def __repr__(self):
        return "<Employee:name=%s,salary=%s>" % (self.name,self.salary)
    
class Chief(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print self.name,"makes food"
        
class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 40000) 
    def work(self):
        print self.name,"interfaces with customers"

class PizzaRobot(Chief):
    def __init__(self,name):
        Chief.__init__(self, name)       
    def work(self):
        print self.name,"makes Pizza"
        
if __name__=="__main__":
    Bob=PizzaRobot('Bob')
    print Bob
    Bob.work()
    Bob.giveRaise(0.2)
    print Bob;print
    
    
    for klass in Employee,Chief,Server,PizzaRobot:
        obj=klass(klass.__name__)
        obj.work()
    