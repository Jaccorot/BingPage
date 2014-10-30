import qiniu.conf
import qiniu.rs
import qiniu.io
import os

def UploadToQiniu(uploadname, file_full_path):
    qiniu.conf.ACCESS_KEY = "qS-5BhmoJIM5WITHYwzooxlTiT70vWP9fyNXd_fT"
    qiniu.conf.SECRET_KEY = "5JOR1EiOXN-pbqvNoAf4v4YLmnSMB2rvqy13u3f5"
    bucket_name = "jaccorot"

    policy = qiniu.rs.PutPolicy(bucket_name)
    uptoken = policy.token()

    extra = qiniu.io.PutExtra()
    extra.mime_type = "image/jpeg"

    ret, err = qiniu.io.put_file(uptoken, uploadname, file_full_path, extra)
    if err is not None:
        print err
    file_url = "http://%s.qiniudn.com/%s" % (bucket_name, uploadname)
    print file_url


if __name__ == "__main__":
    CurPath = os.getcwd()
    path = CurPath + '\\' + '20141030.jpg'
    UploadToQiniu('20141030.jpg',path)