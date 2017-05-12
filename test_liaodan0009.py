import unittest
from liaodan0009 import Dict

# 单元测试代码，为liaodan0009.py 中的Dict 类做一个测试
class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a = 1, b = 'test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'text')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
# 运行测试
if __name__ == '__main__':
	unittest.main()