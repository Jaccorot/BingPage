#!/usr/local/bin/python
#coding=utf-8

import urllib2  
import urllib 
import re  
import time

 
def get_bing_pic_url(): 
    """
    通过正则表达式获取bing图片网址
    """ 
    myUrl = "http://cn.bing.com"  
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
    headers = { 'User-Agent' : user_agent } 
    req = urllib2.Request(myUrl, headers = headers) 
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()   
    unicodePage = myPage.decode("utf-8") 
    myItem = re.search('(http:\/\/s\.cn\.bing\.net.*?\d{1,4}x\d{1,4}\.jpg)',unicodePage,re.S)
    print 'file url =' + myItem.group(0)
    return myItem.group(0)

def download_url(url):
    """
    下载至本地
    """
    curtime = time.strftime('%Y%m%d',time.localtime(time.time()))
    filename = str(curtime)+'.jpg'
    print 'download file name :' + filename
    if url:
        urllib.urlretrieve(url,filename)


if __name__ == "__main__":
    get_bing_pic_url()