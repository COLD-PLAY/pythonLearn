import logging
print('===================元类的理解&&自定义元类===================')

def upper_attrs(class_name, class_parents, class_attrs):
	attrs = ((name, value) for name, value in class_attrs.items() if not name.startswith('__'))
	uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
	return type(class_name, class_parents, uppercase_attrs)


class Foo1(object, metaclass = upper_attrs):
	bar = 'big'

print(hasattr(Foo1, 'bar'))	# 此时已经没有了小写的属性
# False
print(hasattr(Foo1, 'BAR'))
# True

# 下面是不同metaclass 类的定义方式
# class UpperAttrMetaClass(type):
# 	def __new__(upperattr_metaclass, class_name, class_parents, class_attrs):
# 		attrs = ((name, value) for name, value in class_attrs.items() if not name.startswith('__'))
# 		uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
# 		return type(class_name, class_parents, uppercase_attrs)

# class UpperAttrMetaClass(type):
# 	def __new__(upperattr_metaclass, class_name, class_parents, class_attrs):
# 		attrs = ((name, value) for name, value in class_attrs.items() if not name.startswith('__'))
# 		uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
# 		return type.__new__(upperattr_metaclass, class_name, class_parents, uppercase_attrs)

# class UpperAttrMetaClass(type):
# 	def __new__(cls, name, bases, dct):
# 		attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
# 		uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
# 		return type.__new__(cls, name, bases, uppercase_attrs)

print('=================将metaclass 定义为一个类==================')
class UpperAttrMetaClass(type):
	def __new__(cls, name, bases, dct):
		attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
		uppercase_attrs = dict((name.upper(), value) for name, value in attrs)		
		return super(UpperAttrMetaClass, cls).__new__(cls, name, bases, uppercase_attrs)

class Foo2(object, metaclass = UpperAttrMetaClass):
	bar = 'big'

print(hasattr(Foo2, 'bar'))	# 此时已经没有了小写的属性
# False
print(hasattr(Foo2, 'BAR'))
# True

print('============类对象的mro() 方法可以得到一个MRO 列表===========')
class a(object):
	pass

class b(a):
	pass

class c(a):
	pass

class d(b, c):
	pass

dd = d()
# 类的mro() 方法可以得到一个MRO 表，用于存储继承自什么类并最终集成到object
print(dd.__class__.mro())

print('==========================================================')
# for attr in d.__dict__.items():
# 	print(attr)
for attr in dir(d):
	print(attr)
# 打印出d 类的所有属性

print('==========================================================')
try:
	print('try...')
	r = 10 / 0
	print('result: ', r)
except ZeroDivisionError as e:
	print('except: ', e)
finally:
	print('finally...')
print('END')

print('==========================================================')
try:
	print('try...')
	r = 10 / int('a')
	print('result: ', r)
except ValueError as e:
	print('ValueError: ', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError: ', e)
finally:
	print('finally...')
print('END')

print('==========================================================')
try:
	print('try...')
	r = 10 / int('2')
	print('result: ', r)
except ValueError as e:
	print('ValueError: ', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError: ', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

print('==========================================================')
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
		# print(e)

main()
print('END')

print('==========================================================')
class FooError(ValueError):
	pass

def foo1(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

def bar1():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise

bar1()