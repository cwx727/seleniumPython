import sys
sys.path.append('..')
from util.keyword_excel_util import ExcelUtil
from keywordaction.action_method import ActionMethod

class ActionMethod_KW:
	def run_main(self):
		handle_excel = ExcelUtil()
		self.action_method = ActionMethod()
		case_lines = handle_excel.get_count_rows()  #获得案例excel行数
		for i in range(1,case_lines):
			is_run = handle_excel.get_cell_value(i, 3)   #获得案例excel是否执行
			if is_run:
				method = handle_excel.get_cell_value(i, 4)   #获得案例excel执行方法
				send_value = handle_excel.get_cell_value(i, 5)   #获得案例excel输入数据
				handle_value = handle_excel.get_cell_value(i, 6)   #获得案例excel操作元素
				expect_result_method = handle_excel.get_cell_value(i, 7) #获得案例excel预期结果方法
				expect_result = handle_excel.get_cell_value(i, 8)   #获得案例excel预期结果值

				self.run_method(method, send_value, handle_value)  #执行操作
				if expect_result:
					expect_value = self.get_expect_result_value(expect_result)
					if expect_value[0] == 'text':    #如果预期结果等号左边为text
						result = self.run_method(expect_result_method)   #获得等号右边的text的值
						if expect_value[1] in result:     
							handle_excel.write_cell_value(i, 'pass')
						else:
							handle_excel.write_cell_value(i, 'fail')
					elif expect_value[0] == 'element':  #如果预期结果值等号左边为element
						result = self.run_method(expect_result_method, expect_value[1]) #将预期结果操作和元素传入查找
						if result:   #如果找到预期结果元素
							handle_excel.write_cell_value(i, 'pass')
						else:
							handle_excel.write_cell_value(i, 'fail')



	def get_expect_result_value(self, data):
		return data.split('=')



	def run_method(self, method, send_value='', handle_value=''):

		method_value = getattr(self.action_method, method)  #查找ActionMethod中方法名为methon的方法
		print(method,send_value,handle_value)
		if send_value!='' and handle_value!='':
			result = method_value(handle_value, send_value)     
		elif handle_value!='' and send_value=='':
			result = method_value(handle_value)
		elif send_value=='' and handle_value =='':
			result = method_value()
		else:
			result = method_value(send_value)
		return result

if __name__ == '__main__':
	ActionMethod_KW().run_main()


