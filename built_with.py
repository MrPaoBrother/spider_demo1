#-*-coding:utf8-*-
import builtwith
import whois
import urllib2
import re
import urlparse
#print builtwith.parse("http://www.baidu.com")

#print whois.whois('appspot.com')


def download(url , url_agent = 'wswp' ,num_retries = 2):
    print "DownLoad:",url
    try:
        headers = {'User-Agent':url_agent}
        request = urllib2.Request(url , headers=headers)
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "DownLoad Error:" , e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code <600:
                return download(url , num_retries - 1)
    return html
def downloadByProxy(url , url_agent , num_retries = 3, proxy = None):
    headers = {'User-Agent':url_agent}
    request = urllib2.Request(url , headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print "DownLoad:" , e.reason
        html = None
        if num_retries > 0:
            if hasattr(e , 'code') and 500 <= e < 600:
                html = downloadByProxy(url , url_agent , num_retries - 1 , proxy)
    return html
def crawl_sitemap(url):
    sitemap = download(url)
    print sitemap
    '''links = re.findall("<loc>(.*?)</loc>" , sitemap)
    for link in links:
        print link'''
def main():
    url = "http://www.caogen.com/bullent/1.html"
    #html = download(url)
    #print html
    #crawl_sitemap(url)
    url_agent = 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
    proxy = '27.151.11.211'
    caogen = downloadByProxy(url ,url_agent , 3 , proxy)
    print caogen
    print "========================end=========================="



main()

