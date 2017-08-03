import urllib
import urllib2

def md5(fname):
     import hashlib
     hash_md5 = hashlib.md5()
     with open(fname, "rb") as f:
         for chunk in iter(lambda: f.read(4096), b""):
             hash_md5.update(chunk)
     return hash_md5.hexdigest()

location = "/mount_point/odoo_"

try:
        query_args = { 'master_pwd':'pass','name':'database','backup_format':'zip' }
        encoded_args = urllib.urlencode(query_args)
        url = 'http://server:port/web/database/backup'
        f = urllib2.urlopen(url, encoded_args)

        file_name = f.info()['Content-Disposition'].split("filename*=UTF-8''")[1]
        location = "/location/odoo_"+file_name

        with open(location, "wb") as local_file:
                local_file.write(f.read())

        o = open(location, "r")
        print file_name, len(o.read()), md5(location)
        o.close()

#handle errors
except urllib2.HTTPError,e:
        print "HTTP Error:", e.code, url
except urllib2.URLError, e:
        print "URL Error:", e.reason, url
