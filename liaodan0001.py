# name = input('please input your name: ')
# print('hello,', name)
# print('i\'m learning\n\"Python\"')
# print(r'''line1
# line2
# line3''')
# print(True and True, False or True, not True)
# age = 12
# print(age)
# if age >= 18:
# 	print('True')
# else:
# 	print('False')

# a = 'abc'
# b = a
# a = 'xyz'
# print(b)

############################################# decode 和encode 字符编码函数
# nn = chr(25991) # '文'
# print('中文'.encode('utf-8'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(len('中文'.encode('utf-8')))
# print('Hello %s, your age is %d!' % ('liaozhou', 13))
# print('%d%%' % (3))
# print('我们将来计算小明成绩提升的百分点\n')
# s1 = input('请输入去年的成绩：')
# s1 = int(s1)
# s2 = input('请输入今年的成绩：')
# s2 = int(s2)
# improve = (s2-s1)/s1*100

# print('提高的百分点是 %.2f%%' % improve)

############################################# list 和tuple 的區別
# classMates = ['liaozhou', 'xiaoming', 'michael']
# print('原list：', classMates)
# classMates.append('zouguilin');
# print('添加\'zouguilin\'后list：', classMates)
# classMates.insert(4, 'liaoanle')
# print('添加\'liaoanle\'后list：', classMates)
# classMates.pop()
# print('pop后list：', classMates)

# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']
# print(len(s))

# p = ('liaozhou', 'zouguilin', 'zoubin')
# print(p[1])

############################################# if elif else 语句
# age = int(input('please input your age: '))
# if age >= 18:
# 	print('your age is:', age)
# 	print('adult')
# elif age > 6:
# 	print('your age is:', age)
# 	print('teenager')
# else :
# 	print('your age is:', age)
# 	print('kid')

############################################# for 循环和while 循环
# names = ['liaozhou', 'zouguilin', 'zoubin']
# for name in names:
# 	print(name)
# sum = 0
# for x in list(range(101)):
# 	sum += x
# print(sum)

# sum = 0
# n = 100
# while n > 0:
# 	sum += n
# 	n = n - 1
# print(sum)

# n = 0
# while n < 100:
# 	n = n + 1
# 	if n % 2 == 0:
# 		continue
# 	print(n)

############################################# dict 和set
# d = {'liaozhou': 100, 'zhoujielun': 99, 'linjunjie': 98}
# print(d['liaozhou'])
# d['laoda'] = 200
# print(d)
# d.pop('laoda')
# print('liaozhou' in d)
# print(d.get('zhoujielun'))
# s = set([3, 1, 2, 2, 3, 3, 4])
# s.add(5)
# print(s)
# a = [11, 12, 3, 4, 1]
# a.sort()
# print(a)
# string = 'liao zhou shi shuai ge'
# print(string.replace('l', 'L') + '\n' + string)

############################################# d函数
# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('bad operand type')
# 	if x > 0:
# 		return x
# 	else :
# 		return -x
# print(my_abs(-0))

# 函数返回多个值，其实就是返回一个tuple，返回时可以省略括号，所以看起来就像是返回了多个值
# import math
# def move(x, y, step, angle = 0):
# 	nx = x + step * math.cos(angle)
# 	ny = y + step * math.sin(angle)
# 	return nx, ny
# x, y = move(100, 100, 60, math.pi/6)
# print(x, y)

# import math
# def quadratic(a, b, c):
# 	d = b*b - 4*a*c
# 	if d < 0:
# 		return None
# 	else:
# 		x1 = (-b - math.sqrt(d))/a/2
# 		x2 = (-b + math.sqrt(d))/a/2
# 		return x1, x2
# print(quadratic(1, -5, 1))

# def power(x, n = 2):
# 	sum = 1
# 	while n > 0:
# 		sum = sum*x
# 		n = n - 1
# 	return sum

# print(power(12, 3))

# def add_End(L = None):
# 	if L is None:
# 		L = []
# 	L.append('END')
# 	return L

# print(add_End())
# print(add_End())

# def cal(numbers):
# 	sum = 0
# 	for x in numbers:
# 		sum += x*x
# 	return sum

# print(cal((1, 2, 3)))

# def cal_test(*numbers):
# 	sum = 0
# 	for x in numbers:
# 		sum += x*x
# 	return sum

# list = range(0, 1001)
# print(cal_test(*list))

# 递归函数的定义
# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n*fact(n - 1)

# print(fact(10))

# 尾递归对递归函数进行优化
# def  fact(num, product):
# 	if num == 1:
# 		return product
# 	return fact(num - 1, num*product)
# print(fact(100, 1))	

# Slice切片函数用法
# names = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(names[-2::-1])

# string = 'this is a string'
# print(string[-1::-1])

# 迭代（Iteration）for in，可以使用collections 中的isinstance Iterable来检验是否可以进行迭代
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
# 	print(key)

# for ch in 'ABC':
# 	print(ch)

# from collections import Iterable
# flag = isinstance('123', Iterable)
# print(flag)

# for x, y in [(1, 2), (3, 4), (4, 5)]:
# 	print(x, y)

# print([x*x for x in range(1, 11) if x%2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# print([d for d in os.listdir('/users/pc/desktop')])

# string = 'THIS IS THE STRING'
# print(string.lower().upper().lower())

# 迭代生成器generator
# g = (x*x for x in range(1, 11))
# for n in g:
# 	print(n)

# def fib(max):
# 	n, a, b = 0, 1, 1
# 	while n < max:
# 		yield a
# 		a, b = b, a + b
# 		n += 1
# 	return 'done'
# g = fib(6)
# while True:
# 	print(next(g))

# def triangles():
# 	list = [1]
# 	a = 0
# 	while True:
# 		i = 0
# 		_list = []
# 		while i <= a:
# 			if i == 0 or i == len(list):
# 				_list.append(1)
# 			else:
# 				_list.append(list[i - 1] + list[i])
# 			i = i + 1
# 		list = _list
# 		yield list
# 		a = a + 1
# n = 0
# for t in triangles():
# 	print(t)
# 	n = n + 1
# 	if n == 10:
# 		break

# def add(a, b, f):
# 	return f(a) + f(b)

# print(add(-11, -23, abs))

# r = map(abs, [-1, 23, -231, 4, 5])
# print(list(r))

# 匿名函数
# def f(x, y):
# 	return lambda: x*x + y*y

# fun = f(1, 2)
# print(fun())

def f(n):
	if n > 0:
		pass
	else:
		n = -n
	return n
