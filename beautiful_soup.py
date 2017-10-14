#-*-coding:utf8-*-

from bs4 import BeautifulSoup
import urllib2
import urlparse 
'''broken_html = '<ul class="abc">\
<li>\
    lxm\
<li>\
    ccc\
</ul>'

soup = BeautifulSoup(broken_html , 'html.parser')

fixed_html = soup.prettify()

print fixed_html'''




def downloadByProxy(url , url_agent , retries = 3, proxy = None):
    headers = {'User-Agent':url_agent}
    request = urllib2.Request(url , headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params)) #加入proxy
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print "DownLoad:",e.reason #输出错误的原因
        html = None
        if retries > 0:
            if hasattr(e , 'code') and 500 <= e.code < 600:
                downloadByProxy(url , url_agent , retries - 1 , proxy)
    return html

def main():
    url = 'http://www.caogen.com/bullent/1.html'
    url_agent = 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
    proxy = '61.135.217.7'
    html = downloadByProxy(url , url_agent , 5)
    soup = BeautifulSoup(html)
    lis = soup.find_all(attrs={'class':'AC'})
    for li in lis:
        print li.text
    #li = soup.find(attrs={'class':'AC'})
    #a = li.text
    #print a

#==============运行入口===============
main()
#===================================