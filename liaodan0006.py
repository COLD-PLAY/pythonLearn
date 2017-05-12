# class Animal(object):
# 	def say(self):
# 		print('I am animal!')

# class Mammal(Animal):
# 	def say(self):
# 		print('I am mammal!')

# class Bird(Animal):
# 	def say(self):
# 		print('I am bird!')

# class Runnable(Animal):
# 	def move(self):
# 		print('I running...')

# class Flyable(Animal):
# 	def move(self):
# 		print('I flying...')

# class Dog(Mammal, Runnable):
# 	pass

# class Bat(Mammal, Flyable):
# 	pass

# def Introduce(Animal):
# 	Animal.say()
# 	Animal.move()

# doge = Dog()
# batt = Bat()
# Introduce(doge)
# print()
# Introduce(batt)

# 类中的一些特殊变量名
# __init__, __str__, __repr__, __iter__, __call__
# class Student(object):
# 	def __init__(self, name):
# 		self.name = name
# 	def __str__(self):
# 		return 'Student object(name: %s)' % self.name
# 	__repr__ = __str__	# 默认返回的是__repr__ 这个方法返回的值

# liaozhou = Student('liaozhou')
# print(liaozhou)

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration();
#         return self.a # 返回下一个值

#     def __getitem__(self, n):
#     	if isinstance(n, int):
#     		a, b = 1, 1
#     		for x in range(n):
#     			a, b = b, a + b
#     		return a
#         # 使得该对象实例可以进行切片操作
#     	if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
# for n in Fib():
# 	print(n)
# fib = Fib()

# for n in range(100):
# 	print(fib[n])

# print(list(range(100))[5:10])

# print(fib[5:100])

# class Student(object):
#     def __init__(self):
#         self.name = 'LiaoZhou'

#     def __getattr__(self, attr):
#         if attr == 'age':
#             return 19
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# liaozhou = Student()
# print(liaozhou.age)

class Chain(object):
    def __init__(self, path = 'GET '):
        self._path = path

    # def user(self, path):
    #     return Chain('%s/%s' % (self._path, path))

    def __getattr__(self, path):
        # if path == 'user':
        #     return lambda name: Chain('%s/%s' % (self._path, name))
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):


    def __str__(self):
        return self._path

    # def __call__(self, *args, **kwarge):
    #     return Chain('%s = %s' % (self._path, args))

    __repr__ = __str__


# print(Chain(), Chain()(), Chain()()())
# print()
# print(Chain().status)
# print()
# print(Chain().status.user('ksven'))
# print()
# print(Chain().status.user('ksven').timeline)

print('----------------------------------------')
print(Chain().status.user('coldplay').timeline.list)

# __call__ 方法就是当调用实例加上() 表示调用实例的__call__ 方法
class Student(object):
    def __init__(self, name = ''):
        self.name = name

    def __call__(self, move = ''):
        print('My name is %s. And %s' % (self.name, move))

    def __str__(self):
        return 'Student object: name = ' + self.name

liaozhou = Student('liaozhou')
liaozhou('i am fucking a dog!')

# callable() 方法判断对象是否是“可调用” 对象
print(callable(Student()), callable('str'), callable(Chain()))