from tkinter import *
try:
	from tkmacosx import *
except:
	pass

from OOT_Locations_Graph import *

class reminderScreen:
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
		self.OOT_Graph = self.parentScreen.controller.OOT_Graph
		#self.OOT_Graph = OOT_Locations_Graph(True, True, True, True)
		self.gui = Toplevel()
		self.gui.title('Reminder List')
		
		self.topFrame = Frame(self.gui)
		self.topFrame.grid(row = 0, column = 0, sticky = W)
		self.topLabel = Label(self.topFrame, text = "Reminder List:", fg = "red", font = "Heveltica 32 bold")
		self.topLabel.grid(row = 0, column = 0, sticky = NSEW, padx = (600, 100))

		self.mainFrame = Frame(self.gui, bg = "white")
		self.mainFrame.grid(row = 1, column = 0, sticky = W, padx = (170, 170), pady = (50, 50))
		self.listbox = Listbox(self.mainFrame, font = "Heveltica 14", fg = "black", height = 20, width = 120, selectmode = MULTIPLE)
		self.listbox.grid(row = 0, column = 0, sticky = W, padx = (10, 0), pady = (10, 0))

		self.horizontalScroll = Scrollbar(self.mainFrame, orient = HORIZONTAL)
		self.horizontalScroll.grid(row = 1, column = 0, sticky = S)

		self.listbox.config(xscrollcommand = self.horizontalScroll.set)

		self.horizontalScroll.config(command = self.listbox.xview)


		self.verticalScroll = Scrollbar(self.mainFrame)
		self.verticalScroll.grid(row = 0, column = 1, sticky = E)
		self.listbox.config(yscrollcommand = self.verticalScroll.set)
		self.verticalScroll.config(command = self.listbox.yview)

		for myReminder in self.OOT_Graph.reminderList:
			self.listbox.insert(END, myReminder)


		self.bottomFrame = Frame(self.mainFrame, bg = "white")
		self.bottomFrame.grid(row = 2, column = 0, sticky = W, padx = (0, 170))

		self.addReminderButton = Button(self.bottomFrame, bg = "blue", fg = "white", text = "Add Reminder")
		self.addReminderButton.grid(row = 2, column = 0, sticky = W, padx = (10, 20), pady = (20, 20))

		self.deleteReminderButton = Button(self.bottomFrame, bg = "blue", fg = "white", text = "Delete Reminders")
		self.deleteReminderButton.grid(row = 2, column = 1, sticky = W, padx = (10, 20))

		self.unhighlightButton = Button(self.bottomFrame, bg = "blue", fg = "white", text = "Unhighlight All")
		self.unhighlightButton.grid(row = 2, column = 2, sticky = W, padx = (10, 20))



		self.outerFrame = Frame(self.gui)
		self.outerFrame.grid(row = 2, column = 0, sticky = W, pady = (0, 100))
		self.otherLabel = Label(self.outerFrame, text = "Enter New Reminder: ", fg = "red", font = "Heveltica 20 bold")
		self.otherLabel.grid(row = 0, column = 0, sticky = W, padx = (20, 0))


		self.reminderXScroll = Scrollbar(self.outerFrame, orient = HORIZONTAL)
		self.reminderXScroll.grid(row = 1, column = 1, sticky = N)
		
		self.reminderVar = StringVar()
		self.newReminderEntry = Entry(self.outerFrame, bg = "white", fg = "green", textvariable = self.reminderVar, width = 120)

		self.newReminderEntry.grid(row = 0, column = 1, sticky = W, padx = (20, 20))
		
		self.newReminderEntry.config(xscrollcommand = self.reminderXScroll.set)
		self.reminderXScroll.config(command = self.newReminderEntry.xview)


if __name__ == '__main__':
	reminderScreen(None)	
