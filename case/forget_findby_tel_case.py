'''测试案例,调用bussiness层方法'''
import sys
sys.path.append('..')
from bussiness.forget_findby_tel_bussiness import ForgetFindByTelBussiness
from selenium import webdriver

class ForgetFindByTelCase:
	def __init__(self):
		driver = webdriver.Chrome()
		driver.get("https://passport.isoftstone.com/forgot")
		self.forget_tel_bussiness = ForgetFindByTelBussiness(driver)

	def test_forget_username_null(self):
		if self.forget_tel_bussiness.forget_user_name_null(user_name='', user_tel='2', code_text='3'):
			print("邮箱为空，测试成功")

	def test_forget_tel_null(self):
		if self.forget_tel_bussiness.forget_user_tel_null(user_name='1', user_tel='', code_text='3'):
			print("手机为空，测试失败")

	def test_forget_code_error(self):
		if self.forget_tel_bussiness.forget_code_error(user_name='1', user_tel='2', code_text='3'):
			print("验证码错误，测试通过")
		else:
			print("验证码错误，测试失败")


	def test_forget_success(self):
		if self.forget_tel_bussiness.forget_success(user_name='1', user_tel='2'):
			print("短信发送失败，测试失败")
		else:
			print("短信发送失败，测试通过")

if __name__ == '__main__':
	case = ForgetFindByTelCase()
	#case.test_forget_username_null()
	#case.test_forget_tel_null()
	case.test_forget_code_error()
	case.test_forget_success()
