from selenium import webdriver
import sys
sys.path.append('..')
from base.find_element import FindElement
import time


class ActionMethod:

	def open_brower(self, brower):
		if brower == "chrome":
			self.driver = webdriver.Chrome()
		elif brower == "firefox":
			self.driver = webdriver.Firefox()
		else:
			self.driver = webdriver.Edge()

	def get_url(self, url):
		self.driver.get(url)

	def get_element(self, key):
		return FindElement(self.driver).get_element_locator(key)

	def click_element(self, key):
		self.get_element(key).click()

	def send_value(self, key, value=''):
		self.get_element(key).send_keys(value)

	def sleep_time(self):
		time.sleep(1.5)

	def close_browser(self):
		self.driver.close()

	def get_title(self):
		print(self.driver.title)
		return self.driver.title


