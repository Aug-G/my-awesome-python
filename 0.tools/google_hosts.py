#coding:utf-8
# google hosts
# 从定期更新的博客上抓取google host
# 目前支持windows 持续支持mac

import urllib
import platform


google_hosts_url = "http://www.360kb.com/kb/2_150.html"

windows_hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
linux_hosts_path = "/etc/hosts"

def get_html(url):
    page = urllib.urlopen(url)
    return page.read()

if __name__ == "__main__":
    os_name = platform.system()
    data = get_html(google_hosts_url)
    end_data = data[data.find("#google hosts"):data.rfind("#google hosts")].replace("&nbsp;", " ").replace("<br />","")
    path = ""
    if os_name == "Windows":
        path = windows_hosts_path
    elif os_name == "Linux":
        path = linux_hosts_path

    f = open(path,"w")
    f.write(end_data)
    f.close()

    print "ok"


