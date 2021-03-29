'''调用page，加入操作'''
import sys
sys.path.append('..')
from page.forget_findby_tel_page import ForgetFindByTelPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgetFindByTelHandle:
	def __init__(self,driver):
		self.forget_tel_page = ForgetFindByTelPage(driver)

	def click_find_way(self):
		if self.forget_tel_page.find_way():
			self.forget_tel_page.find_way().click()

	#输入用户名
	def send_user_name(self, user_name):
		self.forget_tel_page.get_user_name().send_keys(user_name)

	#输入手机
	def send_user_tel(self, user_tel):
		self.forget_tel_page.get_user_tel().send_keys(user_tel)

	#输入验证码
	def send_code(self, code_text):
		self.forget_tel_page.get_code().send_keys(code_text)

	'''
	def send_code_error(self, info, user_info):
		if self.forget_tel_page.get_code_error().text:
			print('get_code_error  find')
				return True
		else:
			print('user_code_error  unfind')
				return False
	'''		


	#获得页面提示信息
	def get_user_text(self, info, user_info):
		if info == 'user_name_null':
			if self.forget_tel_page.get_user_name_null().text == user_info:
				print('user_name_null  find')
				return True
			else:
				print('user_name_null  unfind')
				return False

		elif info == 'user_tel_null':
			if self.forget_tel_page.get_user_tel_null().get_attribute("textContent")==user_info:
				print("user_tel_null find")
				return True
			else:
				print('user_tel_null  unfind')
				return False
		elif info == 'code_error':
			if self.forget_tel_page.code_error().text==user_info:
				#print(self.forget_tel_page.code_error().text+"find"+user_info)
				return True
			else:
				#print(self.forget_tel_page.code_error().text+" unfind"+user_info)
				return False

			'''
			if self.forget_tel_page.get_code_error().text:
				print("get_code_error find")
				return True
			else:
				print('get_code_error  unfind')
				return False
			'''

	#点击发送信息至手机
	def click_submit(self):
		self.forget_tel_page.submit().click()
