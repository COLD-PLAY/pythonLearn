from collections import namedtuple, deque
from collections import defaultdict, OrderedDict
from collections import Counter
import base64, struct, hashlib
import itertools

print('=================collections================')

Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['x', 'y', 'r'])

p = Point(1, 2)
print('p:', p.x, p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])

d = dict(a = 1, b = 2, c = 3)
print(d)
od = OrderedDict(a = 1, b = 2, c = 3)

class LastUpdateOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdateOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print('remove', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)

c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print(c)

print('===================base64===================')

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# 'A'~'Z' 'a'~'z' '0'~'9' '+' '/' 标准的Base64 编码
# 'A'~'Z' 'a'~'z' '0'~'9' '-' '_' url safe 的Base64 编码

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

print('=====================test===================')
# -*- coding: utf-8 -*-

def safe_base64_decode(s):
	if len(s)%4:
		for i in range(4 - len(s)%4):
			s = s + b'='
	return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

print('=====================struct=================')
print(struct.pack('>I', 10240099))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))

print('====================hashlib=================')
# 可以分块计算
md5 = hashlib.md5()
print('how to use **** in python hashlib?')
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('this is md5:', md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print('this is sha1:', sha1.hexdigest())

print('=====================test===================')
db = {}
def get_md5(string):
	md5 = hashlib.md5()
	md5.update(string.encode('utf-8'))
	return md5.hexdigest()

def register(username, password):
	db[username] = get_md5(password + username + 'the-salt')

register('mixishizi', '123456789')
print(db)

print('====================itertools=================')

natuals = itertools.count(1)
# for n in natuals:
# 	print(n)

cs = itertools.cycle('ABC')
# for c in cs:
# 	print(c)

ns = itertools.repeat('A', 3)
# for n in ns:
# 	print(n)

na = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(na))

for c in itertools.chain('ABC', 'XYZ'):
	print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
