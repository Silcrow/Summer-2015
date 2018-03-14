from Tkinter import *



class Filtering:

	def __init__(self):
		root = Tk()
		root.title("Key Filtering")

		self.string = StringVar()
		e = Entry(root, textvariable=self.string)
		e.pack()
		# e.bind('<KeyPress>', self.keyPress)
		# e.focus()

		b1 = Button(root,text="Execute",command=execute)
		b1.pack()

		display = Text(root, height =4, width=50)
		display.pack()
		root.mainloop()
	def execute():
		display.insert(END, string.get())
# def keyPress(self, event):
# 		allowedValues = ["KP_0","KP_1", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8",
# 		"KP_9"]

# 		if event.keysym not in allowedValues:
# 			return 'break'
# 		else:
# 			retur

Filtering()