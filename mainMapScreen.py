from tkinter import *
from tkinter.filedialog import *
try:
	from tkmacosx import *
except:
	pass


from mapSelectionCanvas import *
from overworldCanvas import *
from subLocationCanvas import *
from locationListCanvas import *
from newRandScreen import *
from songScreen import *
from viewScreen import *
from spawnScreen import *
from reminderScreen import *
from shortestPathScreen import *
from helpScreen import *

def donothing():
	pass

class mainMapScreen():
	def __init__(self, controller):
		self.gui = Toplevel()
		self.controller = controller
		self.gui.geometry('1420x1420')
		self.OOT_Graph = self.controller.OOT_Graph
		menuBar = Menu(self.gui)
		self.gui.config(menu=menuBar)
		self.newRoot = None
		self.newRandomizerScreen = None
		self.mySongScreen = None
		self.myViewScreen = None
		self.mySpawnScreen = None
		self.myReminderScreen = None
		self.myShortestScreen = None
		self.pathSource = ""
		self.pathDest = ""
		self.spawnType = ""
		self.lastLocation = ""
		self.sourceLocation = ""
		self.destinationLocation = ""
		self.currentSubLocation = ""
		self.currentSong = ""

		fileMenu = Menu(menuBar)
		fileMenu.add_command(label = "New Randomizer", command = self.newRando)
		fileMenu.add_command(label = "Load Randomizer", command = self.load)
		fileMenu.add_command(label = "Save", command = self.save)
		fileMenu.add_separator()
		fileMenu.add_command(label = "Exit Program", command = self.exitFunc)
		menuBar.add_cascade(label = "File", menu = fileMenu)

		songMenu = Menu(menuBar)
		songMenu.add_command(label = "Open Song Tracker", command = self.openSongs)
		menuBar.add_cascade(label = "Songs", menu = songMenu)   
        
		ageMenu = Menu(menuBar)
		ageMenu.add_command(label = "Set Age Spawn Points", command = self.openSpawn)
		menuBar.add_cascade(label = "Age", menu = ageMenu)

		viewMenu = Menu(menuBar)
		viewMenu.add_command(label = "View Current Seed Properties", command = self.openView)
		menuBar.add_cascade(label = "View", menu = viewMenu)

		reminderMenu = Menu(menuBar)
		reminderMenu.add_command(label = "Open Reminder Tracker", command = self.loadReminders)
		menuBar.add_cascade(label = "Reminders", menu = reminderMenu)

		navigationMenu = Menu(menuBar)
		navigationMenu.add_command(label = "Find Shortest Path", command = self.openShortestPath)
		menuBar.add_cascade(label = "Routing", menu = navigationMenu)

		helpMenu = Menu(menuBar)
		helpMenu.add_command(label = "Help", command = self.openHelp)
		menuBar.add_cascade(label = "Help", menu = helpMenu)		

		self.mode = "Explore"  #mode has the value 'Explore' by default, when the user hasn't done anything. The user can select a source for a connection in this mode. Other values are 'Destination', where the user needs to select a destination to make a connection to. 'PathStart' when setting a path from the source, 'PathEnd' when selecting a destination from a source. and 'Song-X', when setting the destination for a song, where X is the name of the song, and 'childStart' and 'adultStart' modes.
	
		self.gui.title("Select Map!")
		self.mainCancelButton = None
		self.myBackButton = None
		self.screenBusy = False
		self.topFrame = Frame(self.gui, relief = RIDGE, borderwidth = 0, bg = '#FFFFE0')
		self.topFrame.grid(row = 0, column = 0, sticky = N+S+E+W)
		self.mainFrame = Frame(self.gui, relief = RAISED, borderwidth = 1)
		self.mainFrame.grid(row = 1, column = 0)
		self.mainCanvas = mapSelectionCanvas(self.mainFrame, self)
		self.setMainScreenTagBindings()

		self.titleText = Label(self.topFrame, text = "Exploration Mode!", fg = "red", font = "Heveltica 32 bold", bg = '#FFFFE0')
		self.titleText.grid(row = 0, column = 1, sticky = N)
		self.topFrame.grid_rowconfigure(0, weight = 1)
		self.topFrame.grid_columnconfigure(1, weight = 1)

		self.gui.protocol("WM_DELETE_WINDOW", self.exitFunc)
		self.gui.mainloop()
	

	def openHelp(self):
		helpScreen(self)

	def openShortestPath(self):
		if self.screenBusy or self.mode != 'Explore':
			return
		self.changeModes('PathStart')
	

	def reminderClose(self):
		self.screenBusy = False
		self.gui.after(25, lambda: self.myReminderScreen.gui.destroy())

	def unhighlightReminders(self):
		self.myReminderScreen.listbox.select_clear(0, END)

	def loadReminders(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		self.myReminderScreen = reminderScreen(self)
		self.myReminderScreen.gui.protocol("WM_DELETE_WINDOW", self.reminderClose)
		self.myReminderScreen.addReminderButton.bind("<Button-1>", lambda x: self.addReminder())
		self.myReminderScreen.deleteReminderButton.bind("<Button-1>", lambda x: self.deleteReminders())
		self.myReminderScreen.unhighlightButton.bind("<Button-1>", lambda x: self.unhighlightReminders())

	
	def addReminder(self):
		newRemind = self.myReminderScreen.reminderVar.get().strip()
		if newRemind == "":
			return

		self.OOT_Graph.addReminder(newRemind)
		self.myReminderScreen.listbox.insert(END, newRemind)

		self.myReminderScreen.reminderVar.set("")

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

	
	def deleteReminders(self):

		while(len(self.myReminderScreen.listbox.curselection()) > 0):
			nextLine = self.myReminderScreen.listbox.curselection()[0]
			self.myReminderScreen.listbox.delete(nextLine)		


		self.OOT_Graph.reminderList = []
		
		for i in range(0, self.myReminderScreen.listbox.size()):
			newRemind = self.myReminderScreen.listbox.get(i)
			self.OOT_Graph.addReminder(newRemind)

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)
		

	def spawnClose(self):
		self.screenBusy = False
		self.gui.after(25, lambda: self.mySpawnScreen.gui.destroy())

	def openSpawn(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		self.mySpawnScreen = spawnScreen(self)
		self.mySpawnScreen.gui.protocol("WM_DELETE_WINDOW", self.spawnClose)
		self.mySpawnScreen.cancelButton.bind("<Button-1>", lambda x: self.spawnClose())
		for element in self.mySpawnScreen.spawnList:
			name = element[0]
			addButton = element[1]
			deleteButton = element[2]
			addButton.bind("<Button-1>", lambda x, spawnLoc = name: self.setSpawnClicked(spawnLoc))
			deleteButton.bind("<Button-1>", lambda x, spawnLoc = name: self.deleteSpawnClicked(spawnLoc))
	
		self.mySpawnScreen.saveButton.bind("<Button-1>", lambda x: self.spawnSave())



	def deleteSpawnClicked(self, spawnLoc):

		extraString = ""
		if spawnLoc == 'Child Spawn Point:':
			extraString = self.OOT_Graph.ID_to_string_dictionary[self.OOT_Graph.childStartID]
			self.OOT_Graph.childStartID = -1
		else:
			extraString = self.OOT_Graph.ID_to_string_dictionary[self.OOT_Graph.adultStartID]
			self.OOT_Graph.adultStartID = -1

		if bool(self.mySpawnScreen.isChildVar.get()):
			self.OOT_Graph.isChild = True
		else:
			self.OOT_Graph.isChild = False

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		messagebox.showinfo("Success!", "Succesfully deleted the " + self.spawnType + " savewarp location of " + extraString)
		self.screenBusy = False
		self.changeModes('Explore')
		self.spawnClose()


	def spawnSave(self):
		if bool(self.mySpawnScreen.isChildVar.get()):
			self.OOT_Graph.isChild = True
		else:
			self.OOT_Graph.isChild = False

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		self.spawnClose()


	def setSpawnClicked(self, spawnLoc):
		if spawnLoc == 'Child Spawn Point:':
			self.spawnType = "Child"
		else:
			self.spawnType = "Adult"

		if bool(self.mySpawnScreen.isChildVar.get()):
			self.OOT_Graph.isChild = True
		else:
			self.OOT_Graph.isChild = False

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		self.screenBusy = False
		self.changeModes("Spawn")
		self.spawnClose()


	def addSpawnLoc(self):
		if self.spawnType == 'Child':
			self.OOT_Graph.childStartID = self.OOT_Graph.string_to_ID_dictionary[self.lastLocation]
		else:
			self.OOT_Graph.adultStartID = self.OOT_Graph.string_to_ID_dictionary[self.lastLocation]

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		messagebox.showinfo("Success!", "Succesfully set the spawn point for " + self.spawnType)
		self.screenBusy = False
		self.changeModes('Explore')
		self.closeWindow()

	def openView(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		self.myViewScreen = viewScreen(self)
		self.myViewScreen.gui.protocol("WM_DELETE_WINDOW", self.viewClose)
		self.myViewScreen.cancelButton.bind("<Button-1>", lambda x: self.viewClose())
		self.myViewScreen.saveButton.bind("<Button-1>", lambda x: self.viewSave())

	
	def viewClose(self):
		self.screenBusy = False
		self.gui.after(25, lambda: self.myViewScreen.gui.destroy())


	def viewSave(self):
		if bool(self.myViewScreen.autosaveVar.get()):
			self.OOT_Graph.isAutosaveOn = True
		else:
			self.OOT_Graph.isAutosaveOn = False

		if bool(self.myViewScreen.childVar.get()):
			self.OOT_Graph.isChild = True
		else:
			self.OOT_Graph.isChild = False

		if bool(self.myViewScreen.templeAccessVar.get()):
			self.OOT_Graph.hasTempleOfTimeAccess = True
		else:
			self.OOT_Graph.hasTempleOfTimeAccess = False

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		self.screenBusy = False
		self.gui.after(25, lambda: self.myViewScreen.gui.destroy())			


	def closeSong(self, arg = None):
		self.screenBusy = False
		self.gui.after(25, lambda: self.mySongScreen.gui.destroy())



	#This helper function updates which songs the user owns
	def updateSongsOwnedHelper(self, args = None):
		for element in self.mySongScreen.songList:
			songName = element[0]
			truthVar = bool(element[1].get())

			if songName == 'Minuet':
				self.OOT_Graph.hasMinuet = truthVar
			elif songName == 'Bolero':
				self.OOT_Graph.hasBolero = truthVar
			elif songName == 'Serenade':
				self.OOT_Graph.hasSerenade = truthVar
			elif songName == 'Nocturne':
				self.OOT_Graph.hasNocturne = truthVar
			elif songName == 'Requiem':
				self.OOT_Graph.hasRequiem = truthVar
			elif songName == 'Prelude':
				self.OOT_Graph.hasPrelude = truthVar
			else:
				print("Error: Unknown song of " + songName + " encountered in updateSongsOwnedHelper()")
				exit(0)

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)




	#The function which opens and sets up the songs menu.
	def openSongs(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		self.mySongScreen = songScreen(self)
		self.mySongScreen.gui.protocol("WM_DELETE_WINDOW", self.closeSong)
		self.mySongScreen.cancelButton.bind("<Button-1>", self.closeSong)
		self.mySongScreen.saveButton.bind("<Button-1>", self.saveSongs)
		if self.OOT_Graph.isDefaultSongs == True:
			return

		for element in self.mySongScreen.songList:
			songName = element[0]
			addButton = element[2]
			deleteButton = element[3]
			addButton.bind("<Button-1>", lambda rect, name = songName: self.addSongLocationClicked(name))
			deleteButton.bind("<Button-1>", lambda rect, name = songName: self.deleteSongLocationClicked(name))

	def addSongLocationClicked(self, songName):
		self.currentSong = songName
		self.screenBusy = False
		self.updateSongsOwnedHelper()
		self.changeModes('Song')
		self.gui.after(25, lambda: self.mySongScreen.gui.destroy())

	def deleteSongLocationClicked(self, songName):
		if songName == 'Minuet':
			self.OOT_Graph.minuetID = -1
		elif songName == 'Bolero':
			self.OOT_Graph.boleroID = -1
		elif songName == 'Serenade':
			self.OOT_Graph.serenadeID = -1
		elif songName == 'Nocturne':
			self.OOT_Graph.nocturneID = -1
		elif songName == 'Requiem':
			self.OOT_Graph.requiemID = -1
		elif songName == 'Prelude':
			self.OOT_Graph.preludeID = -1
		else:
			print("Error: unknown song named " + songName + " in deleteSongLocationClicked()")
			exit(1)

		self.updateSongsOwnedHelper()
		
		self.gui.after(25, lambda: self.mySongScreen.gui.destroy())
		messagebox.showinfo("Success!", "Succesfully deleted " + songName + " destination!")
		self.screenBusy = False
	

	#This function saves which songs the user has when they click "save changes." It also closes the song window.
	def saveSongs(self, arg = None):
		for element in self.mySongScreen.songList:
			name = element[0]
			truthValue = bool(element[1].get())
			if name == 'Minuet':
				self.OOT_Graph.hasMinuet = truthValue
			elif name == 'Bolero':
				self.OOT_Graph.hasBolero = truthValue
			elif name == 'Serenade':
				self.OOT_Graph.hasSerenade = truthValue
			elif name == 'Nocturne':
				self.OOT_Graph.hasNocturne = truthValue
			elif name == 'Requiem':
				self.OOT_Graph.hasRequiem = truthValue
			elif name == 'Prelude':
				self.OOT_Graph.hasPrelude = truthValue

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)	

		self.screenBusy = False
		self.gui.after(25, lambda: self.mySongScreen.gui.destroy())
		

	def addSongDest(self):
		destID = self.OOT_Graph.string_to_ID_dictionary[self.lastLocation]

		if self.currentSong == 'Minuet':
			self.OOT_Graph.minuetID = destID
		elif self.currentSong == 'Bolero':
			self.OOT_Graph.boleroID = destID
		elif self.currentSong == 'Serenade':
			self.OOT_Graph.serenadeID = destID
		elif self.currentSong == 'Nocturne':
			self.OOT_Graph.nocturneID = destID
		elif self.currentSong == 'Requiem':
			self.OOT_Graph.requiemID = destID
		elif self.currentSong == 'Prelude':
			self.OOT_Graph.preludeID = destID

		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		messagebox.showinfo("Success!", "Succesfully set destination of " + self.currentSong)
		self.closeWindow()
		self.changeModes('Explore')	


	def save(self):
		if self.screenBusy:
			return
		self.OOT_Graph.writeDataToFile(self.controller.fileName)




	def closeNewWind(self):
		self.newRandomizerScreen.gui.destroy()
		self.screenBusy = False

	def newRando(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		self.newRandomizerScreen = newRandScreen(self)
		self.newRandomizerScreen.gui.protocol("WM_DELETE_WINDOW", self.closeNewWind)
		self.newRandomizerScreen.saveButton.bind("<Button-1>", self.createNewButton)


	#This function is a helper function which creates a new Rando file when the user hits the "Create New Randomizer" button
	def createNewButton(self, args):
		tempFile = ""
		tempFile = asksaveasfilename(initialdir = '.')
		if tempFile.strip() == "":
			return

		try:
			defaultStarts = bool(self.newRandomizerScreen.hasDefaultStartPointsVar.get())
			defaultSongs = bool(self.newRandomizerScreen.hasDefaultWarpSongsVar.get())	
			decoupled = bool(self.newRandomizerScreen.hasDecoupledEntrancesVar.get())
			
			autosaveOn = bool(self.newRandomizerScreen.autosaveOnVar.get())
			myOOTGraph = OOT_Locations_Graph(decoupled = decoupled, defaultStarts = defaultStarts, defaultSongs = defaultSongs, autoSave = autosaveOn)
			newFileObj = open(tempFile, "w")
			newFileObj.close()
			if myOOTGraph.writeDataToFile(tempFile) != 0:
				messagebox.showerror("Error", "Error occured writing to file. Please check that you have entered in a valid file name and that you have permission to create a file in this directory", icon = "warning")
				return
			self.OOT_Graph = myOOTGraph
			self.controller.OOT_Graph = myOOTGraph
			self.controller.fileName = tempFile
			messagebox.showinfo("Success!", "New file succesfully created!")
			self.screenBusy = False
			self.mainCanvas.destroy()
			self.mainCanvas = mapSelectionCanvas(self.mainFrame, self)
			self.setMainScreenTagBindings()	
			self.changeModes("Explore")
			self.gui.after(25, lambda: self.newRandomizerScreen.gui.destroy())
		except Exception as e:
			messagebox.showerror("Error", "Error occured writing to file. Please check that you have entered in a valid file name and that you have permission to create a file in this directory", icon = "warning")
			print(e)
			return

	def exitFunc(self):
		if self.screenBusy:
			return
		exit(0)


	def load(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		tempFileName = askopenfilename()
		if tempFileName.strip() == "":
			messagebox.showerror("Invalid File Name", "Invalid File Name! Please try again...")
			self.screenBusy = False
			return
		tempOOTGraph = OOT_Locations_Graph(True, True, True, True)
		try:
			if tempOOTGraph.readDataFromFile(tempFileName) != 0:
				messagebox.showerror("Invalid File Format", "Error: The file you selected was not properly formatted. Please try again!")
				self.screenBusy = False
				return

			else:
				messagebox.showinfo("Success!", "Randomzier data file succesfully launched!", icon = "info")
				self.controller.OOT_Graph = tempOOTGraph
				self.OOT_Graph = tempOOTGraph
				self.controller.fileName = tempFileName
				self.mainCanvas.destroy()
				self.mainFrame.destroy()
				self.mainFrame = Frame(self.gui, relief = RAISED, borderwidth = 1)
				self.mainFrame.grid(row = 1, column = 0)
				self.mainCanvas = mapSelectionCanvas(self.mainFrame, self)
				self.setMainScreenTagBindings()
				self.screenBusy = False
				self.changeModes("Explore")
				return
				
		except Exception as e:
			messagebox.showerror("Invalid File", "Error: The file you selected was not found or could not be opened. Please check the name of the file you selected and try again.")
			self.screenBusy = False
			return


	def setMainScreenTagBindings(self):
		self.mainCanvas.tag_bind("overworldButton", "<Button-1>", self.overworldLoad)
		self.mainCanvas.tag_bind("overworldText", "<Button-1>", self.overworldLoad)
		self.mainCanvas.tag_bind("dungeonButton", "<Button-1>", self.dungeonLoad)
		self.mainCanvas.tag_bind("dungeonText", "<Button-1>", self.dungeonLoad)
		self.mainCanvas.tag_bind("grottosButton", "<Button-1>", self.grottoLoad)
		self.mainCanvas.tag_bind("grottosText", "<Button-1>", self.grottoLoad)
		self.mainCanvas.tag_bind("housesButton", "<Button-1>", self.houseLoad)
		self.mainCanvas.tag_bind("housesText", "<Button-1>", self.houseLoad)


	def dungeonLoad(self, args):
		self.genericLoad("Dungeon")

	def grottoLoad(self, args):
		self.genericLoad("Grotto")

	def houseLoad(self, args):
		self.genericLoad("House")


	def genericLoad(self, locType):
		if self.screenBusy:
			return
		self.mainCanvas.destroy()
		self.mainFrame.destroy()
		self.mainFrame = Frame(self.gui, relief = RAISED, borderwidth = 1)
		self.mainFrame.grid(row = 1, column = 0)
		self.mainCanvas = locationListCanvas(self.mainFrame, self, locType)
		for rectID in self.mainCanvas.rect_ID_to_string_dictionary:
			self.mainCanvas.tag_bind(rectID, "<Button-1>", lambda x, name = self.mainCanvas.rect_ID_to_string_dictionary[rectID]: self.loadInfoRectangle(name))
	
		for textID in self.mainCanvas.text_ID_to_string_dictionary:
			self.mainCanvas.tag_bind(textID, "<Button-1>", lambda x, name = self.mainCanvas.text_ID_to_string_dictionary[textID]: self.loadInfoRectangle(name))	
		if self.myBackButton is not None:
			self.myBackButton.grid_forget()
		self.myBackButton = Button(self.topFrame, text = "Back", bg = "blue", fg = "white", command = self.goBackFromOverworld)
		self.myBackButton.grid(row = 0, column = 0, sticky = W, padx = (10, 0))





	def goBackFromOverworld(self):
		if self.screenBusy:
			return
		self.screenBusy = True
		self.mainCanvas.destroy()
		self.mainCanvas = mapSelectionCanvas(self.mainFrame, self)
		self.myBackButton.grid_forget()
		self.setMainScreenTagBindings()
		self.screenBusy = False

	def overworldLoad(self, args):
		if self.screenBusy == False:
			self.screenBusy = True
			self.mainCanvas.destroy()
			self.mainFrame.destroy()
			self.mainFrame = Frame(self.gui, relief = RAISED, borderwidth = 1)
			self.mainFrame.grid(row = 1, column = 0)
			self.mainCanvas = overworldCanvas(self.mainFrame, self)
			self.gui.title("Select a Location!")
			
			self.myBackButton = Button(self.topFrame, text = "Back", bg = "blue", fg = "white", command = self.goBackFromOverworld)
			self.myBackButton.grid(row = 0, column = 0, sticky = W, padx = (10, 0))

			self.mainCanvas.tag_bind("hyruleField", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.hyruleFieldRect))
			self.mainCanvas.tag_bind("lonLonRanch", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.lonLonRect))
			self.mainCanvas.tag_bind("gerudoValley", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.gerudoValleyRect))
			self.mainCanvas.tag_bind("gerudosFortress", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.gerudosFortressRect))
			self.mainCanvas.tag_bind("hauntedWasteland", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.hauntedWastelandRect))
			self.mainCanvas.tag_bind("desertColossus", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.desertColossusRect))
			self.mainCanvas.tag_bind("lakeHylia", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.lakeHyliaRect))
			self.mainCanvas.tag_bind("marketEntryway", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.marketEntrywayRect))
			self.mainCanvas.tag_bind("market", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.marketRect))
			self.mainCanvas.tag_bind("templeOfTimeEntryway", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.ToTEntrywayRect))
			self.mainCanvas.tag_bind("templeOfTime", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.ToTRect))
			self.mainCanvas.tag_bind("castle", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.castleRect))
			self.mainCanvas.tag_bind("ganon", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.ganonRect))
			self.mainCanvas.tag_bind("kokiriForest", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.kokiriRect))
			self.mainCanvas.tag_bind("lostWoods", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.lostWoodsRect))
			self.mainCanvas.tag_bind("sacredForestMeadow", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.sacredForestRect))
			self.mainCanvas.tag_bind("kakariko", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.kakarikoRect))
			self.mainCanvas.tag_bind("zorasRiver", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.zorasRiverRect))
			self.mainCanvas.tag_bind("graveyard", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.graveyardRect))
			self.mainCanvas.tag_bind("zorasDomain", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.zorasDomainRect))
			self.mainCanvas.tag_bind("zorasFountain", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.zorasFountainRect))
			self.mainCanvas.tag_bind("dmt", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.dmtRect))
			self.mainCanvas.tag_bind("goronCity", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.goronCityRect))
			self.mainCanvas.tag_bind("dmc", "<Button-1>", lambda rect: self.rectangleClicked(self.mainCanvas.dmcRect))
			self.screenBusy = False
	
	def goBackFromSubLocation(self):
		if self.screenBusy:
			return
		self.myBackButton.grid_forget()
		self.overworldLoad(self)

	def loadSubLocation(self, locName):
		self.currentSubLocation = locName
		self.mainCanvas.destroy()
		self.mainFrame.destroy()
		self.mainFrame = Frame(self.gui, relief = RAISED, borderwidth = 1)
		self.mainFrame.grid(row = 1, column = 0)
		self.mainCanvas = subLocationCanvas(self.mainFrame, self, locName)
		self.myBackButton.grid_forget()
		self.myBackButton = Button(self.topFrame, text = "Back", bg = "blue", fg = "white", command = self.goBackFromSubLocation)
		self.myBackButton.grid(row = 0, column = 0, sticky = W, padx = (10, 0))

		for rectID in self.mainCanvas.rect_ID_to_string_dictionary:
			self.mainCanvas.tag_bind(rectID, '<Button-1>', lambda x, name = self.mainCanvas.rect_ID_to_string_dictionary[rectID]: self.loadInfoRectangle(name))



	def rectangleClicked(self, rectangleID):
		if self.screenBusy == True:
			return

		self.screenBusy = True
		if rectangleID == self.mainCanvas.hyruleFieldRect:
			self.loadSubLocation("Hyrule_Field")
		elif rectangleID == self.mainCanvas.lonLonRect:
			self.loadSubLocation("Lon_Lon_Ranch")
		elif rectangleID == self.mainCanvas.gerudoValleyRect:
			self.loadSubLocation("Gerudo_Valley")
		elif rectangleID == self.mainCanvas.gerudosFortressRect:
			self.loadSubLocation("Gerudos_Fortress")
		elif rectangleID == self.mainCanvas.hauntedWastelandRect:
			self.loadSubLocation("Haunted_Wasteland")
		elif rectangleID == self.mainCanvas.desertColossusRect:
			self.loadSubLocation("Desert_Colossus")
		elif rectangleID == self.mainCanvas.lakeHyliaRect:
			self.loadSubLocation("Lake_Hylia")
		elif rectangleID == self.mainCanvas.marketEntrywayRect:
			self.loadSubLocation("Market_Entryway")
		elif rectangleID == self.mainCanvas.marketRect:
			self.loadSubLocation("Market")
		elif rectangleID == self.mainCanvas.ToTEntrywayRect:
			self.loadSubLocation("Temple_Of_Time_Entryway")
		elif rectangleID == self.mainCanvas.ToTRect:
			self.loadSubLocation("Temple_Of_Time")
		elif rectangleID == self.mainCanvas.castleRect:
			self.loadSubLocation("Castle")
		elif rectangleID == self.mainCanvas.ganonRect:
			self.loadSubLocation("Ganons_Castle")
		elif rectangleID == self.mainCanvas.kokiriRect:
			self.loadSubLocation("Kokiri_Forest")
		elif rectangleID == self.mainCanvas.lostWoodsRect:
			self.loadSubLocation("Lost_Woods")
		elif rectangleID == self.mainCanvas.sacredForestRect:
			self.loadSubLocation("Sacred_Forest_Meadow")
		elif rectangleID == self.mainCanvas.kakarikoRect:
			self.loadSubLocation("Kakariko")
		elif rectangleID == self.mainCanvas.zorasRiverRect:
			self.loadSubLocation("Zoras_River")
		elif rectangleID == self.mainCanvas.graveyardRect:
			self.loadSubLocation("Graveyard")
		elif rectangleID == self.mainCanvas.zorasDomainRect:
			self.loadSubLocation("Zoras_Domain")
		elif rectangleID == self.mainCanvas.zorasFountainRect:
			self.loadSubLocation("Zoras_Fountain")
		elif rectangleID == self.mainCanvas.dmtRect:
			self.loadSubLocation("Death_Mountain_Trail")
		elif rectangleID == self.mainCanvas.goronCityRect:
			self.loadSubLocation("Goron_City")
		elif rectangleID == self.mainCanvas.dmcRect:
			self.loadSubLocation("Death_Mountain_Crater")

		else:
			print("\t...Unknown rectangle clicked!")
			self.screenBusy = False
			return

		self.screenBusy = False
		pass


	def addPathStartLoc(self):
		self.pathSource = self.lastLocation
		self.closeWindow()
		self.changeModes('PathEnd')

	def finishPath(self):
		self.pathDest = self.lastLocation
		self.closeWindow()
		self.changeModes('Explore')
		self.myShortestScreen = shortestPathScreen(self)

	def loadInfoRectangle(self, locationString):
		if self.screenBusy:
			return
		self.screenBusy = True

		self.lastLocation = locationString
		self.newRoot = Toplevel()
		self.newRoot.title('Info Rectangle')
		self.newRoot.geometry('700x400')
		myFontColor = "green"			
		if self.OOT_Graph.isExemptFromArea(locationString):
			myFontColor = "red"

		destinationsList = self.OOT_Graph.adjacency.getAllNonZeroDestinationsOfSource(self.OOT_Graph.string_to_ID_dictionary[locationString])
		
		destinationString = ""
		if destinationsList == []:
			destinationString = "---------------------"
			myFontColor = "blue"
		else:
			destinationString = self.OOT_Graph.ID_to_string_dictionary[destinationsList[0]]

		sourceLabel = Label(self.newRoot, text = "Source: ", fg = "black", font = "Heveltica 16 bold")
		sourceLabel.grid(row = 0, column = 0, sticky = W, padx = (8, 0))	
		sourceLocLabel = Label(self.newRoot, text = locationString, fg = myFontColor, font = "Heveltica 12")
		sourceLocLabel.grid(row = 0, column = 1, sticky = W)

		destinationLabel = Label(self.newRoot, text = "Destination: ", fg = "black", font = "Heveltica 16 bold")
		destinationLabel.grid(row = 1, column = 0, sticky = W, padx = (8, 0))

		destinationLocLabel = Label(self.newRoot, text = destinationString, fg = myFontColor, font = "Heveltica 12")
		destinationLocLabel.grid(row = 1, column = 1, sticky = W)


		if(self.mode == 'Explore'):
			actionButton = Button(self.newRoot, text = "        Add\nConnection", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.addSource)
		elif(self.mode == 'Destination'):
			actionButton = Button(self.newRoot, text = "      Finish\nConnection", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.addDestination)
		elif(self.mode == 'Song'):
			actionButton = Button(self.newRoot, text = "Set " + self.currentSong + "\nDestination", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.addSongDest)
		elif(self.mode == 'Spawn'):
			actionButton = Button(self.newRoot, text = "            Set " + self.spawnType + "\nSavewarp Destination", fg = "white", bg =  "blue", font = "Heveltica 16 bold", command = self.addSpawnLoc)
		elif(self.mode == 'PathStart'):
			actionButton = Button(self.newRoot, text = "   Select As\nStart of Path", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.addPathStartLoc)
		elif(self.mode == 'PathEnd'):
			actionButton = Button(self.newRoot, text = "        Select as\nDestination of Path", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.finishPath)


		if( (self.mode == 'Explore' or self.mode == 'Destination') and destinationsList != []):
			deleteButton = Button(self.newRoot, text = "      Delete\nConnection", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.deleteConnection)
			deleteButton.grid(row = 3, column = 0, sticky = W, pady = 20, padx = (8, 50)) 

		actionButton.grid(row = 2, column = 0, sticky = W, pady = 50, padx = (8, 50))			

	
		cancelButton = Button(self.newRoot, text = "Cancel", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.closeWindow)
		cancelButton.grid(row = 2, column = 1, sticky = W, pady = 50, ipady = 10)
		self.newRoot.protocol("WM_DELETE_WINDOW", self.closeWindow)	
	

	def deleteConnection(self):
		mySource = self.lastLocation
		destinationString = ""
		destinationList = self.OOT_Graph.adjacency.getAllNonZeroDestinationsOfSource(self.OOT_Graph.string_to_ID_dictionary[mySource])
		if destinationList == []:
			messaegebox.showwarning("Error", "Error: No connection found out from " + mySource)
			return
		destinationString = self.OOT_Graph.ID_to_string_dictionary[destinationList[0]]
		destinationID = destinationList[0]
		sourceID = self.OOT_Graph.string_to_ID_dictionary[mySource]
		self.OOT_Graph.adjacency.removeConnection(sourceID, destinationID)
		if self.OOT_Graph.isDecoupled == False:
			self.OOT_Graph.adjacency.removeConnection(destinationID, sourceID)

		messagebox.showinfo("Success!", "Succesfully deleted the connection from " + mySource + " to " + destinationString)
		self.closeWindow()
		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)
	
		self.changeModes('Explore')


	def addSource(self):
		if self.OOT_Graph.isExemptFromArea(self.lastLocation):
			messagebox.showwarning("Error", "Error: " + self.lastLocation + " can only be a destination, not a source!")
			return
		self.sourceLocation = self.lastLocation
		self.closeWindow()
		self.changeModes('Destination')


	def addDestination(self):
		if self.lastLocation == 'DMT_Owl' or self.lastLocation == 'Lake_Hylia_Owl':
			messagebox.showwarning("Error", "Error: " + self.lastLocation + " can only be a source, not a destination!")
			return
		self.destinationLocation = self.lastLocation
		self.OOT_Graph.addLinkBetweenStrings(self.sourceLocation, self.destinationLocation)
		messagebox.showinfo("Success!", "Added connection from " + self.sourceLocation + " to " + self.destinationLocation + "!")
		self.newRoot.destroy()
		if self.OOT_Graph.isAutosaveOn:
			self.OOT_Graph.writeDataToFile(self.controller.fileName)

		self.screenBusy = False
		self.changeModes('Explore')

	def closeWindow(self):
		self.newRoot.destroy()
		self.screenBusy = False


	#This function is called to handle when we change from one mode to another. 
	#More specifically, it changes what mode is stored in self.mode, recenters the title text
	#Adds or removes a cancel button from the top frame, and reloads the current canvas.
	def changeModes(self, newModeName):
		if self.screenBusy:
			return
		self.screenBusy = True
		if newModeName == 'Destination':
			self.mode = newModeName
			if self.mainCancelButton is None:
				self.mainCancelButton = Button(self.topFrame, text = "Cancel", fg = "white", bg = "blue", command = lambda: self.changeModes('Explore'))
			self.mainCancelButton.grid(row = 0, column = 2, padx = (0, 20))
			self.titleText['text'] = 'Select The Destination To Complete This Connection!'
			self.titleText.update()
			self.reloadCanvas()
		elif newModeName == 'Explore':
			self.mode = newModeName
			if self.mainCancelButton is not None:
				self.mainCancelButton.grid_forget()
			self.titleText['text'] = "Exploration Mode!"
			self.titleText.update()
			self.reloadCanvas()
		elif newModeName == 'Song':
			self.mode = newModeName
			if self.mainCancelButton is None:
				self.mainCancelButton = Button(self.topFrame, text = "Cancel", fg = "white", bg = "blue", command = lambda: self.changeModes('Explore'))
			self.mainCancelButton.grid(row = 0, column = 2, padx = (0, 20))
			self.titleText['text'] = "Select the entrance that " + self.currentSong + " takes you to"
			self.titleText.update()
			self.reloadCanvas()

		elif newModeName == 'Spawn':
			self.mode = newModeName
			if self.mainCancelButton is None:
				self.mainCancelButton = Button(self.topFrame, text = "Cancel", fg = "white", bg = "blue", command = lambda: self.changeModes('Explore'))

			self.mainCancelButton.grid(row = 0, column = 2, padx = (0, 20))
			self.titleText['text'] = "Select the savewarp location for " + self.spawnType
			self.titleText.update()
			self.reloadCanvas()

		elif newModeName == 'PathStart':
			self.mode = newModeName
			if self.mainCancelButton is None:
				self.mainCancelButton = Button(self.topFrame, text = "Cancel", fg = "white", bg = "blue", command = lambda: self.changeModes('Explore'))
			self.mainCancelButton.grid(row = 0, column = 2, padx = (0, 20))
			self.titleText['text'] = 'Select the start location of this path:'
			self.titleText.update()
			self.reloadCanvas() 
		elif newModeName == 'PathEnd':
			self.mode = newModeName
			self.titleText['text'] = 'Select the destination of this path:'
			self.titleText.update()
			self.reloadCanvas()



		else:
			print("Error: Unknown mode: " + newModeName)		
		self.screenBusy = False

	def reloadCanvas(self):
		if self.mainCanvas.type == 'mapSelectionCanvas':
			if self.myBackButton is not None:
				self.myBackButton.grid_forget()
			return
		elif self.mainCanvas.type == 'overworldCanvas':
			self.screenBusy = False
			self.overworldLoad(None)
		elif self.mainCanvas.type == 'subLocationCanvas':
			self.loadSubLocation(self.currentSubLocation)
			return
		elif self.mainCanvas.type == 'Dungeon':
			self.screenBusy = False
			self.dungeonLoad(None)
		elif self.mainCanvas.type == 'Grotto':
			self.screenBusy = False
			self.grottoLoad(None)
		elif self.mainCanvas.type == 'House':
			self.screenBusy = False
			self.houseLoad(None)


if __name__ == '__main__':
	mainMapScreen()
