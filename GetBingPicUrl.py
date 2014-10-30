#!/usr/local/bin/python
#coding=utf-8

import urllib2  
import urllib 
import re  
import time

 
def GetBingPicUrl():  
    myUrl = "http://cn.bing.com"  
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
    headers = { 'User-Agent' : user_agent } 
    req = urllib2.Request(myUrl, headers = headers) 
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()   
    unicodePage = myPage.decode("utf-8") 
    myItem = re.search('(http:\/\/s\.cn\.bing\.net.*?1366x768\.jpg)',unicodePage,re.S)
    print 'file url =' + myItem.group(0)
    return myItem.group(0)

def DownloadUrl(url):
    CurTime = time.strftime('%Y%m%d',time.localtime(time.time()))
    FileName = str(CurTime)+'.jpg'
    print 'download file name :' + FileName
    if url:
        urllib.urlretrieve(url,FileName)


if __name__ == "__main__":
    GetBingPicUrl()