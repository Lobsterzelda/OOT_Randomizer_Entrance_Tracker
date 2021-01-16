from tkinter import *

try:
	from tkmacosx import *
except:
	pass

from OOT_Locations_Graph import *

class spawnScreen():
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
		self.OOT_Graph = self.parentScreen.controller.OOT_Graph
		#self.OOT_Graph = OOT_Locations_Graph(False, False, False, False)
		#self.OOT_Graph.childStartID = 5
		self.gui = Toplevel(bg = "white")
		self.gui.title("Set Spawn Points")
		self.topFrame = Frame(self.gui, bg = "white")
		self.topFrame.grid(row = 0, column = 0)
		self.mainLabel = Label(self.topFrame, text = "Select Your Age Properties:", fg = "red", bg = "white", font = "Heveltica 32 bold")
		self.mainLabel.grid(row = 0, column = 0, sticky = W, padx = (300, 300))	

		self.mainFrame = Frame(self.gui, bg = "white")
		self.mainFrame.grid(row = 1, column = 0, sticky = W)

		temp = 0
		if self.OOT_Graph.isChild:
			temp = 1
		self.isChildVar = IntVar(value = temp)

		self.childCheckbox = Checkbutton(self.mainFrame, var = self.isChildVar, text = "Is Child? ", bg = "white", fg = "red", font = "Heveltica 20 bold")
		self.childCheckbox.grid(row = 0, column = 0, padx = (20, 20), pady = (20, 20), sticky = W)

		self.spawnList = [
		['Child Spawn Point:', Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue", fg = "white")],

		['Adult Spawn Point:', Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue", fg = "white")]
		]



		index = 1
		for element in self.spawnList:
			myName = element[0]
			Label(self.mainFrame, text = myName, font = "Heveltica 24 bold", bg = "#ccffcc").grid(row = index, column = 0, padx = (20, 20), sticky = W)
			extraString = " -------------------------- "

			if(myName == 'Child Spawn Point:' and self.OOT_Graph.childStartID != -1):
				extraString = self.OOT_Graph.ID_to_string_dictionary[self.OOT_Graph.childStartID]
			elif(myName == 'Adult Spawn Point:' and self.OOT_Graph.adultStartID != -1):
				extraString = self.OOT_Graph.ID_to_string_dictionary[self.OOT_Graph.adultStartID]

			Label(self.mainFrame, text = extraString, font = "Heveltica 24 bold", bg = "#ccffcc").grid(row = index, column = 1, padx = (0, 20), pady = 30, sticky = W)

			if self.OOT_Graph.isDefaultStartPoints == False:
				element[1].grid(row = index, column = 2, padx = (0, 20), sticky = W)
				if(myName == 'Child Spawn Point:' and self.OOT_Graph.childStartID != -1):
					element[2].grid(row = index, column = 3, padx = (0, 20), sticky = W)
				elif(myName == 'Adult Spawn Point:' and self.OOT_Graph.adultStartID != -1):
					element[2].grid(row = index, column = 3, padx = (0, 20), sticky = W)

			index += 1

		self.saveButton = Button(self.mainFrame, text = "Confirm Changes", bg = "orange", fg = "white")
		self.saveButton.grid(row = index, column = 0, padx = (0, 50), pady = (50, 50))

		self.cancelButton = Button(self.mainFrame, text = "Cancel", bg = "orange", fg = "white")
		self.cancelButton.grid(row = index, column = 1, padx = (0, 20))




if __name__ == '__main__':
	spawnScreen(None)

			




		
