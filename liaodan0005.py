from io import StringIO
from io import BytesIO
import time
import os
import pickle
import json

print('================文件读写常见方法================')
# 文件读写
# with open('1.txt', 'r') as f:
# 	for line in f.readlines():
# 		print(line.strip())

# with open('1.txt', 'w') as f:
# 	f.write('Hello Python!')

# StringIO和 BytesIO
# f = StringIO('Hello\nWorld\n!')

# for line in f.readlines():
# 	print(line)

# f = BytesIO()
# f.write('廖舟！'.encode('utf-8'))

# print(f.getvalue())

# f = StringIO()
# f.write('liaozhou')
# print(f.tell())
# f.seek(0)
# print(f.readline())

# 操作文件和目录
# print(os.name)	# 输出系统名字
# print(os.environ)	# 输出环境变量
# print(os.environ.get('PATH'))	# 输出环境变量中的'PATH'

# print(os.path.abspath('.')) # 输出当前目录的绝对路径
# os.path.join('C:/Users/pc/Desktop/CODE/Python', 'testdir') # 新建文件夹之前需要完善文件的信息
# os.mkdir('C:/users/pc/Desktop/CODE/Python/testdir')	# 新建文件
# os.rmdir('C:/users/pc/Desktop/CODE/Python/testdir')	# 删除文件

# print(os.path.split('/path/to/file.txt'))	# 分开成/path/to 和file.txt
# print(os.path.splitext('/path/to/file.txt')) # 分开成/path/to/file 和.txt
# os.rename('1.txt', '2.txt')	# 改名
# os.remove('2.txt')	# 移除文件

# g = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print(g)
# for x in os.listdir('.'):
# 	os.rename(x, x.lower())

# 实现命令行命令dir -l
# def dir_l():
# 	g = [x.lower() for x in os.listdir('.') if os.path.isfile(x) or os.path.isdir(x)]
# 	for dir in g:
# 		print(dir)
# dir_l()

# 实现找出当前目录以及子目录的所有含有string 的文件
# 并且输出该文件的路径
# res = []
# def dir_find(dir ,string):
# 	for doc in os.listdir(dir):
# 		if os.path.isdir(dir + '/' + doc):
# 			dir_find(dir + '/' + doc, string)
# 		elif string in doc:
# 			res.append(dir + '/' + doc)		

# dir_find('C:/Users/pc/Desktop/CODE/Python', 'py')

# for x in res:
# 	print(x)
# print('一共 ' + str(len(res)) + '个文件')
# for f in res:
# 	print(f)

print('================json与对象的转换================')
# Python 的序列化即picking，
# 将内存中的变量变成可存储或传输的过程称之为序列化
# 反过来就是unpicking
# d = dict(name = 'liaozhou', age = 19, score = 666)
# print(pickle.dumps(d))
# pickle.dumps() 方法将任意对象序列化成一个bytes 类型
# 然后就可以将这个bytes 写入文件
# 直接利用pickle.dump() 方法将序列化的bytes 写入文件中
# with open('dump.txt', 'wb') as f:
# 	pickle.dump(d, f)

# 使用loads() 方法反序列化出对象，
# 也可以直接用pickle.load() 方法从一个file-like Object 
# 中直接反序列化出对象，
# with open('dump.txt', 'rb') as f:
# 	byte = f.read()
# d = pickle.loads(byte)
# print(d)
# with open('dump.txt', 'rb') as f:
# 	d = pickle.load(f)
# 	print(d)

# d = dict(name = 'liaozhou', age = 19, score = 666)
# json_str = json.dumps(d)
# print(json_str)

# print(json.loads(json_str))

class Student():
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	def get_score(self):
		return self.score

def stu2dict(stu):
	return {
		'name': stu.name,
		'age': stu.age,
		'score': stu.score
	}

stu = Student('mixishizi', 19, 93)

json_str = json.dumps(stu, default = stu2dict)
print(json_str)
# 一样的作用，通常class 的实例都有一个__dict__ 属性
# __dict__ 就是一个dict，用来存储实例变量。定义了__slots__ 的class 没有
json_str = json.dumps(stu2dict(stu))
print(json_str)
json_str = json.dumps(stu.__dict__)
print(json_str)

def dict2stu(d):
	return Student(d['name'], d['age'], d['score'])
# 通过json.loads() 方法得到了Student 实例化对象
stu1 = json.loads(json_str, object_hook = dict2stu)
print(stu1.get_score())