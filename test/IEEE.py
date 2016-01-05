'''
Created on 2015-12-26

@author: jingdai
'''

import urllib2
import urllib


import cookielib
class IEEE:
    def __init__(self,keytext):
#        self.searchURL='http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText='+keytext
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        
    def getpage(self,pagenumber):
        for i in range(1,pagenumber):
            self.searchURL='http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText='+keytext+'&pageNumber='+str(i)+'&newsearch=true&searchField=Search_All'
            request  = urllib2.Request(url = self.searchURL)
            result = self.opener.open(request)
        return result
        
    def getitems(self):
        
        
if __name__=='__main__':
    keytext=raw_input('Please input your search keytext:')
    IEEE('antenna').getpage()