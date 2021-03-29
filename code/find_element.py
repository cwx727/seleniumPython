'''
调用read_ini读取文件，实现find_element
'''

import sys
sys.path.append('..')
from util.read_ini import Read_ini

class FindElement:
	def __init__(self, driver):
		self.driver = driver

	def get_element(self, key):
		'''
		从ini文件中取到元素属性和值，并封装成find_element方法
		'''
		data = Read_ini(filename='../config/LocalElement.ini',node='ForgetElement').get_value(key)
		by = data.split('>')[0]
		value = data.split('>')[1]
		try:
			if by == 'id':
				return self.driver.find_element_by_id(value)
			elif by == 'name':
				return self.driver.find_element_by_name(value)
			elif by == "class_name":
				return self.driver.find_element_by_class_name(value)
			elif by == 'xpath':
				return self.driver.find_element_by_xpath(value)
		except:
			return None

if __name__ == '__main__':
	from selenium import webdriver
	driver = webdriver.Chrome()
	print(FindElement(driver).get_element("find_way"))
	driver.close()

