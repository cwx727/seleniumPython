import xlrd

class ExcelUtil:
	def __init__(self, excel_path='../config/ddt_casedata.xlsx', index=0):
		self.data = xlrd.open_workbook(excel_path)
		self.table = self.data.sheets()[index]
		self.nrows = self.table.nrows

	def table_list(self):
		data = []
		for i in range(1, self.nrows):
			col = self.table.row_values(i)
			data.append(col)
		return data


if __name__ == '__main__':
	print(ExcelUtil().table_list())
