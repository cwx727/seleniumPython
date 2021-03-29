import unittest
import ddt
import sys
sys.path.append('..')
from bussiness.forget_findby_tel_bussiness import ForgetFindByTelBussiness
from selenium import webdriver
import unittest
from base.HTMLTestRunner import HTMLTestRunner
import time
from util.excel_util import ExcelUtil

@ddt.ddt
class DdtForgetFindbyTelCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.forget_tel_bussiness = ForgetFindByTelBussiness(cls.driver)

	def setUp(self):
		self.driver.get("https://passport.isoftstone.com/forgot")
	'''
	@ddt.data(
		['','2','3','user_name_null','员工域名 字段是必需的。'],
		['1','','3','user_tel_null','绑定手机 字段是必需的。'],
		['1','2','3','code_error','验证码输入有误']
		)

	@ddt.unpack
	def test01_forget_username_null(self,user_name,user_tel,code_text,assertCode,assertText):
		self.assertTrue(self.forget_tel_bussiness.forget_function(user_name,user_tel,code_text,assertCode,assertText))
	'''
	data = ExcelUtil().table_list()

	@ddt.data(*data)
	def test01_forget_username_null(self,data):
		user_name,user_tel,code_text,assertCode,assertText = data
		self.assertTrue(self.forget_tel_bussiness.forget_function(user_name,user_tel,code_text,assertCode,assertText))

	def tearDown(self):
		pass

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()



if __name__ == '__main__':
	unittest.main()
	'''
	suite = unittest.TestSuite()
	cases = unittest.TestLoader().loadTestsFromTestCase(DdtForgetFindbyTelCase)
	suite.addTests(cases)
	#testRunner = unittest.TextTestRunner(verbosity=2)
	#testRunner.run(suite)
	now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
	HtmlFile = "../report/" + now + "_Report.html"
	#fp = file(HtmlFile, "wb")
	with open(HtmlFile, "wb") as fp:
    	#声明一个runner
		myTestRunner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")

    	#执行Runner
		myTestRunner.run(suite)
	'''
	