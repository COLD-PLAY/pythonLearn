from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen
from xml.parsers.expat import ParserCreate
from html.parser import HTMLParser
from html.entities import name2codepoint

print('===================contextlib=================')

class Query(object):
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')

	def query(self):
		print('Query info about %s...' % self.name)

# with Query('Bob') as q:
# 	q.query()

# @contextmanager 接受一个generator
# yield 语句把with ... as var 把变量输出出去
# 然后with 语句就可以正常的使用了
# with 首先执行yield 之前的语句，然后执行with 里面的语句
# 最后执行yield 之后的语句
@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('Bob') as q:
	q.query()

@contextmanager
def tag(name):
	print('<%s>' % name)
	yield
	print('</%s>' % name)

with tag('h1'):
	print('hello')
	print('world')

# @closing，如果一个对象没有实现上下文，我们就不能把它用于with 语句
# 这个时候，可以用closing() 来把对象变为上下文对象

# with closing(urlopen('https://www.python.org')) as page:
# 	for line in page:
# 		print(line)

# closing() 的作用就是将任意对象变为上下文对象，并支持with 语句
@contextmanager
def closing(thing):
	try:
		yield thing
	finally:
		thing.close()

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax: start_element: %s, attrs: %s' % (name, str(attrs)))

	def end_element(self, name):
		print('sax: end_element: %s' % name)
	
	def char_data(self, text):
		print('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler  = handler.char_data
parser.Parse(xml)

def get_xml():
	L = []
	L.append(r'<?xml version="1.0"?>')
	L.append(r'<root>')
	L.append(encode('some & data'))
	L.append(r'</root>')
	return ''.join(L)

print('===================HTMLParser=================')

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')

	def handle_entityref(self, name):
		print('&%s;' % name)

	def handle_charref(self, name):
		print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')