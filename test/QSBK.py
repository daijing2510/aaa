'''
Created on 2015-12-26

@author: jingdai
'''

# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
#�ٶ�����������
class BDTB:
 
    #��ʼ�����������ַ���Ƿ�ֻ��¥���Ĳ���
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
 
    #����ҳ�룬��ȡ��ҳ���ӵĴ���
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"���Ӱٶ�����ʧ��,����ԭ��",e.reason
                return None
 
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)