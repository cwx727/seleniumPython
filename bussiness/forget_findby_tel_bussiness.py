'''调用handle层方法，被case层调用'''
import sys
sys.path.append('..')
sys.path.append('C:/Users/admin/Desktop/python/selenium')
from handle.forget_findby_tel_handle import ForgetFindByTelHandle
import time
from base.get_code_online import GetCodeOnline



class ForgetFindByTelBussiness:
	def __init__(self,driver):
		self.driver = driver
		self.forget_tel_handle= ForgetFindByTelHandle(self.driver)


	def user_base(self, user_name='', user_tel='', code_text=''):
		time.sleep(2)
		self.forget_tel_handle.click_find_way()
		
		time.sleep(2)
		self.forget_tel_handle.send_user_name(user_name)
		self.forget_tel_handle.send_user_tel(user_tel)
		self.forget_tel_handle.send_code(code_text)
		time.sleep(2)
		self.forget_tel_handle.click_submit()
		time.sleep(2)


	def forget_user_name_null(self, user_name='', user_tel='', code_text=''):
		self.user_base(user_name, user_tel, code_text)
		time.sleep(1)

		
		if self.forget_tel_handle.get_user_text("user_name_null","员工域名 字段是必需的。"):


			print("用户名为空")
			return True
		else:
			return False
		
		

	def forget_user_tel_null(self, user_name='', user_tel='', code_text=''):
		self.user_base(user_name, user_tel, code_text)
		time.sleep(1)
		if self.forget_tel_handle.get_user_text("user_tel_null","绑定手机 字段是必需的。"):
			print("手机为空")
			return True
		else:
			return False


	def forget_code_error(self, user_name='', user_tel='', code_text=''):
		self.user_base(user_name, user_tel, code_text)
		time.sleep(1.5)
		if self.forget_tel_handle.get_user_text("code_error","111"):
			print("验证码错误")
			return True
		else:
			print("text为空")
			return False

	def forget_success(self, user_name='', user_tel='', code_text=''):
		get_code = GetCodeOnline(self.driver)
		code_text1 = get_code.code_online()
		time.sleep(1)
		self.user_base(user_name,user_tel,code_text1)
		time.sleep(2)

		if self.forget_tel_handle.get_user_text("code_error",code_text1):
			return True
		else:
			print("发送短信成功")
			return False

	'''ddt框架def'''
	def forget_function(self,user_name,user_tel,code_text,assertCode,assertText):
		self.user_base(user_name, user_tel, code_text)
		time.sleep(1)
		if self.forget_tel_handle.get_user_text(assertCode,assertText):
			return True
		else:
			return False


		