#!/usr/local/bin/python
#coding=utf-8
import GetBingPicUrl
import time
import UploadToQiniu
import os

def main():
    while 1:
        print 'Start!'

        try:
            BingPicUrl = GetBingPicUrl.GetBingPicUrl()
            GetBingPicUrl.DownloadUrl(BingPicUrl)
            print 1
        except AttributeError:
            print 'AttributeError error'
            continue

        CurPath = os.getcwd()
        CurTime = time.strftime('%Y%m%d',time.localtime(time.time()))
        FileName = str(CurTime)+'.jpg'
        path = CurPath + '\\' + FileName
        UploadToQiniu.UploadToQiniu(FileName,path)
        time.sleep(7200)

if __name__ == "__main__":
    main()