import mysql.connector
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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