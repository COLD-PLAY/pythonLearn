# _*_ coding: utf-8 _*_

import re

# pattern = re.compile(r'hello')

# result = []
# result.append(re.match(pattern, 'hello'))
# result.append(re.match(pattern, 'helloo CQC!'))
# result.append(re.match(pattern, 'helo CQC!'))
# result.append(re.match(pattern, 'hello CQC!'))

# n = 1
# for ele in result:
# 	if ele:
# 		print(ele.group())
# 	else:
# 		print(str(n), 'fail!')
# 	n += 1

pattern = re.compile(r'.+\.jpg')

result = re.match(pattern, r"{url: '\/az\/hprichbg\/rb\/BlanchardSprings_ZH-CN10814394195_1920x1080.jpg'")

if result:
	print(result.group())
else:
	print('something wrong!')