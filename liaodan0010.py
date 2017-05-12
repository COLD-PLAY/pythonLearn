import threading
import random, time, queue
from multiprocessing.managers import BaseManager
import sys, re
from datetime import datetime, timedelta

print('================ThreadLocal================')
# global_dict = {}

# class Student():
# 	def __init__(self, name):
# 		self.name = name

# def std_thread(name):
# 	std = Student(name)
# 	# 把std 放到全局变量global_dict 中：
# 	global_dict[threading.current_thread()] = std
# 	do_task_1()
# 	do_task_2()

# def do_task_1():
# 	std = global_dict[threading.current_thread()]

# def do_task_2():
# 	std = global_dict[threading.current_thread()]

# 创建全局ThreadLocal 对象：
local_school = threading.local()

def process_student():
	# 获取当前线程关联的student：
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	# 绑定ThreadLocal 的student
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

print('=================分布式进程================')
# task_queue = queue.Queue()
# result_queue = queue.Queue()

# class QueueManager(BaseManager):
# 	pass

# QueueManager.register('get_task_queue', callable = lambda: task_queue)
# QueueManager.register('get_result_queue', callable = lambda: result_queue)

# manager = QueueManager(address = ('', 5000), authkey = b'abc')

# manager.start()

# task = manager.get_task_queue()
# result = manager.get_result_queue()

# for i in range(10):
# 	n = random.randint(0, 10000)
# 	print('Put task %d...' % n)
# 	task.put(n)

# print('Try get results...')
# for i in range(10):
# 	r = result.get(timeout = 10)
# 	print('Result: %s' % r)

# manager.shutdown()
# print('master exit.')

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

print('================正则表达式=================')
# print('a b  c'.split(' '))
print(re.split(r'\s+', 'a b  c'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 返回一个match 对象
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0), m.group(1), m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())

re_mail = re.compile(r'([\w.<>\s]+@\w+.\w+)')
print(re_mail.match('someone@gmail.com').groups())
print(re_mail.match('bill.gates@microsoft.com').groups())
print(re_mail.match('1193334525@qq.com').groups())
print(re_mail.match('tom@voyager.org').groups())
print(re_mail.match('mi_xi_shi_zi@163.com').groups())
print(re_mail.match('<Tom Paris> tom@voyager.org').groups())
print(re_mail.match('liaozhou@uestc.edu.cn').groups())

print('================常用内建模块===============')
print('==================datetime=================')
now = datetime.now()
print(now)
print()

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
print()

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%a, %b %d %H:%M'))
print()

now = now + timedelta(days = 2, hours = 10)
print(now)

# -*- coding:utf-8 -*-

def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	tz = -int(tz_str[3:5])
	dt = dt + timedelta(hours = tz)
	return datetime.timestamp(dt)

print(to_timestamp('2017-3-20 7:50:45', 'UTC+8:00'))

print('Pass')