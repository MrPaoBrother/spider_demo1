#-*-coding:utf8-*-

import urllib
import urllib2

#直接使用urlopen(url , data , timeout)
#response = urllib2.urlopen("http://www.baidu.com")  
#print response.read()

#============构造Request==================

'''request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()'''

#Post Get方法

'''post_url = "http://localhost:3000/signin"
values = {"username":"admin" , "password":"123456"}
data = urllib.urlencode(values)
request = urllib2.Request(post_url)
response = urllib2.urlopen(request)
print "==============下面是返回的数据===============\n"
print response.read()'''

#GET
'''post_url = "http://localhost:3000/signin"
values = {"username":"admin" , "password":"123456"}
data = urllib.urlencode(values)
get_url = post_url + "?" + data
request = urllib2.Request(get_url)
response = urllib2.urlopen(request)
print "==============下面是返回的数据===============\n"
print response.read()'''

#设置header

'''url = "http://localhost:3000/"
values = {
    "username":"admin" , 
    "password":"123456"
}
data = urllib.urlencode(values)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' , user_agent}
request = urllib2.Request(url , data , headers=headers)
response = urllib2.urlopen(request)

print response.read()'''


















