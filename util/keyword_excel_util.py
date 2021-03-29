import xlrd
from xlutils.copy import copy

class ExcelUtil:
	def __init__(self, file_path='../config/keyword_casedata.xls', index=0):
		self.file_path = file_path
		self.excel_data = xlrd.open_workbook(self.file_path)
		self.index = index
		self.file_path = file_path
		self.table = self.excel_data.sheets()[self.index]

	#获得excel一行数据
	def table_list(self):
		data = []
		table_nrows = self.get_count_rows()
		if table_nrows >= 2:
			return self.table.nrows
		return None

	#获得行数
	def get_count_rows(self):
		nrows = self.table.nrows
		return nrows

	#取excel中单元格值
	def get_cell_value(self, row, col):
		if self.get_count_rows() > row:
			cell_data = self.table.cell(row, col).value
			return cell_data
		return None

	def write_cell_value(self, row, value):
		read_value = xlrd.open_workbook(self.file_path)
		write_data = copy(read_value)
		write_data.get_sheet(self.index).write(row, 9, value)
		write_data.save(self.file_path)

if __name__ == '__main__':
	print(ExcelUtil().get_cell_value(1,3))
	ExcelUtil().write_cell_value(1,"test")