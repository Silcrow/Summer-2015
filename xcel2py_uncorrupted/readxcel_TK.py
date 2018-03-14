from Tkinter import *
import xlrd

win = Tk()
win.title("Excel-Python")

def execute():
	file_location = unicode(str(locationVar.get()))
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index((int(sheetVar.get())-1))
	col = int(colVar.get())
	# col =0
	for row in range(sheet.nrows):
		print sheet.cell_value(row, col)
		display.insert(END, sheet.cell_value(row, col))
		display.insert(END, "\n")



frame1 = Frame(win)
frame1.pack()

Label(frame1, text="File Location").grid(row=0, column=0, sticky=W)
locationVar = StringVar()
location = Entry(frame1, textvariable=locationVar)
location.grid(row=0, column=1, sticky=W)

Label(frame1, text="Sheet Number").grid(row=1, column=0, sticky=W)
sheetVar= StringVar()
sheet= Entry(frame1, textvariable=sheetVar)
sheet.grid(row=1, column=1, sticky=W)

Label(frame1, text="Designated Column").grid(row=2, column=0, stick=W)
colVar= StringVar()
col= Entry(frame1, textvariable=colVar)
col.grid(row=2, column=1, sticky=W)

frame2 = Frame(win)
frame2.pack()
b1 = Button(frame2,text="Execute", command = execute)
b1.pack()
Label(frame2, text="Designation will display below").pack()

frame3 = Frame(win)
frame3.pack()
display = Text(frame3, height =4, width=50)
display.grid(row=2, column=1, sticky=W)

win.mainloop()