#coding:utf-8
# google hosts
# 从定期更新的博客上抓取google host
# 目前支持windows 持续支持mac

import urllib
import re

google_hosts_url = "http://www.360kb.com/kb/2_150.html"

windows_hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

def get_html(url):
    page = urllib.urlopen(url)
    return page.read()

if __name__ == "__main__":

    data = get_html(google_hosts_url)
    end_data = data[data.find("#google hosts"):data.rfind("#google hosts")].replace("&nbsp;", " ").replace("<br />","")
    f = open(windows_hosts_path,"w")
    f.write(end_data)
    f.close()

    print "ok"


