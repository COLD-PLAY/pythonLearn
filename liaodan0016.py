import sqlite3
import mysql.connector
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# we need to commit our command when use sqllite's or mysql's 'insert' command
print('==================使用SQLite=================')
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'MiXiShiZi\')')
# cursor.rowcount
# cursor.close()
# conn.commit()
# conn.close()

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('select * from user where id=?', ('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
try:
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
	cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
	cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
	cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
except Exception as e:
	print('something goes wrong... %s' % e)
	raise e
finally:
	cursor.close()
	conn.commit()
	conn.close()

def get_score_in(low, high):
    # ' 返回指定分数区间的名字，按分数从低到高排序 '
    L = []
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where score between ? and ?', (low, high))
    values = cursor.fetchall()
    values_sorted = sorted(values, key = lambda i: i[2])
    for i in values_sorted:
    	L.append(i[1])
    return L

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

try:
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute('select * from user')
	values = cursor.fetchall()
	print(values)
except Exception as e:
	print('something goes wrong... %s' % e)
	raise e
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()

print('Pass')

print('==================使用MYSQL=================')

# try:
# 	# set the password for your root
# 	conn = mysql.connector.connect(user = 'root', password = '', database = 'coldplay')
# 	cursor = conn.cursor()
# 	# create user table
# 	cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 	# insert a row of record, notice: MySQL's %s
# 	cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'MiXiShiZi'])
# 	print(cursor.rowcount)
# 	# submit the command
# 	conn.commit()
# except Exception as e:
# 	raise e
# finally:
# 	if cursor:
# 		cursor.close()
# 	if conn:
# 		conn.close()

# try:
# 	# search command
# 	cursor = conn.cursor()
# 	cursor.execute('select * from user where id = %s', ('1',))
# 	values = cursor.fetchall()
# 	print(values)
# except Exception as e:
# 	raise e
# finally:
# 	# close the Cursor and Connection
# 	if cursor:
# 		cursor.close()
# 	if conn:
# 		conn.close()

print('================使用SQLAlchemy===============')

# create the base class of object
Base = declarative_base()

# define User object
class User(Base):
	# name of table
	__tablename__ = 'user'

	# structure of table
	id = Column(String(20), primary_key = True)
	name = Column(String(20))

# initlize the connection of database
engine = create_engine('mysql+mysqlconnector://root:liaozhou1998@localhost:3306/test')
# create DBSession type
DBSession = sessionmaker(bind = engine)

try:
	# create session object
	session = DBSession()
	# create new User object
	new_user = User(id = '5', name = 'Bob')
	# add to session
	session.add(new_user)
	# submit(save) to database
	session.commit()
except Exception as e:
	raise e
finally:
	# close session
	if session:
		session.close()