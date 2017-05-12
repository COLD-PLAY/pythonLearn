from enum import Enum, unique

print('======================================')
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

print('======================================')
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print(day1, '=>', day1.value)
print(Weekday(3), '=>', Weekday(3).value)

# class Hello(object):
# 	def hello(self, name = 'world'):
# 		print('Hello, %s.' % name)

# 	def __str__(self):
# 		return '<Hello Object, name: ' + name + '>'

# h = Hello()
# print(h)
# h.hello()
# print(type(h))

def fn(self, name = 'world'):
	print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello = fn))
h = Hello()
h.hello()
print(type(Hello))

class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
	pass

# class MyList(list):
# 	def add(self, value):
# 		self.append(value)

L = MyList()
L.add(1)

print(L)

###################################################
print('======================================')

class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s: %s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

# 这个ModelMetaclass 的作用就是为新建的类（对象）中添加'__mappings__' 和'__table__' 属性
# 并将所有Filed 类实例放进'__mappings__' 里面的dict 中，顺便'__mappings__' 外的那些属性删除
# 把name 作为'__table__' 属性的值
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))

class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')
	age = IntegerField('age')

u = User(id = 12345, name = 'mixishizi', email = 'mi_xi_shi_zi@163.com', password = 'liaozhou1998', age = '19')
u.save()

# print(','.join(['hhh', 'nimei', 'nidaye']))


print('======================================')