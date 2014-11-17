#!/usr/local/bin/python
#coding=utf-8

import urllib

def qiniufetch(url,bucket,filename):
    """调用七牛的fetch API 将url的图片存储到七牛"""
    from base64 import urlsafe_b64encode as b64e
    from qiniu.auth import digest

    access_key = "qS-5BhmoJIM5WITHYwzooxlTiT70vWP9fyNXd_fT"
    secret_key = "5JOR1EiOXN-pbqvNoAf4v4YLmnSMB2rvqy13u3f5"

    encoded_url = b64e(url)
    dest_entry = "%s:%s" % (bucket, filename)
    encoded_entry = b64e(dest_entry.encode('utf-8'))

    api_host = "iovip.qbox.me"
    api_path = "/fetch/%s/to/%s" % (encoded_url, encoded_entry)

    mac = digest.Mac(access=access_key, secret=secret_key)
    client = digest.Client(host=api_host, mac=mac)

    ret, err = client.call(path=api_path)
    if err is not None:
        print "Fetch image file\"%s\" failed" % url
        print err
        return None
    else:
        print "Fetch \"%s\" to qiniu \"%s\" success!" % (url,dest_entry)
        return "http://%s.qiniudn.com/%s" % (bucket,urllib.quote(filename.encode('utf-8')))


if __name__ == "__main__":
    qiniufetch('http://s.cn.bing.net/az/hprichbg/rb/BlueTitFrost_ZH-CN13664641037_1366x768.jpg','jaccorot','aaa.jpg')