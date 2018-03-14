def whichSelected():
    print "At %s of %d" % (select.curselection(), len(phonelist))
    return int(select.curselection()[0])

def addEntry():
    phonelist.append ([nameVar.get(), phoneVar.get()])
    setSelect()

def updateEntry() :
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect()

def deleteEntry():
    del phonelist[whichSelected()]
    setSelect()

def loadEntry():
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

 def setSelect():
	phonelist.sort()
	select.delete(0,END)
	for name,phone in phonelist:
		select.insert(END, name)

