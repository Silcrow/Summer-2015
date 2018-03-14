
from Tkinter import *

root = Tk()

def name():
	import Tkinter,tkFileDialog
	root = Tkinter.Tk()
	filename = tkFileDialog.askopenfilename(parent=root,title='Choose a file')
	# print "I got " + (str(filename))
	display.insert(END, filename)
	
button = Button(root, text="Browse", command= name)
button.pack()

display = Text(root, height=8, width=30)
S = Scrollbar(root)
display.pack(side=LEFT, fill=Y)
S.pack(side=RIGHT, fill=Y)
S.config(command=display.yview)
display.config(yscrollcommand=S.set)


root.mainloop()