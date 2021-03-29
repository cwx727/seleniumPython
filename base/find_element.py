'''
调用read_ini读取文件，实现find_element
'''

import sys
sys.path.append('..')
sys.path.append('C:/Users/admin/Desktop/python/selenium')
from util.read_ini import Read_ini
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

class FindElement:
	def __init__(self, driver):
		self.driver = driver

	def get_element(self, key):
		'''
		从ini文件中取到元素属性和值，并封装成find_element方法
		'''
		#data = Read_ini(filename='../config/LocalElement.ini',node='ForgetElement').get_value(key)
		data = Read_ini(filename='C:/Users/admin/Desktop/python/selenium/config/LocalElement.ini',node='ForgetElement').get_value(key)
		
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
				print("111")
				return self.driver.find_element_by_xpath(value)

		except:
			return None


	'''By方法定位元素是否存在'''

	def get_element_locator(self, key):
		#data = Read_ini(filename='../config/LocalElement.ini',node='ForgetElement').get_value(key)
		data = Read_ini(filename='C:/Users/admin/Desktop/python/selenium/config/LocalElement.ini',node='ForgetElement').get_value(key)
		by = data.split('>')[0]
		value = data.split('>')[1]

		if by == 'id':
			locator = (By.ID, value)
		elif by == 'name':
			locator = (By.NAME, value)
		elif by == 'class_name':
			locator = (By.CLASS_NAME, value)
		elif by == 'xpath':
			locator = (By.XPATH, value)	
		try:
			WebDriverWait(self.driver, 30,0.5).until(EC.visibility_of_element_located(locator))
			print("定位到了")
			return self.get_element(key)
		except:
		#print(self.get_element(key).text)
			return None

if __name__ == '__main__':
	from selenium import webdriver
	import time
	'''
	driver = webdriver.Chrome()
	print(FindElement(driver).get_element("find_way"))
	driver.close()
	'''
	driver = webdriver.Chrome()
	driver.get("https://passport.isoftstone.com/forgot")
	time.sleep(1)

	driver.find_element_by_class_name("umobile").click()
	time.sleep(1)
	driver.find_element_by_name("RP_EmpDomainName").send_keys("333")
	driver.find_element_by_name("RP_EmpMobile").send_keys("333")
	driver.find_element_by_id("imgcode").send_keys("444")

	driver.find_element_by_id("mbtn").click()
	time.sleep(1)
	print(FindElement(driver).get_element_locator("code_error").text)
	driver.close()

