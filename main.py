#!/usr/local/bin/python
#coding=utf-8
import get_bing_pic_url
import time
import upload_to_qiniu
import os

def main():
    while 1:
        print 'Start!'

        try:
            bing_pic_url = get_bing_pic_url.get_bing_pic_url()
            # get_bing_pic_url.download_url(bing_pic_url)
            print 1
        except AttributeError:
            print 'AttributeError error'
            continue

        # CurPath = os.getcwd()
        cur_time = time.strftime('%Y%m%d',time.localtime(time.time()))
        file_name = str(cur_time)+'.jpg'
        # path = CurPath + '\\' + FileName
        judge = upload_to_qiniu.qiniufetch(bing_pic_url,'jaccorot',file_name)
        print 'judge:'+judge
        if judge:
            time.sleep(7200)
        else:
            continue

if __name__ == "__main__":
    main()