from PIL import Image
import urllib
import urllib.request
import base64
import re
import json
import sys
sys.path.append('..')
sys.path.append('C:/Users/admin/Desktop/python/selenium')
from base.find_element import FindElement

class GetCodeOnline:
	def __init__(self, driver):
		self.driver = driver
		self.find_element = FindElement(self.driver)

	#获得验证码图片
	#def get_code(self, filename='../image/code_img.png'):
	def get_code(self, filename='C:/Users/admin/Desktop/python/selenium/image/code_img.png'):
		self.driver.save_screenshot(filename)
		element = self.find_element.get_element("code_img")
		left = element.location['x']
		top = element.location['y']
		right = left + element.size['width']
		down = top + element.size['height']
		im = Image.open(filename)
		img = im.crop((left, top, right, down))
		img.save(filename)

	#识别验证码
	#def code_online(self, filename='../image/code_img.png'):
	def code_online(self, filename='C:/Users/admin/Desktop/python/selenium/image/code_img.png'):
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