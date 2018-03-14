from Tkinter import Tk, StringVar, Entry, Button


class calculator:

	def __init__(self):
		self.error=True
		window = Tk()
		window.title("Tub_Calculator")
		window.configure(background='orange')

		self.string = StringVar()
		entry = Entry(window, textvariable = self.string, font = "Helvetica 17 bold")
		entry.grid(row=0, column=0,columnspan=6)
		entry.bind('<KeyPress>', self.keyPress)
		entry.focus()

		values = ["7", "8", "9", "/", "Clear", "<-", "4", "5", "6", "*","(",")","1","2","3","-","=","0",".","%","+"]

		i=0
		row=1
		col=0
		for txt in values:
			padx=10
			pady=10

			if(i==6):
				row=2
				col=0
			if(i==12):
				row=3
				col=0
			if(i==17):
				col=0
				row=4

			if(txt=="="):
				btn = Button(window, height = 1, width = 2, padx=23, pady=23, text=txt,
								command = lambda txt=txt:self.equals())
				btn.grid(row=row, column=col, columnspan=2, rowspan=2, padx=1, pady=1)
			elif(txt=="Clear"):
				btn = Button(window, height = 1, width = 2, padx=padx, pady=pady, text=txt,
								command = lambda txt=txt:self.clearTxt())
				btn.grid(row=row, column=col, padx=1, pady=1)
			elif(txt=="<-"):
				btn = Button(window, height = 1, width = 2, padx=padx, pady=pady, text=txt,
					command = lambda txt=txt:self.delete())
				btn.grid(row=row, column=col, padx=1, pady=1)
			else:
				btn = Button(window, height = 1, width = 2, padx=padx, pady=pady, text=txt,
							command = lambda txt=txt:self.addChar(txt))
				btn.grid(row=row, column=col, padx=1, pady=1)

			col=col+1
			i=i+1

		window.mainloop()

	def keyPress(self, event):

		allowedValues = ["KP_0","KP_1", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8",
		"KP_9", "7", "8", "9", "KP_Divide", "slash", "4", "5", "6", "KP_Multiply", "parenleft", "parenright",
		"1","2","3","KP_Subtract","minus","equal","0","period","percent","KP_Add","plus","BackSpace","asterisk",
		"Right","Left","KP_Decimal"] 

		if(not self.error):
			if event.keysym in("Return", "KP_Enter"):
				self.equals()
			elif event.keysym not in allowedValues:
				return 'break'
		else:
			return 'break'
	def clearTxt(self):
		self.string.set("")
		self.error = False
	def equals(self):
		result=""

		try: # execute like normal, but if fail execute what's under 'except'
			result=eval(self.string.get())
		except:
			self.error=True
			result= "Error"
		self.string.set(result)
	def addChar(self, char):
		if(not self.error):
			self.string.set(self.string.get() + (str(char)))
	def delete(self):
		if(not self.error):
			self.string.set(self.string.get()[0:-1]) # del the last char of string

calculator()		

''' 2/7/15 learned: 
introduces Python's documentation of new keywords and function = Button,StringVar, Entry...
	unclear understanding of "command = lambda txt=txt:self.equals()"
demonstrates using Tkinter GUI
using for loop to align widgets'''
