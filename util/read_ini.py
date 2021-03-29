'''
处理读取LocalElement.ini文件
'''
import configparser

class Read_ini:
	def __init__(self, filename='../config/LocalElement.ini',node='ForgetElement'):
		self.node = node
		self.cf = self.load_ini(filename)

	#加载ini文件
	def load_ini(self, filename):
		cf = configparser.ConfigParser()
		cf.read(filename, encoding="utf-8-sig")
		return cf

	#读取元素
	def get_value(self, key):
		return self.cf.get(self.node, key)

if __name__ == '__main__':
	print(Read_ini('../config/LocalElement.ini', 'ForgetElement').get_value('code_error'))
	'''
	cf = configparser.ConfigParser()
	cf.read('../config/LocalElement.ini')
	print(cf.get('ForgetElement','find_way'))
	'''