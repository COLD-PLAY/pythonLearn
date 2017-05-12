import socket, threading, time

# two ways to program a server
print('==============TCP编程============')

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # listener port
# s.bind(('127.0.0.1', 9999))
# s.listen(5)
# print('Waiting for connection...')

# def tcplink(sock, addr):
# 	print('Accept new connection from %s: %s...' % addr)
# 	sock.send(b'Welcome!')
# 	while True:
# 		data = sock.recv(1024)
# 		time.sleep(1)
# 		if not data or data.decode('utf-8') == 'exit':
# 			break
# 		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
# 	sock.close()
# 	print('Connection from %s: %s closed' % addr)

# while  True:
# 	# recieve a new connection
# 	sock, addr = s.accept()
# 	# create a new thread to handle TCP connection
# 	t = threading.Thread(target = tcplink, args = (sock, addr))
# 	t.start()

# UDP programming only need using the 'sendto' function to send data
# not need to connect or listen, it's easy, isn't it?
print('==============UDP编程============')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the port
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999....')
while True:
	# receive data
	data, addr = s.recvfrom(1024)
	print('Receive from %s: %s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)