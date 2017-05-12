import requests
from bs4 import BeautifulSoup
import os
from lxml import html

headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}
payload = {
	
}
url = 'http://www.uestc.edu.cn/'
html = requests.get(url, headers = headers)
Soup = BeautifulSoup(html.text, 'lxml')

all_link = Soup.find('div', class_ = 'slides-wrapper').find_all('img')
print(all_link)

i = 1
for link in all_link:
	print('正在下载第' + str(i) + ' 张学校官网图片...')
	img_url = 'http://www.uestc.edu.cn/' + link['src']
	name = str(i)
	img = requests.get(img_url, headers = headers)
	with open('C:/Users/pc/Desktop/' + name + '.jpg', 'ab') as f:
		f.write(img.content)
	i += 1
