from tkinter import *
try:
	from tkmacosx import *
except:
	pass


from mapSelectionCanvas import *
from overworldCanvas import *
from subLocationCanvas import *

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
		self.lastLocation = ""
		self.sourceLocation = ""
		self.destinationLocation = ""
		self.currentSubLocation = ""

		fileMenu = Menu(menuBar)
		fileMenu.add_command(label = "New Randomizer", command = donothing)
		fileMenu.add_command(label = "Load Randomizer", command = donothing)
		fileMenu.add_command(label = "Save", command = donothing)
		fileMenu.add_separator()
		fileMenu.add_command(label = "Exit Program", command = donothing)
		menuBar.add_cascade(label = "File", menu = fileMenu)

		songMenu = Menu(menuBar)
		songMenu.add_command(label = "Open Song Tracker", command = donothing)
		menuBar.add_cascade(label = "Songs", menu = songMenu)   
        
		ageMenu = Menu(menuBar)
		ageMenu.add_command(label = "Open Temple Of Time Tracker", command = donothing)
		menuBar.add_cascade(label = "Age", menu = ageMenu)

		viewMenu = Menu(menuBar)
		viewMenu.add_command(label = "View Current Seed Properties", command = donothing)
		menuBar.add_cascade(label = "View", menu = viewMenu)

		reminderMenu = Menu(menuBar)
		reminderMenu.add_command(label = "Open Reminder Tracker", command = donothing)
		menuBar.add_cascade(label = "Reminders", menu = reminderMenu)

		navigationMenu = Menu(menuBar)
		navigationMenu.add_command(label = "Find Shortest Path", command = donothing)
		menuBar.add_cascade(label = "Routing", menu = navigationMenu)

		helpMenu = Menu(menuBar)
		helpMenu.add_command(label = "Help", command = donothing)
		menuBar.add_cascade(label = "Help", menu = helpMenu)		

		self.mode = "Explore"  #mode has the value 'Explore' by default, when the user hasn't done anything. The user can select a source for a connection in this mode. Other values are 'Destination', where the user needs to select a destination to make a connection to. 'PathStart' when setting a path from the source, 'PathEnd' when selecting a destination from a source. and 'Song-X', when setting the destination for a song, where X is the name of the song, and 'childStart' and 'adultStart' modes.
	
		self.gui.title("Select Map!")
		self.mainCancelButton = None
		self.screenBusy = False
		self.topFrame = Frame(self.gui, relief = RIDGE, borderwidth = 0, bg = '#FFFFE0')
		self.topFrame.grid(row = 0, column = 0, sticky = N+S+E+W)
		self.mainFrame = Frame(self.gui, relief = RAISED, borderwidth = 1)
		self.mainFrame.grid(row = 1, column = 0)
		self.mainCanvas = mapSelectionCanvas(self.mainFrame, self)
		self.mainCanvas.tag_bind("overworldButton", "<Button-1>", self.overworldLoad)
		self.mainCanvas.tag_bind("overworldText", "<Button-1>", self.overworldLoad)
		self.titleText = Label(self.topFrame, text = "Exploration Mode!", fg = "red", font = "Heveltica 32 bold", bg = '#FFFFE0')
		self.titleText.grid(row = 0, column = 1, sticky = N)
		self.topFrame.grid_rowconfigure(0, weight = 1)
		self.topFrame.grid_columnconfigure(1, weight = 1)

		self.gui.protocol("WM_DELETE_WINDOW", self.leaveFunc)
		self.gui.mainloop()
		

	def leaveFunc(self):
		exit(0)


	def goBackFromOverworld(self):
		if self.screenBusy:
			return
		self.mainCanvas.destroy()
		self.mainCanvas = mapSelectionCanvas(self.mainFrame, self)
		self.myBackButton.grid_forget()
		self.mainCanvas.tag_bind("overworldButton", "<Button-1>", self.overworldLoad)
		self.mainCanvas.tag_bind("overworldText", "<Button-1>", self.overworldLoad)

	def overworldLoad(self, args):
		if self.screenBusy == False:
			self.screenBusy = True
			self.mainCanvas.destroy()
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
		self.mainCanvas = subLocationCanvas(self.mainFrame, self, locName)
		self.myBackButton.grid_forget()
		self.myBackButton = Button(self.topFrame, text = "Back", bg = "blue", fg = "white", command = self.goBackFromSubLocation)
		self.myBackButton.grid(row = 0, column = 0, sticky = W, padx = (10, 0))

		for rectID in self.mainCanvas.rect_ID_to_string_dictionary:
			self.mainCanvas.tag_bind(rectID, '<Button-1>', lambda x, name = self.mainCanvas.rect_ID_to_string_dictionary[rectID]: self.loadInfoRectangle(name))



	def rectangleClicked(self, rectangleID):
		print("In rectangleClicked...")
		if self.screenBusy == True:
			print("Screen was busy!")
			return

		self.screenBusy = True
		if rectangleID == self.mainCanvas.hyruleFieldRect:
			self.loadSubLocation("Hyrule_Field")
			print("\t...Hyrule Field clicked!")
		elif rectangleID == self.mainCanvas.lonLonRect:
			self.loadSubLocation("Lon_Lon_Ranch")
			print("\t...Lon Lon Ranch clicked!")
		elif rectangleID == self.mainCanvas.gerudoValleyRect:
			self.loadSubLocation("Gerudo_Valley")
			print("\t...Gerudo Valley clicked!")
		elif rectangleID == self.mainCanvas.gerudosFortressRect:
			self.loadSubLocation("Gerudos_Fortress")
			print("\t...Gerudo's Fortress clicked!")
		elif rectangleID == self.mainCanvas.hauntedWastelandRect:
			self.loadSubLocation("Haunted_Wasteland")
			print("\t...Haunted Wasteland clicked!")
		elif rectangleID == self.mainCanvas.desertColossusRect:
			print("\t...Desert Colossus clicked!")
			self.loadSubLocation("Desert_Colossus")
		elif rectangleID == self.mainCanvas.lakeHyliaRect:
			self.loadSubLocation("Lake_Hylia")
			print("\t...Lake Hylia clicked!")
		elif rectangleID == self.mainCanvas.marketEntrywayRect:
			print("\t...Market Entryway clicked!")
			self.loadSubLocation("Market_Entryway")
		elif rectangleID == self.mainCanvas.marketRect:
			self.loadSubLocation("Market")
			print("\t...Market clicked!")
		elif rectangleID == self.mainCanvas.ToTEntrywayRect:
			print("\t...Temple of Time Entryway clicked!")
			self.loadSubLocation("Temple_Of_Time_Entryway")
		elif rectangleID == self.mainCanvas.ToTRect:
			self.loadSubLocation("Temple_Of_Time")
		elif rectangleID == self.mainCanvas.castleRect:
			self.loadSubLocation("Castle")
			print("\t...Hyrule Castle clicked!")
		elif rectangleID == self.mainCanvas.ganonRect:
			print("\t...Ganon's Castle clicked!")
			self.loadSubLocation("Ganons_Castle")
		elif rectangleID == self.mainCanvas.kokiriRect:
			print("\t...Kokiri Forest clicked!")
			self.loadSubLocation("Kokiri_Forest")
		elif rectangleID == self.mainCanvas.lostWoodsRect:
			self.loadSubLocation("Lost_Woods")
			print("\t...Lost Woods clicked!")
		elif rectangleID == self.mainCanvas.sacredForestRect:
			self.loadSubLocation("Sacred_Forest_Meadow")
			print("\t...Sacred Forest Meadow clicked!")
		elif rectangleID == self.mainCanvas.kakarikoRect:
			print("\t...Kakariko Village clicked!")
		elif rectangleID == self.mainCanvas.zorasRiverRect:
			self.loadSubLocation("Zoras_River")
			print("\t...Zora's River clicked!")
		elif rectangleID == self.mainCanvas.graveyardRect:
			self.loadSubLocation("Graveyard")
			print("\t...Graveyard clicked!")
		elif rectangleID == self.mainCanvas.zorasDomainRect:
			self.loadSubLocation("Zoras_Domain")
			print("\t...Zora's Domain clicked!")
		elif rectangleID == self.mainCanvas.zorasFountainRect:
			self.loadSubLocation("Zoras_Fountain")
			print("\t...Zora's Fountain clicked!")
		elif rectangleID == self.mainCanvas.dmtRect:
			print("\t..Death Mountain Trail clicked!")
		elif rectangleID == self.mainCanvas.goronCityRect:
			print("\t...Goron City clicked!")
		elif rectangleID == self.mainCanvas.dmcRect:
			print("\t...Death Mountain Crater clicked!")

		else:
			print("\t...Unknown rectangle clicked!")
			self.screenBusy = False
			return

		self.screenBusy = False
		pass


	def loadInfoRectangle(self, locationString):
		if self.screenBusy:
			return
		self.screenBusy = True

		self.lastLocation = locationString
		self.newRoot = Toplevel()
		self.newRoot.geometry('400x500')
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
		sourceLocLabel.grid(row = 0, column = 1)

		destinationLabel = Label(self.newRoot, text = "Destination: ", fg = "black", font = "Heveltica 16 bold")
		destinationLabel.grid(row = 1, column = 0, sticky = W, padx = (8, 0))

		destinationLocLabel = Label(self.newRoot, text = destinationString, fg = myFontColor, font = "Heveltica 12")
		destinationLocLabel.grid(row = 1, column = 1, sticky = W)


		if(self.mode == 'Explore'):
			actionButton = Button(self.newRoot, text = "        Add\nConnection", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.addSource)
		elif(self.mode == 'Destination'):
			actionButton = Button(self.newRoot, text = "Finish\nConnection", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.addDestination)


		if( (self.mode == 'Explore' or self.mode == 'Destination') and destinationsList != []):
			deleteButton = Button(self.newRoot, text = "Delete\nConnection", fg = "white", bg = "blue", font = "Heveltica 16 bold", command = self.deleteConnection)
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
		else:
			print("Error: Unknown mode: " + newModeName)		
		self.screenBusy = False

	def reloadCanvas(self):
		if self.mainCanvas.type == 'mapSelectionCanvas':
			return
		elif self.mainCanvas.type == 'overworldCanvas':
			self.screenBusy = False
			self.overworldLoad(None)
		elif self.mainCanvas.type == 'subLocationCanvas':
			self.loadSubLocation(self.currentSubLocation)
			return




if __name__ == '__main__':
	mainMapScreen()
