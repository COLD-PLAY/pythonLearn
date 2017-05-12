from wsgiref.simple_server import make_server
from flask import Flask
from flask import request
from flask import render_template
import asyncio, threading

print('===================WSGI=================')

# def application(environ, start_response):
# 	start_response('200 OK', [('Content-Type', 'text/html')])
# 	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Web')
# 	return [body.encode('utf-8')]

# create a server, ip address is null
# port is 8000, function is application
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')
# start listen HTTP request
# httpd.serve_forever()

print('==============Use Web Frame=============')
print('=============Use the Template===========')

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	# return '<h1>Home</h1>'
	return render_template('home.html')

@app.route('/signin', methods = ['GET'])
def signin_from():
	print(request.method)
	# return '''<form action = "/signin" method = "post">
	# 		  <p><input name = "username"></p>
	# 		  <p><input name = "password" type = "password"></p>
	# 		  <p><button type = "submit">Sign In</button></p>
	# 		  </form>'''
	return render_template('form.html')

@app.route('/signin', methods = ['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	# it's needful to read form content from the request object
	if username == 'admin' and password == 'password':
		# return '<h3>Hello, Admin!</h1>'
		return render_template('signin-ok.html', username = username)
	# return '<h3>Bad username or password.</h3>'
	return render_template('form.html', message = 'Bad username or password.', username = username)

if __name__ == '__main__':
	app.run()

print('=============Asynchronous IO===========')

# do_some_code()
# f = open('/path/to/file', 'r')
# r = f.read()	# <== thread stop and wait for the IO result
# # thread execute again while IO finished
# do_some_code()

# this is asynchronous
# loop = get_event_loop()
# while True:
# 	event = loop.get_event()
# 	process_event(event)

# this is the Coroutine
def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'

def produce(c):
	c.send(None);
	n = 0
	while n < 5:
		n += 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()

c = consumer()
produce(c)

print('==============asyncio=============')

@asyncio.coroutine
def hello():
	print('Hello %s!' % threading.currentThread())
	# asy call the asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print('Hello Again, %s!' % threading.currentThread())

# get the ventLoop
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# execute coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

print()

# @asyncio.coroutine
# def wget(host):
# 	print('wget %s...' % host)
# 	connect = asyncio.open_connection(host, 80)
# 	reader, writer = yield from connect
# 	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
# 	writer.write(header.encode('utf-8'))
# 	yield from writer.drain()
# 	while True:
# 		line = yield from reader.readline()
# 		if line == b'\r\n':
# 			break
# 		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
# 	# Ignore the body, close the socket
# 	writer.close()

# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# new grammer
async def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = await connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line = await reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	# Ignore the body, close the socket
	writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()