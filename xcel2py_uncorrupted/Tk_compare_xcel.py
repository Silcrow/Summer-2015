from Tkinter import *
import xlrd

win = Tk()
win.title("Excel-Python")

ListA = []

def make_excel():
	import Tkinter,tkFileDialog
	fileName = tkFileDialog.asksaveasfilename(parent=win,title="Save the image as...")
	if len(fileName ) > 0:
		print "Now saving under %s" % fileName

	import xlsxwriter
	workbook = xlsxwriter.Workbook(fileName + '.xlsx')
	worksheet = workbook.add_worksheet()

	row=0
	col=0

	for item in ListA:
		worksheet.write(row, col, item)
		row +=1

	workbook.close()


def get_locationA():
	locationA.delete(0,END)
	import Tkinter,tkFileDialog
	filename = tkFileDialog.askopenfilename(parent=win,title='Choose a file')
	locationA.insert(END, filename)


def get_locationB():
	locationB.delete(0,END)
	import Tkinter,tkFileDialog
	filename = tkFileDialog.askopenfilename(parent=win,title='Choose a file')
	locationB.insert(END, filename)


def execute():
	display.delete('1.0',END)
	ListB = []

	try:
		file_locationA = unicode(str(locationVarA.get()))
		workbookA = xlrd.open_workbook(file_locationA)
	except:
		display.insert(END, "finding file location A results in error")
		return
	if not sheetVarA.get():
		display.insert(END, "please fill in sheet A")
		return
	if int(sheetVarA.get()) <= int(workbookA.nsheets) and int(sheetVarA.get()) > 0:
		sheetA = workbookA.sheet_by_index((int(sheetVarA.get())-1))
	else:
		display.insert(END, "sheet A does not exist")
		return
	if not colVarA.get():
		display.insert(END, "please fill in column A")
		return
	if int(colVarA.get()) <= int(sheetA.ncols) and int(colVarA.get()) > 0:
		colA = int(colVarA.get())-1
	else:
		display.insert(END, "column A is empty")
		return

	try:
		file_locationB = unicode(str(locationVarB.get()))
		workbookB = xlrd.open_workbook(file_locationB)
	except:
		display.insert(END, "finding file location B results in error")
		return
	if not sheetVarB.get():
		display.insert(END, "please fill in sheet B")
		return
	if int(sheetVarB.get()) <= int(workbookB.nsheets) and int(sheetVarB.get()) > 0:
		sheetB = workbookB.sheet_by_index((int(sheetVarB.get())-1))
	else:
		display.insert(END, "sheet B does not exist")
		return
	if not colVarB.get():
		display.insert(END, "please fill in column B")
		return
	if int(colVarB.get()) <= int(sheetB.ncols) and int(colVarB.get()) > 0:
		colB = int(colVarB.get())-1
	else:
		display.insert(END, "column B is empty")
		return

	print "bookA sheets: ", workbookA.nsheets
	print "bookB sheets: ", workbookB.nsheets
	print "sheetA columns: ", sheetA.ncols
	print "sheetB columns: ", sheetB.ncols

	for rowA in range(sheetA.nrows):
		ListA.append(sheetA.cell_value(rowA, colA)) # if cell_value empty have append " "
	for rowB in range(sheetB.nrows):
		ListB.append(sheetB.cell_value(rowB, colB))
	for B in ListB:
		for A in ListA:
			if B==A:
				ListA.remove(A)
				break
	for a in ListA:
		display.insert(END, a)
		display.insert(END, "\n")

frame1 = Frame(win)
frame1.pack()

Label(frame1, text="Excel A").grid(row=0, column=0, sticky=W)
Label(frame1, text="File Path").grid(row=1, column=0, sticky=W)
locationVarA = StringVar()
locationA = Entry(frame1, textvariable=locationVarA)
locationA.grid(row=1, column=1, sticky=W)

buttonA = Button(frame1, text="Browse A", command= get_locationA)
buttonA.grid(row=2, column=1, sticky=E)

Label(frame1, text="Sheet").grid(row=3, column=0, sticky=W)
sheetVarA= StringVar()
sheetA= Entry(frame1, textvariable=sheetVarA)
sheetA.grid(row=3, column=1, sticky=W)
sheetA.insert(END, "1")

Label(frame1, text="Column").grid(row=4, column=0, stick=W)
colVarA= StringVar()
colA= Entry(frame1, textvariable=colVarA)
colA.grid(row=4, column=1, sticky=W)
colA.insert(END, "1")

Label(frame1, text="Excel B").grid(row=0, column=2, sticky=W)
Label(frame1, text="File Path").grid(row=1, column=2, sticky=W)
locationVarB = StringVar()
locationB = Entry(frame1, textvariable=locationVarB)
locationB.grid(row=1, column=3, sticky=W)

buttonB = Button(frame1, text="Browse B", command=get_locationB)
buttonB.grid(row=2, column=3, sticky=E)

Label(frame1, text="Sheet").grid(row=3, column=2, sticky=W)
sheetVarB= StringVar()
sheetB= Entry(frame1, textvariable=sheetVarB)
sheetB.grid(row=3, column=3, sticky=W)
sheetB.insert(END, "1")

Label(frame1, text="Column").grid(row=4, column=2, stick=W)
colVarB= StringVar()
colB= Entry(frame1, textvariable=colVarB)
colB.grid(row=4, column=3, sticky=W)
colB.insert(END, "1")

frame2 = Frame(win)
frame2.pack()
b1 = Button(frame2,text="list A excluding B", command = execute)
b1.pack()

frame3 = Frame(win)
frame3.pack()
display = Text(frame3, height=8, width=30)
S = Scrollbar(frame3)
display.pack(side=LEFT, fill=Y)
S.pack(side=RIGHT, fill=Y)
S.config(command=display.yview)
display.config(yscrollcommand=S.set)

frame4 = Frame(win)
frame4.pack()
b2 = Button(frame2,text="Create Excel with this list", command = make_excel)
b2.pack(side=BOTTOM)

win.mainloop()