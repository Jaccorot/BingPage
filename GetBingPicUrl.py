#!/usr/local/bin/python
#coding=utf-8

import urllib2   
import re  

 
def GetBingPicUrl():  
    myUrl = "http://cn.bing.com"  
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
    headers = { 'User-Agent' : user_agent } 
    req = urllib2.Request(myUrl, headers = headers) 
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()   
    unicodePage = myPage.decode("utf-8") 
    myItem = re.search('(http:\/\/s\.cn\.bing\.net.*?1366x768\.jpg)',unicodePage,re.S)
    print myItem.group(0)
    return myItem.group(0)
if __name__ == "__main__":
    GetBingPicUrl()