'''

#pytesseract 方法，需安装Tesseract-OCR

import pytesseract
from PIL import Image

img = Image.open("./code_brower.png") 
text = pytesseract.image_to_string(img)
print(text)
'''


'''
阿里云第三方API方法
'''
import urllib
import urllib.request
import base64
import re
import json


#API产品路径
host = 'https://codevirify.market.alicloudapi.com'
path = '/icredit_ai_image/verify_code/v1'
#阿里云APPCODE
appcode = '03c1e54feda948179da812867f14a72c'
url = host + path 
bodys = {}
querys = ""


f = open(r'.\code_img.png', 'rb')
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
    print(content.decode('utf-8'))
    content1 = content.decode('utf-8')
    print(json.loads(content1)['VERIFY_CODE_ENTITY']['VERIFY_CODE'])




'''
阿里云实例
import urllib
import urllib.request
import base64
import re

#API产品路径
host = 'https://codevirify.market.alicloudapi.com'
path = '/icredit_ai_image/verify_code/v1'
#阿里云APPCODE
appcode = '阿里云APPCODE'
url = host + path 
bodys = {}
querys = ""

#参数配置
if False:
    #启用BASE64编码方式进行识别
    #内容数据类型是BASE64编码
    f = open(r'本地图片路径', 'rb')
    contents = base64.b64encode(f.read())
    f.close()
    bodys['IMAGE'] = contents
    bodys['IMAGE_TYPE'] = '0'
else:
    #启用URL方式进行识别
    #内容数据类型是图像文件URL链接
    bodys['IMAGE'] = 'https://icredit-api-market.oss-cn-hangzhou.aliyuncs.com/%E9%AA%8C%E8%AF%81%E7%A0%81.jpg'
    bodys['IMAGE_TYPE'] = '1'

post_data = urllib.parse.urlencode(bodys).encode('utf-8')

request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content.decode('utf-8'))
'''

