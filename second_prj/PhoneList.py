from Tkinter import *

win = Tk()

name_list =[]
phone_list =[] # will change to textbox later

def addEntry():
	if nameVar.get() in name_list:
		display.insert(END, " name is already in list ")
		return
	else:
	    name_list.append(nameVar.get())
	    phone_list.append(phoneVar.get())
	    select.insert(END, nameVar.get())
	    display.insert(END, name_list)
	    display.insert(END, phone_list)
	    							# if curselection not found, display!!!

def loadEntry(): 						# change to autoLoad onclick!!!
    nameVar.set(name_list[select.curselection()[0]])
    phoneVar.set(phone_list[select.curselection()[0]])
    											# if curselection not found, display!!!

def deleteList():
	name_list.remove(name_list[select.curselection()[0]])
	phone_list.remove(phone_list[select.curselection()[0]])
	select.delete(select.curselection()[0])
	display.insert(END, name_list)
	display.insert(END, phone_list)
								# if curselection not found, display!!!

def updateEntry():
	name_list[select.curselection()[0]] = nameVar.get()
	phone_list[select.curselection()[0]] = phoneVar.get()
	select.insert(select.curselection()[0], nameVar.get())
	select.delete(select.curselection()[0])
	display.insert(END, name_list)
	display.insert(END, phone_list)
    							# if curselection not found, display!!!

frame1 = Frame(win)
frame1.pack()

Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
nameVar = StringVar()
name = Entry(frame1, textvariable=nameVar)
name.grid(row=0, column=1, sticky=W)

Label(frame1, text="Phone").grid(row=1, column=0, sticky=W)
phoneVar= StringVar()
phone= Entry(frame1, textvariable=phoneVar)
phone.grid(row=1, column=1, sticky=W)

Label(frame1, text="Display").grid(row=2, column=0, sticky=W)
display = Text(frame1, height =4, width=50)
display.grid(row=2, column=1, sticky=W)

frame2 = Frame(win)       # Row of buttons
frame2.pack()
b1 = Button(frame2,text=" Add  ", command = addEntry)
b2 = Button(frame2,text="Update", command = updateEntry)
b3 = Button(frame2,text="Delete", command = deleteList)
b4 = Button(frame2, text="Load", command = loadEntry)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)

frame3 = Frame(win)       # select of names
frame3.pack()

scroll = Scrollbar(frame3, orient=VERTICAL)
select = Listbox(frame3, height=6)

scroll.config(command=select.yview)
select.config(yscrollcommand=scroll.set)

scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


win.mainloop()
