#!/usr/local/bin/python
#coding=utf-8
import get_bing_pic_url
import time
import upload_to_qiniu
import os

def main():
    """
    先实现获取图片地址，再传送至七牛云存储
    """
    while 1:
        print 'Start!'

        try:
            bing_pic_url = get_bing_pic_url.get_bing_pic_url()
            print 1
        except AttributeError:
            print 'AttributeError error'
            continue

        cur_time = time.strftime('%Y%m%d',time.localtime(time.time()))
        file_name = str(cur_time)+'.jpg'
        judge = upload_to_qiniu.qiniufetch(bing_pic_url,'jaccorot',file_name)
        if judge:
            print 'Mission Completed'
            return 'Mission Completed'
        else:
            continue

if __name__ == "__main__":
    main()