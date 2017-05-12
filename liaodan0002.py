# -*- coding: utf-8 -*-
from functools import reduce

# num = reduce(lambda x, y: 10*x + y, [1, 2, 3, 4, 5])
# print(num)
# string = input('please input a string: ')

# 自定义str 转int 函数只需要几行代码
# def char2num(s):
# 	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
# def str2int(s):
# 	return reduce(lambda x, y: x*10 + y, map(char2num, s))

# str = '1123123'
# print(str2int(str) + 123)

# def normalize(name):
# 	return name[0].upper() + name[1:].lower()

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def prod(L):
#     return reduce(lambda x, y: x*y, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 自定义str 转float 函数只需要几行代码
# def str2float(s):
# 	def char2num(s):
# 		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
# 	def str2int(s):
# 		return reduce(lambda x, y: x*10 + y, map(char2num, s))
# 	num = len(s) - s.rfind('.') - 1
# 	if num == len(s):
# 		num = 0
# 	s = s.replace('.', '')
# 	return str2int(s)/pow(10, num)

# print('str2float(\'123.456\') =', str2float('123.456'))

# def list2str(l):
# 	return reduce(lambda x, y: x + y, l)
# def is_blank(s):
# 	return s != ' '
# print(list2str(list(filter(is_blank, 'l ls  da  lf'))))

# 利用filter 高阶函数筛选出素数
# def _odd_iter():
# 	n = 1
# 	while True:
# 		n += 2
# 		yield n
# def _not_divisible(n):
# 	return lambda x: x%n > 0

# def primes():
# 	yield 2
# 	it = _odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(_not_divisible(n), it)

# for num in primes():
# 	if num < 10:
# 		print(num)
# 	else:
# 		break

# 利用filter 高阶函数筛选出回数
# def is_palindrome(n):
# 	str_n = str(n)
# 	return str_n == str_n[-1::-1]

# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

# 利用sorted 高阶函数对list 进行排序
# print(sorted([-34, -2, 4, 13, -22, 54], key = abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
# 	return t[0]
# def by_score(t):
# 	return t[1]

# # L2 = sorted(L, key = by_name)
# L2 = sorted(L, key = by_score)
# print(L2)

# 闭包，返回函数
# def get_f(*args):
# 	def f():
# 		sum = 0
# 		for x in args:
# 			sum += x
# 		return sum
# 	return f
# f = get_f(12, 3, 4)
# num = f()
# print(num)

# def get_f():
# 	def f(x):
# 		return lambda: x*x
# 	fs = []
# 	for i in range(1, 4):
# 		fs.append(f(i))
# 	return fs

# fs = get_f()
# f1, f2, f3 = fs
# print(f1(), f2(), f3())

# 装饰器decorator
# import functools
# def log(text):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kw):
# 			print('%s %s()' % (text, func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator

# @log('execute')
# def now():
# 	print('2017.2.20')
# now()
# import functools
# def log_begin(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('begin call')
# 		print('call %s()' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper

# def log_end(func):
# 	func()
# 	print('end call')
# @log_end
# @log_begin
# def now():
# 	print('i am the function')

# 偏函数 的定义
# def int2(str, base = 2):
# 	return int(str, base)
# import functools
# # int2 = functools.partial(int, base = 2)
# # print(int2('10001010101010010101'))
# sorted_byabs = functools.partial(sorted, key = abs)
# print(sorted_byabs([1, 3, -12, 213, -1234]))

# print([x*x for x in range(1, 11) if x%2 == 1])

# 使用模块
# import functools
# max2 = functools.partial(max, 10)
# print(max2(1, 2, 3))

# import liaodan0001
# print(liaodan0001.f(-11))

# 'a test module'
# __author__ = 'mixi shizi'

# import sys

# def test():
# 	args = sys.argv
# 	if len(args) == 1:
# 		print('Hello %s' % args[0])
# 	elif len(args) == 2:
# 		print('Hello %s' % args[1])
# 	else:
# 		print('Too Many Arguments!')

# if __name__ == '__main__':
# 	test()

# from PIL import Image
# im = Image.open('image.jpg')
# print(im.format, im.size, im.mode)
# im.thumbnail((200, 100))
# im.save('image.png', 'PNG') # 如果文件中包含该名字的文件 Python会直接替换

# import sys
# print(sys.path)

# 类&&实例
# class Student(object):
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score
# 	def print_score(self):
# 		print('%s: %s' % (self.name, self.score))

# lz = Student('liaozhou', 666)
# yt = Student('yangtao', 222)

# lz.print_score()
# yt.print_score()

# def print_score(stu):
# 	print('%s: %s' % (stu.name, stu.score))
# print_score(lz)
# print_score(yt)

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

stu_1 = Student('liaozhou', 666)
stu_1.set_score(17)
stu_1.print_score()