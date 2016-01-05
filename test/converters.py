'''
Created on 2015-12-10

@author: jingdai
'''
from streams import Processor

class Uppercase(Processor):
    def converter(self,data):
        return data.upper()

if __name__=="__main__":
    import sys
#    Uppercase(open('spam.txt'),sys.stdout).process()
    Uppercase(open('spam.txt'),open('spamup.txt','w')).process()