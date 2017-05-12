import urllib
import http.cookiejar
import urllib.request

# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://i.baidu.com/')
# cookie.save(ignore_discard = True, ignore_expires = True)
# print('OK')

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)

# response = opener.open('http://i.baidu.com/')
# for item in cookie:
# 	print('Name = ' + item.name)
# 	print('Value = ' + item.value)

# response 对象是一个HttpResponse 对象
# headers = {
# 	'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
# 	'Referer' : 'https://i.baidu.com/'
# }
# values = {'username': '18280278028', 'password': 'liaozhou1998'}
# data = urllib.parse.urlencode(values)
# binary_data = data.encode('ascii')

# url = 'https://www.zhihu.com/#signin'
# # 先请求
# try:
# 	request = urllib.request.Request(url, binary_data, headers)
# 	response = urllib.request.urlopen(request)
# 	print(response.read().decode('utf-8'))
# except urllib.request.HTTPError as e:
# 	print(e.code)
# except urllib.request.URLError as e:
# 	print(e.reason)
# else:
# 	print('OK')

# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)

# response = opener.open('http://i.baidu.com/')
# cookie.save(ignore_discard = True, ignore_expires = True)
# print('finished download cookie')

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
postdata = urllib.parse.urlencode({
		'username' : '2015060103012',
		'password' : '101387'
	}).encode('ascii')
loginUrl = 'http://idas.uestc.edu.cn/authserver/login'

request = urllib.request.Request(loginUrl, data = postdata)
response = opener.open(request)

cookie.save(ignore_discard = True, ignore_expires = True)

gradeUrl = 'http://portal.uestc.edu.cn/?.pn=p346'
request = urllib.request.Request(gradeUrl)
response = opener.open(request)

print(response.read().decode('utf-8'))
# try:
# 	with open('mail.qq.com.txt', 'wb') as fs:
# 		fs.write(response.read())
# except IOError as e:
# 	print(e)
# else:
# 	print('download successfully!')