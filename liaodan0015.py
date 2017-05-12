import socket, threading, time
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

print('==============网络编程============')

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create a connection
s.connect(('www.sina.com.cn', 80))
# send data
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# receive the data
buffer = []
while True:
	# it only can receive 1k bytes once
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break

data = b''.join(buffer)
# close the connection
s.close()

print('data has been downloaded...')
print('here is the header of page...\n')
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
print()
# write the html to file
print('writing...')
# with open('other\sina.html', 'wb') as f:
# 	f.write(html)
print('writing finished...\n')

print('==============SMTP发送邮件============')

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
# msg = MIMEMultipart('alternative') # it can support the 'plain' and 'html'
msg = MIMEMultipart()	# mail object

# input Email address and password
from_addr = input('From: ')
password = input('Password: ')
# input receiver's address
to_addr = input('To: ')
# input SMTP server address
smtp_server = input('SMTP server: ')

print()
print('sending the mail...')
# try:
# 	# SMTP's default port is 25
# 	server = smtplib.SMTP_SSL(smtp_server, 465)
# 	# server.set_debuglevel(1)
# 	server.login(from_addr, password)
# 	server.sendmail(from_addr, [to_addr], msg.as_string())
# 	server.quit()
# 	print('send finished...')
# except Exception as e:
# 	print('send failed: %s' % e)

# another way to send the mail
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

msg['From'] = _format_addr('Python Enthusiast <%s>' % from_addr)
msg['To'] = _format_addr('Manager <%s>' % to_addr)
msg['Subject'] = Header('helo from SMTP...', 'utf-8').encode()

# try:
# 	server = smtplib.SMTP_SSL(smtp_server, 465)
# 	server.set_debuglevel(1)
# 	server.login(from_addr, password)
# 	server.sendmail(from_addr, [to_addr], msg.as_string())
# 	server.quit()
# 	print('send finished...')
# except Exception as e:
# 	print('send failed: %s' % e)

# mail context is MIMEText
# it can use the image in the content with 'html' model
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + 
	'<p><img src = 'cid:0'></p>' + 
	'</body></html>', 'html', 'utf-8'))
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'utf-8'))

# add a file means to add a MIMEBase, read a image from local
with open('image\image.jpg', 'rb') as f:
	# set the MIME and its filename, here is jpeg type
	mime = MIMEBase('image', 'jpeg', filename = 'image.jpg')
	# add the needed header information
	mime.add_header('Content-Disposition', 'attachment', filename = 'image.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	# read the file's content
	mime.set_payload(f.read())
	# encode with Base64
	encoders.encode_base64(mime)
	# add to the MIMEMultipart
	msg.attach(mime)

try:
	server = smtplib.SMTP_SSL(smtp_server, 465)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
	print('send finished...')
except Exception as e:
	print('send failed: %s' % e)
	raise e