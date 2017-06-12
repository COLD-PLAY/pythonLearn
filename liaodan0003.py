# -*- coding: utf-8 -*-
import types
from io import BytesIO
from io import StringIO
from types import MethodType
import time
# 获取当前系统时间
now = '%d-%d-%d' % time.localtime()[0:3]
print(now)

# 继承与多态
# class Animal(object):
# 	"""docstring for Animal"""
# 	def run(self):
# 		print('Animal is running...')
# 	def __len__(self):
# 		return 120
# 	name = 'Animal'

# class Dog(Animal):
# 	def run(self):
# 		print('Dog is running...')

# class Cat(Animal):
# 	def run(self):
# 		print('Cat is running...')

# class Tortoise(Animal):
# 	def run(self):
# 		print('Tortoise is running slowly...')

# def run_twice(Animal):	# 这个函数含有一个Animal 对象的参数
# 	Animal.run()
# 	Animal.run()
# 该函数其实就是多态的表现，我不需要去改变这个函数的内容
# 就可以实现很多继承自Animal 的对象或 Animal对象的不同表现

# animal = Animal()
# mimi = Cat()
# doge = Dog()
# guii = Tortoise()
# guii.name = 'guigui'
# del 可以删除类的属性
# del guii.name
# print(guii.name, doge.name)
# def set_noise(self, noise):
# 	self.noise = noise
# mimi.set_noise = MethodType(set_noise, mimi)
# mimi.set_noise('miao~')
# print(mimi.noise)

# 将set_noise 绑定到class 中，所有实例对象都可以使用
# Animal.set_noise = set_noise
# mimi.set_noise('miao~')
# print(mimi.noise)

# run_twice(mimi)
# run_twice(doge)
# run_twice(guii)

# print(type('str'), type(123))
# print(type(abs), type(mimi))
# print(type(lambda x:x) == types.LambdaType)
# print(type(x for x in range(10)) == types.GeneratorType)
# print(isinstance(mimi, Animal))

# print(isinstance([1, 2, 3], (list, tuple)), isinstance((1, 2, 3), (list, tuple)))
# print(dir('ABC'))
# print(len(mimi))	# len 函数就是返回对象的__len__ 属性

# str_func = dir('str')
# string = 'LiaoZhou'
# for value in str_func:
# 	fun = getattr(str, value)
# 	print(string.fun())

# print(getattr(str, 'upper')) # 得到str 中的'upper' 属性，是一个方法
# setattr(Animal, 'age', 19)	# 给动物这个类添加年龄属性 为19
# print(getattr(Animal, 'age'))	
# print(animal.age)
# print(doge.age)

# str_list = dir([1, 2, 3])
# for func in str_list:
# 	print(func)
# print(hasattr(str, 'split'))
# print(getattr(str, 'find', 404))

# 为对象添加属性
# setattr(mimi, 'liaozhou', lambda x, y: x*10 + y)
# print(mimi.liaozhou(5, 3))

# def readImage(fp):
# 	if hasattr(fp, 'read'):
# 		return fp.read()
# 	return None

# with open('dump.txt', 'rb') as fp:
# 	for line in fp.readline():
# 		print(line)

# 使用@property
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

LiaoZhou = Student()
LiaoZhou.score = 99
print(LiaoZhou.score)