'''测试案例,调用bussiness层方法'''
import sys
sys.path.append('..')
sys.path.append('C:/Users/admin/Desktop/python/selenium')
from bussiness.forget_findby_tel_bussiness import ForgetFindByTelBussiness
from selenium import webdriver
import unittest
from base.HTMLTestRunner import HTMLTestRunner
import time
from log.forgot_log import ForgotLog



class ForgetFindByTelCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.forget_tel_bussiness = ForgetFindByTelBussiness(cls.driver)
		cls.logclass = ForgotLog()
		cls.log = cls.logclass.run_log()

	def setUp(self):
		self.driver.get("https://passport.isoftstone.com/forgot")
		self.log.info("chrome")  #设置日志只打印chrome
	
	
	def test01_forget_username_null(self):
		self.assertTrue(self.forget_tel_bussiness.forget_user_name_null(user_name='', user_tel='2', code_text='3'))
	
				
	def test02_forget_tel_null(self):
		self.assertTrue(self.forget_tel_bussiness.forget_user_tel_null(user_name='1', user_tel='', code_text='3'))


	def test03_forget_code_error(self):
		self.assertTrue(self.forget_tel_bussiness.forget_code_error(user_name='1', user_tel='2', code_text='3'))
		'''
		if self.forget_tel_bussiness.forget_code_error(user_name='1', user_tel='2', code_text='3'):
			print("验证码错误，测试通过")
		else:
			print("验证码错误，测试失败")
		'''


	def test04_forget_success(self):
		self.assertFalse(self.forget_tel_bussiness.forget_success(user_name='1', user_tel='2'))
		'''
		if self.forget_tel_bussiness.forget_success(user_name='1', user_tel='2', code_text='3'):
			print("短信发送失败，测试失败")
		else:
			print("短信发送失败，测试通过")
		'''

	def tearDown(self):
		pass

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.logclass.close_log()






if __name__ == '__main__':
	unittest.main()

	'''
	suite = unittest.TestSuite()
	cases = unittest.TestLoader().loadTestsFromTestCase(ForgetFindByTelCase)
	suite.addTests(cases)
	#testRunner = unittest.TextTestRunner(verbosity=2)
	#testRunner.run(suite)
	now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
	#HtmlFile = "../report/" + now + "_Report.html"
	HtmlFile = "C:/Users/admin/Desktop/python/selenium/report/" + now + "_Report.html"
	#fp = file(HtmlFile, "wb")
	with open(HtmlFile, "wb") as fp:
    	#声明一个runner
		myTestRunner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")

    	#执行Runner
		myTestRunner.run(suite)
	'''



