import socket

print('==============TCP编程============')

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(('127.0.0.1', 9999))

# print(s.recv(1024).decode('utf-8'))
# for data in [b'MiXiShiZi', b'LiaoZhou', b'ColdPlay']:
# 	s.send(data)
# 	print(s.recv(1024).decode('utf-8'))

# s.send(b'exit')
# s.close()

print('==============UDP编程============')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'MiXiShiZi', b'LiaoZhou', b'ColdPlay']:
	# send the data
	s.sendto(data, ('127.0.0.1', 9999))
	# receive the data
	print(s.recv(1024).decode('utf-8'))
s.close()