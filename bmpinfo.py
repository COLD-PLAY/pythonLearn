import struct, os

while True:
	url = input('input the url of your file: ')
	if not os.path.isfile(url):
		print('\tthis is not a right url, please input again')
		continue

	with open(url, 'rb') as f:
		b = f.read()[0:30]
		t = struct.unpack('<ccIIIIIIHH', b)
		if (t[0] == b'B' and t[1] == b'M'):
			print('\tthis is a bmp and its size is %dx%d, colornum is %d' % (t[6], t[7], t[9]))
		else:
			print('\tthis is not bmp file')
