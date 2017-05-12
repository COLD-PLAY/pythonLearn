import urllib.request
import time
import re

urlpath = 'http://cn.bing.com/'
regex = '{url: "(.*jpg)"'
local = 'D:\\bing_wallpapers\\%s.jpg' % ('%d-%d-%d' % time.localtime()[0:3])
# local = 'bing.jpg'

def callbackfunc(blocknum, blocksize, totalsize):
	'''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
	persent = 100.0 * blocknum * blocksize / totalsize
	if persent > 100:
		persent = 100
	print('下载进度: %f%%' % persent)

try:
	html = urllib.request.urlopen(urlpath)
	print(html.getcode())
	img_url = 'http://cn.bing.com' + re.findall(regex, html.read().decode('utf-8'))[0]
except Exception as e:
	print(e)
else:
	print('正在从' + img_url, '悄悄下载bing 壁纸')
	urllib.request.urlretrieve(img_url, local, callbackfunc)
	print('下载成功！')