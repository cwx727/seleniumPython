from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
import random


import urllib
import urllib.request
import base64
import re
import json



driver = webdriver.Chrome()

driver.get("https://passport.isoftstone.com/forgot")
#driver.maximize_window()
time.sleep(2)
print(EC.title_contains("服务"))
driver.find_element_by_class_name("umobile").click()
time.sleep(2)
# locator = (By.ID,"RP_EmpDomainName")  #用By方法定位元素
# element_appear = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))  #等待10s，直到元素出现，有返回true，无返回false
# #time.sleep(2)

# element_RP_EmpDomainName = driver.find_element_by_id("RP_EmpDomainName")
# print(element_RP_EmpDomainName.get_attribute("data-val-required"))    #获得元素属性值
# element_RP_EmpDomainName.send_keys("222")
# driver.find_element_by_name("RP_EmpMobile").send_keys("333")
# driver.find_element_by_id("imgcode").send_keys("444")


'''
保存验证码图片
'''
driver.save_screenshot("../image/code_brower.png")  #保存浏览器截图

element_imgcode = driver.find_element_by_id("cimg")  #找到验证码元素
#print(element_imgcode.location)  #返回验证码坐标{'x': 422, 'y': 414}
left = element_imgcode.location['x']    
top = element_imgcode.location['y']
right = left + element_imgcode.size['width']   
down = top + element_imgcode.size['height']
im = Image.open("../image/code_brower.png")   #打开浏览器截图
img = im.crop((left, top, right, down))  #截取验证码的图
img.save("../image/code_img.png")    #保存验证码图





#API产品路径
host = 'https://codevirify.market.alicloudapi.com'
path = '/icredit_ai_image/verify_code/v1'
#阿里云APPCODE
appcode = '03c1e54feda948179da812867f14a72c'
url = host + path 
bodys = {}
querys = ""


f = open(r'..\image\code_img.png', 'rb')
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
    #print(content.decode('utf-8'))
    content1 = content.decode('utf-8')
    #print(json.loads(content1)['VERIFY_CODE_ENTITY']['VERIFY_CODE'])
    text = json.loads(content1)['VERIFY_CODE_ENTITY']['VERIFY_CODE']

driver.find_element_by_id("imgcode").send_keys(text)
time.sleep(5)
driver.close()

'''
随机生成邮箱格式
返回：
	2ac14@163.com
	3c21d@163.com
	fd1b5@163.com
	3cd62@163.com
'''
# for i in range(1,5):
# 	#random.sample('123456abcdef',5))从123456abcdef中随机取5个字符，返回列表，用join拼接
# 	print(''.join(random.sample('123456abcdef',5))+'@163.com')  
