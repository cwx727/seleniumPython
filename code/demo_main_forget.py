'''未封装代码'''

from selenium import webdriver
import time
import random
from PIL import Image
import urllib
import urllib.request
import base64
import re
import json

driver = webdriver.Chrome()

#打开url
def start_webdriver():
	driver.get("https://passport.isoftstone.com/forgot")
	driver.maximize_window()
	time.sleep(2)


#查找元素
def find_element(method, value):
	if method == 'id':
		element = driver.find_element_by_id(value)
	elif method == 'name':
		element = driver.find_element_by_name(value)
	elif method == "class_name":
		element = driver.find_element_by_class_name(value)
	return element

#生成随机数
def get_range_user():
	return ''.join(random.sample('12345678901',11))

#获得验证码图片
def get_code(filename):
	driver.save_screenshot(filename)
	element = find_element('id',"cimg")
	left = element.location['x']
	top = element.location['y']
	right = left + element.size['width']
	down = top + element.size['height']
	im = Image.open(filename)
	img = im.crop((left, top, right, down))
	img.save(filename)

#识别验证码
def code_online(filename):
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

def run_main():
	user_tel = get_range_user()
	user_name = user_tel + '@163.com'
	filename = "../image/code_img.png"
	start_webdriver()
	find_element("class_name","umobile").click()
	time.sleep(2)
	find_element("id", "RP_EmpDomainName").send_keys(user_name)
	find_element("id", "RP_EmpMobile").send_keys(user_tel)
	get_code(filename)
	code = code_online(filename)
	find_element("name", 'code').send_keys(code)
	time.sleep(2)

	driver.close()

if __name__ == "__main__":
	run_main()



