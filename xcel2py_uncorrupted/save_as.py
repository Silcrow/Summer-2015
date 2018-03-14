# save list into xcel, after pip install XlsWriter
import xlsxwriter
ListA = ['a','b','c']

import Tkinter,tkFileDialog

root = Tkinter.Tk()
fileName = tkFileDialog.asksaveasfilename(parent=root,title="Save the image as...")
if len(fileName ) > 0:
    print "Now saving under %s" % fileName


workbook = xlsxwriter.Workbook(fileName+'.xlsx')
worksheet = workbook.add_worksheet()

row=0
col=0

for item in ListA:
	worksheet.write(row, col, item)
	row +=1

workbook.close()