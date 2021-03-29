'''读取find_element,获得页面元素,提供给handle'''
import sys
sys.path.append('..')
from base.find_element import FindElement

class ForgetFindByTelPage:
	def __init__(self,driver):
		self.find_element_element = FindElement(driver)

	def find_way(self):
		return self.find_element_element.get_element("find_way")

	def get_user_name(self):
		return self.find_element_element.get_element("user_name")

	def get_user_name_null(self):
		return self.find_element_element.get_element("user_name_null")

	def get_user_tel(self):
		return self.find_element_element.get_element("user_tel")

	def get_user_tel_null(self):
		return self.find_element_element.get_element("user_tel_null")

	def get_code(self):
		return self.find_element_element.get_element("code_text")

	def code_error(self):
		return self.find_element_element.get_element_locator("code_error")

	def submit(self):
		return self.find_element_element.get_element("submit")



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
	print(ForgetFindByTelPage(driver).code_error())

