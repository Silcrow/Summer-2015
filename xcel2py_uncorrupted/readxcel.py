import xlrd

file_location = "C:/python_practices/xcel_python/Apple.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print sheet.cell_value(0,0)
print sheet.nrows
print sheet.ncols

for col in range(sheet.ncols):
	print sheet.cell_value(0, col)

for row in range(sheet.nrows):
	print sheet.cell_value(row,0)