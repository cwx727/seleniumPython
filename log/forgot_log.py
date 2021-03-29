import logging
import os
import datetime

class ForgotLog:
	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)  #设置日志级别
		#控制台输出日志
		# self.consle = logging.StreamHandler() #设置流,建立一个streamhandler来把日志打在CMD窗口上
		# self.logger.addHandler(consle)    #将相应的handler添加在logger对象中

		#按日期生成日志名


		# base_dir = os.path.abspath(os.path.abspath(__file__))
		# file_dir = os.path.join(base_dir, "logs")
		filename = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
		print(filename)

		#文件输出日志
		#self.file_handle = logging.FileHandler(os.path.join("../log/logs", filename), 'a', encoding='utf-8')
		self.file_handle = logging.FileHandler(os.path.join("C:/Users/admin/Desktop/python/selenium/log/logs", filename), 'a', encoding='utf-8')
		self.file_handle.setLevel(logging.INFO)
		self.logger.addHandler(self.file_handle)
		formatter = logging.Formatter('%(asctime)s %(filename)s --> %(funcName)s %(levelno)s : %(levelname)s -----> %(message)s ')
		self.file_handle.setFormatter(formatter)  #设置日志格式

	def run_log(self):
		return self.logger


	def close_log(self):
		self.file_handle.close()
		self.logger.removeHandler(self.file_handle)

		# self.consle.close()   #关闭consle
		# self.logger.removeHandler(consle)  #移除日志

	'''

	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)  #设置日志级别
	#控制台输出日志
	consle = logging.StreamHandler() #设置流,建立一个streamhandler来把日志打在CMD窗口上
	logger.addHandler(consle)    #将相应的handler添加在logger对象中

	filename = datetime.datetime.now().strftime("%Y-%m-%d")+".log"

	#文件输出日志
	file_handle = logging.FileHandler(os.path.join('./logs/', filename), 'a', encoding='utf-8')
	formatter = logging.Formatter('%(asctime)s %(filename)s --> %(funcName)s %(levelno)s : %(levelname)s -----> %(message)s ')
	file_handle.setFormatter(formatter)  #设置日志格式
	logger.addHandler(file_handle)
	logger.debug("test")
	'''

if __name__ == "__main__":
	testLogger = ForgotLog()
	testLogger.run_log()
	testLogger.close_log()
