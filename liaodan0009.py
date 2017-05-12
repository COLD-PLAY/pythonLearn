import pdb
import logging
logging.basicConfig(level = logging.INFO)
import unittest
import re

print('=========================文档测试==========================')
# def foo(s):
# 	n = int(s)
# 	assert n != 0, 'n is zero!'
# 	return 10 / n

# def main():
# 	foo('0')

# s = '0'
# pdb.set_trace()
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

class Dict(dict):
	'''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError as e:
			raise AttributeError("'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value


if __name__ == '__main__':
	import doctest
	doctest.testmod()

# d = Dict(name = 'liaozhou', age = '19')
# print(d.name)
# print(isinstance(d, dict))
# print(d.name)

# nothing
# m = re.search('(?<=abc)def', 'abcdef adef')
# print(dir(m))
# print(m.group(0))

print('==========================================================')
def fact(n):
	'''
	Function fact to get the fact of number n.
	# 注意： >>> 后面有一个空格
	
	>>> fact(1)
	1
	>>> fact(10)
	3628800
	>>> f = fact(0)
	Traceback (most recent call last):
		...
	ValueError
	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	return n * fact(n - 1)

# f = fact(10)
# print(f)
# f = fact(0)

if __name__ == '__main__':
	import doctest
	doctest.testmod()