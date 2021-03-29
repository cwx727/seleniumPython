import sys
sys.path.append('..')

from selenium import webdriver
import time
import random
from PIL import Image
import urllib
import urllib.request
import base64
import re
import json
from find_element import FindElement

class ForgetFunction:
	def __init__(self, url):
		self.driver = self.get_driver(url)

	#driver
	def get_driver(self, url):
		driver = webdriver.Chrome()
		driver.get(url)
		driver.maximize_window()
		time.sleep(2)
		return driver

	#查找元素
	def find_element(self, key):
		return FindElement(self.driver).get_element(key)

	#动作封装
	def send_value(self, key, value):
		self.find_element(key).send_keys(value)

	#动作封装
	def click_element(self,key):
		self.find_element(key).click()


	#生成随机数
	def get_range_user(self):
		return ''.join(random.sample('12345678901',11))

	#获得验证码图片
	def get_code(self, filename):
		self.driver.save_screenshot(filename)
		element = self.find_element("code_img")
		left = element.location['x']
		top = element.location['y']
		right = left + element.size['width']
		down = top + element.size['height']
		im = Image.open(filename)
		img = im.crop((left, top, right, down))
		img.save(filename)

	#识别验证码
	def code_online(self, filename):
		self.get_code(filename)
		host = 'https://codevirify.market.alicloudapi.com'
		path = '/icredit_ai_image/verify_code/v1'
		#阿里云APPCODE
		appcode = '03c1e54feda948179da812867f14a72c'
		url = host + path 
		bodys = {}
		querys = ""

		f = open(filename, 'rb')
		contents = base64.b64encode(f.read())
		f.close()
		bodys['IMAGE'] = contents
		bodys['IMAGE_TYPE'] = '0'

		post_data = urllib.parse.urlencode(bodys).encode('utf-8')
		request = urllib.request.Request(url, post_data)
		request.add_header('Authorization', 'APPCODE ' + appcode)
		request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
		response = urllib.request.urlopen(request)
		content = response.read()

		if (content):
			content = content.decode('utf-8')
			text = json.loads(content)['VERIFY_CODE_ENTITY']['VERIFY_CODE']
			return text


	def run_main(self):
		user_tel = self.get_range_user()     #生成随机数，赋值手机
		user_name = user_tel + '@163.com'    #生成用户名
		filename = "../image/code_img.png"   #验证码路径
		time.sleep(1)
		self.click_element('find_way')       #find_way 为LocalElement.ini中的值
		time.sleep(1)
		self.send_value('user_name',user_name)
		self.send_value('user_tel',user_tel)
		code = self.code_online(filename)
		self.send_value('code_text',code)
		time.sleep(1)
		self.click_element("submit")
		time.sleep(1)
		#判断验证码是否输入正确
		if self.find_element("code_error"):
			time.sleep(1)
			self.driver.save_screenshot('../image/code_error.png')
		else:
			print("注册成功")

		self.driver.close()


if __name__ == '__main__':

	ForgetFunction("https://passport.isoftstone.com/forgot").run_main()

