import requests
from bs4 import BeautifulSoup
import os

headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}
##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url, headers = headers)
# print(start_html.text)
Soup = BeautifulSoup(start_html.text, 'lxml')
all_a = Soup.find('div', class_ = 'all').find_all('a')
i = 100
already = 120
for a in all_a:
	if already > 0:
		already -= 1
		continue
	if i < 1:
		break
	print('正在下载第' + str(121 - i), '组写真...')
	title = a.get_text()
	href = a['href']
	html = requests.get(href, headers = headers)
	html_Soup = BeautifulSoup(html.text, 'lxml')
	max_span = html_Soup.find('div', class_ = 'pagenavi').find_all('span')[-2].get_text()
	for page in range(1, int(max_span) + 1):
		print('    正在下载本写真的第' + str(page), '张照片...')
		page_url = href + '/' + str(page)
		img_html = requests.get(page_url, headers = headers)
		img_Soup = BeautifulSoup(img_html.text, 'lxml')
		img_url = img_Soup.find('div', class_ = 'main-image').find('img')['src']
		name = img_url[-9:-4]
		img = requests.get(img_url, headers = headers)
		f = open('D:/hide/' + name + '.jpg', 'ab')
		f.write(img.content)
		f.close()
	i -= 1