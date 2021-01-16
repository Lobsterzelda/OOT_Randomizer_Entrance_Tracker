from tkinter import *

try:
	from tkmacosx import *
except:
	pass

from OOT_Locations_Graph import *

class viewScreen():
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
		self.OOT_Graph = self.parentScreen.controller.OOT_Graph
		#self.OOT_Graph = OOT_Locations_Graph(False, False, True, True)
		self.gui = Toplevel(bg = "white")
		self.topFrame = Frame(self.gui)
		self.topFrame.grid(row = 0, column = 0, sticky = NSEW)
		self.mainLabel = Label(self.topFrame, text = "View/Edit Randomizer Properties:", font = "Heveltica 32 bold", fg = "red")
		self.mainLabel.grid(row = 0, column = 0, sticky = NSEW, padx = (400, 400))
		self.gui.columnconfigure(0, weight = 1)		

		self.mainFrame = Frame(self.gui, bg = "white")
		self.mainFrame.grid(row = 1, column = 0, sticky = W)

		extraString = "False"
		if self.OOT_Graph.isDecoupled:
			extraString = "True"

		self.decoupledLabel = Label(self.mainFrame, text = "Entrances Decoupled?                                  ------------------------------                 " + extraString, fg = "black", bg = "white", font = "Heveltica 20 bold")
		self.decoupledLabel.grid(row = 0, column = 0, sticky = W, padx = (20, 0), pady = (10, 20))

		extraString = "False"
		if self.OOT_Graph.isDefaultStartPoints:
			extraString = "True"


		self.startLabel = Label(self.mainFrame, text = "Default Start Locations?                              ------------------------------                 " + extraString, fg = "black", bg = "white", font = "Heveltica 20 bold")
		self.startLabel.grid(row = 1, column = 0, sticky = W, padx = (20, 0), pady = (0, 20))


		extraString = "False"
		if self.OOT_Graph.isDefaultSongs:
			extraString = "True"

		self.songLabel = Label(self.mainFrame, text = "Default Warp Song Destinations?           ------------------------------                 " + extraString, fg = "black", bg = "white", font = "Heveltica 20 bold")
		self.songLabel.grid(row = 2, column = 0, sticky = W, padx = (20, 0), pady = (0, 20))


		temp = 0
		if self.OOT_Graph.isAutosaveOn:
			temp = 1
		self.autosaveVar = IntVar(value = temp)

		self.autosaveCheckbox = Checkbutton(self.mainFrame, text = " Autosave On?", var = self.autosaveVar, bg = "white", fg = "red", font = "Times 20 bold")
		self.autosaveCheckbox.grid(row = 3, column = 0, sticky = W, padx = (20, 0), pady = (0, 20))

		temp = 0
		if self.OOT_Graph.isChild:
			temp = 1
		self.childVar = IntVar(value = temp)

		self.childCheckbox = Checkbutton(self.mainFrame, text = " Is Currently A Child?", var = self.childVar, bg = "white", fg = "red", font = "Times 20 bold")
		self.childCheckbox.grid(row = 4, column = 0, sticky = W, padx = (20, 0), pady = (0, 20))

		temp = 0
		if self.OOT_Graph.hasTempleOfTimeAccess:
			temp = 1
		self.templeAccessVar = IntVar(value = temp)

		self.templeCheckbox = Checkbutton(self.mainFrame, text = " Has Access to Temple Of Time?", var = self.templeAccessVar, bg = "white", fg = "red", font = "Times 20 bold")
		self.templeCheckbox.grid(row = 5, column = 0, sticky = W, padx = (20, 0), pady = (0, 20))


		self.saveButton = Button(self.mainFrame, text = "Confirm Changes", bg = "blue", fg = "white", font = "Heveltica 18 bold")
		self.saveButton.grid(row = 6, column = 0, sticky = W, padx = (20, 0), pady = (30, 30))

		self.cancelButton = Button(self.mainFrame, text = "Cancel", bg = "blue", fg = "white", font = "Heveltica 18 bold")
		self.cancelButton.grid(row = 6, column = 1, sticky = W, padx = (20, 0), pady = (30, 30))



if __name__ == '__main__':
	viewScreen(None)
