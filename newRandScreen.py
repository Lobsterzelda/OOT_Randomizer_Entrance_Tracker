from tkinter import *

try:
	from tkmacosx import *
except:
	pass


class newRandScreen():
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
		self.gui = Toplevel()
		self.gui.title("Create New Randomizer")
		self.gui.geometry('1200x650')
		self.decoupled = False	
		self.defaultSongs = False
		self.defaultStarts = False
		self.autosaveOn = True
		
		self.mainLabel = Label(self.gui, text = "Select the features of your randomizer!", bg = "white", fg = "red", font = "Heveltica 32").grid(row = 0, column = 0, padx = 200, pady = (10, 0))

		self.hasDefaultStartPointsVar = IntVar(value = 1)
		self.fir = Checkbutton(self.gui, text = "Has Default Start Points After Savewarping?", var = self.hasDefaultStartPointsVar, bg = "white", fg = "black", font = "Times 24 bold")
		self.fir.grid(row = 1, column = 0, sticky = "W", padx = 200, pady = (40, 0))

		self.hasDefaultWarpSongsVar = IntVar(value = 1)
		self.sec = Checkbutton(self.gui, text = "Has Default/Vanilla Warp Song Locations?", var = self.hasDefaultWarpSongsVar, font = "Times 24 bold", bg = "white", fg = "black",)
		self.sec.grid(row = 2, column = 0, sticky = "W", padx = 200, pady = 20)

		self.hasDecoupledEntrancesVar = IntVar(value = 0)
		self.thir = Checkbutton(self.gui, text = "Has Decoupled Entrances?", var = self.hasDecoupledEntrancesVar, bg = "white", fg = "black", font = "Times 24 bold")
		self.thir.grid(row = 3, column = 0, sticky = "W", padx = 200)

		self.autosaveOnVar = IntVar(value = 1)
		self.four = Checkbutton(self.gui, text = "Autosave Turned On?", var = self.autosaveOnVar, bg = "white", fg = "black", font = "Times 24 bold")
		self.four.grid(row = 4, column = 0, sticky = "W", pady = 20, padx = 200)



		self.importantLabel = Label(self.gui, text = "IMPORTANT NOTE:", font = "Heveltica 27 bold")
		self.importantLabel.grid(row = 5, column = 0)
		self.importantLabel.configure(anchor = "center")
		self.miscLabel = Label(self.gui, text = "Make sure these settings are correct before you hit the save and create randomizer button below, as you won't be able to change these\nsettings later on. Remember: options should be checked off only if they are true. Ex. if you have the vanilla warp songs location option\nenabled in your seed, then the Has Vanilla Warp Song Locations? box should be checked off. Otherwise, it should not be checked off.", justify = LEFT).grid(row = 6, column = 0, sticky = "W", padx = 200) 
 
		self.saveButton = Button(self.gui, text = "Create Randomizer And Create Save File", bg = "green", fg = "white", font = "Times 30 bold")
		self.saveButton.grid(row = 7, column = 0, sticky = "W", pady = 30, padx = 200)

