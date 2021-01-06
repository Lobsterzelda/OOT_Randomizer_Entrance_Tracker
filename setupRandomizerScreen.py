from tkinter import *
from tkinter.filedialog import asksaveasfilename
from OOT_Locations_Graph import *

try:
	from tkmacosx import *
except:
	pass


class setupRandomizerScreen:
	def __init__(self, root):
		self.myFileName = ""
		self.gui = Toplevel()
		self.root = root
		self.gui.title("Create New Randomizer")
		self.gui.geometry('1200x650')
		self.decoupled = False
		self.defaultSongs = True
		self.defaultStarts = True
		self.autosaveOn = True
		self.mainLabel = Label(self.gui, text = "Select the features of your randomizer!", bg = "white", fg = "red", font = "Heveltica 32").grid(row = 0, column = 0, padx = 200, pady = (10, 0))

		self.hasDefaultStartPointsVar = IntVar(value = 1)
		Checkbutton(self.gui, text = "Has Default Start Points After Savewarping?", var = self.hasDefaultStartPointsVar, bg = "white", fg = "black", font = "Times 24 bold").grid(row = 1, column = 0, sticky = "W", padx = 200, pady = (40,0))		
		self.hasDefaultWarpSongsVar = IntVar(value = 1)
		Checkbutton(self.gui, text = "Has Default/Vanilla Warp Song Locations?", var = self.hasDefaultWarpSongsVar, font = "Times 24 bold", bg = "white", fg = "black").grid(row = 2, column = 0, sticky = "W", padx = 200, pady = 20)
		self.hasDecoupledEntrancesVar = IntVar(value = 0)
		Checkbutton(self.gui, text = "Has Decoupled Entrances?", var = self.hasDecoupledEntrancesVar, bg = "white", fg = "black", font = "Times 24 bold").grid(row = 3, column = 0, sticky = "W", padx = 200)

		self.autosaveOnVar = IntVar(value = 1)
		Checkbutton(self.gui, text = "AutoSave Turned On?", var = self.autosaveOnVar, bg = "white", fg = "black", font = "Times 24 bold").grid(row = 4, column = 0, sticky = "W", pady = 20, padx = 200)

		
		self.importantLabel = Label(self.gui, text = "IMPORTANT NOTE:", font = "Heveltica 27 bold")
		self.importantLabel.grid(row = 5, column = 0)
		self.importantLabel.configure(anchor = "center")
		self.miscLabel = Label(self.gui, text = "Make sure these settings are correct before you hit the save and create randomizer button below, as you won't be able to change these\nsettings later on. Remember: options should be checked off only if they are true. Ex. if you have the vanilla warp songs location option\nenabled in your seed, then the Has Vanilla Warp Song Locations? box should be checked off. Otherwise, it should not be checked off.", justify = LEFT).grid(row = 6, column = 0, sticky = "W", padx = 200)

		Button(self.gui, text = "Create Randomizer And Create Save File", bg = "green", fg = "white", font = "Times 30 bold", command = self.saveFile).grid(row = 7, column = 0, sticky = "W", pady = 30, padx = 200)
		
		
		self.gui.protocol("WM_DELETE_WINDOW", self.removePopup)
		self.gui.mainloop()

	def removePopup(self):
		self.root.popUpLoaded = False
		self.gui.destroy()
		self.gui.quit()

	def saveFile(self):
		self.myFileName = ""	
		self.myFileName = asksaveasfilename(initialdir = '.')	
		if self.myFileName.strip() != "":
			try:
				self.defaultStarts = bool(self.hasDefaultStartPointsVar.get())
				self.defaultSongs = bool(self.hasDefaultWarpSongsVar.get())
				self.decoupled = bool(self.hasDecoupledEntrancesVar.get())
				self.autosaveOn = bool(self.autosaveOnVar.get())
				myOOTGraph = OOT_Locations_Graph(decoupled = self.decoupled, defaultStarts = self.defaultStarts, defaultSongs = self.defaultSongs, autoSave = self.autosaveOn)
				newFileObj = open(self.myFileName, "w")
				newFileObj.close()
				if myOOTGraph.writeDataToFile(self.myFileName) != 0:
					messagebox.showerror("Error", "Error occured writing to file. Please check that you have entered in a valid file name and that you have permission to create a file in this directory", icon = "warning")
					return
				self.root.defaultStarts = self.defaultStarts
				self.root.defaultSongs = self.defaultSongs
				self.root.decoupled = self.decoupled
				self.root.autosaveEnabled = self.autosaveOn
				self.root.fileName = self.myFileName
				self.root.coreLoadRandoFunction()
			except Exception as e:
				messagebox.showerror("Error", "Error occured writing to file. Please check that you have entered in a valid file name and that you have permission to create a file in this directory", icon = "warning")
				print(e)
				return

		self.root.popUpLoaded = False
		self.root.parent.readyForMainMapScreen = True
		self.gui.destroy()
		self.gui.quit()
