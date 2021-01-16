from tkinter import *
try:
	from tkmacosx import *
except:
	pass
from OOT_Locations_Graph import *

class songScreen():
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
		self.gui = Toplevel(bg = "white")

		#self.OOT_Graph = OOT_Locations_Graph(False, False, False, False)
		#self.OOT_Graph.hasSerenade = True
		#self.OOT_Graph.hasBolero = True
		#self.OOT_Graph.serenadeID = 15
		self.OOT_Graph = self.parentScreen.controller.OOT_Graph
		
		hasDefaultSongLocations = False
		if self.OOT_Graph.isDefaultSongs:
			hasDefaultSongLocations = True
		


		self.topFrame = Frame(self.gui)
		self.topFrame.grid(row = 0, column = 0, sticky = W)

		self.mainFrame = Frame(self.gui, bg = "white")
		self.mainFrame.grid(row = 1, column = 0, sticky = NSEW)
		self.mainLabel = Label(self.topFrame, text = "Select the warp songs you have, and where they lead to:", font = "Heveltica 32 bold", fg = "red")
		self.mainLabel.grid(row = 0, column = 0, padx = (400, 400), pady = (0, 20))

		#songList keeps track of what songs the user has. It is initalized to a list of lists, where each sublist has the form ['SongName', IntVar, addButton, deleteButton], and the corresponding IntVar is used for a checkbox that keeps track of whether or not the user has the song.
		self.songList = [
		['Minuet', IntVar(value = 0), Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue", fg = "white")], 
		['Bolero', IntVar(value = 0), Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue",     fg = "white")], 
		['Serenade', IntVar(value = 0), Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue",     fg = "white")], 
		['Requiem', IntVar(value = 0), Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue",     fg = "white")], 
		['Nocturne', IntVar(value = 0), Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue",     fg = "white")], 
		['Prelude', IntVar(value = 0), Button(self.mainFrame, text = "Set Destination", bg = "blue", fg = "white"), Button(self.mainFrame, text = "Delete Destination", bg = "blue",     fg = "white")]
		]	

		index = 0
		for element in self.songList:
			longNameCol = self.getLongSongNameAndColor(element[0])
			fullName = longNameCol[0]
			myColor = longNameCol[1]
			Checkbutton(self.mainFrame, text = fullName, var = element[1], bg = "white", fg = myColor, font = "Heveltica 20 bold").grid(row = index, column = 0, padx = (20, 20), pady = (0, 20), sticky = W)
			self.mainFrame.grid_rowconfigure(index, weight = 1)
			if self.OOT_Graph.userHasSong(element[0]):
				element[1].set(1)
		
			locationID = self.OOT_Graph.getSongLocation(element[0])
			locationString = "-----------------------------"
			if locationID != -1:
				locationString = self.OOT_Graph.ID_to_string_dictionary[locationID]
			Label(self.mainFrame, text = locationString, bg = "white", font = "Heveltica 16").grid(row = index, column = 1, padx = (0, 20), sticky = W)

			if hasDefaultSongLocations:
				index += 1
				continue

			element[2].grid(row = index, column = 2, padx = (0, 20), sticky = W)

			if locationID != -1:
				element[3].grid(row = index, column = 3, padx = (0, 20), sticky = W)
			
			index += 1

		self.saveButton = Button(self.mainFrame, text = "Confirm Changes", fg = "white", bg = "green")
		self.saveButton.grid(row = index, column = 0, sticky = W, padx = (20, 20), pady = (20, 20))

		self.cancelButton = Button(self.mainFrame, text = "Cancel", fg = "white", bg = "green")
		self.cancelButton.grid(row = index, column = 1, sticky = W, padx = (20, 20))
			

	#Returns the full name of a song and its associated color as a tuple. For example, if shortName is 'Minuet', then ('Minuet of Forest', 'green') is returned
	def getLongSongNameAndColor(self, shortName):			
		if shortName == 'Minuet':
			return ('Minuet of Forest', 'green')
		elif shortName == 'Bolero':
			return ('Bolero of Fire', 'red')
		elif shortName == 'Serenade':
			return ('Serenade of Water', 'blue')
		elif shortName == 'Nocturne':
			return ('Nocturne of Shadow', 'purple')
		elif shortName == 'Requiem':
			return ('Requiem of Spirit', 'orange')
		elif shortName == 'Prelude':
			return ('Prelude of Light', 'yellow')
		else:
			print("Error: Unknown songName of " + shortName + " in getLongSongNameAndColor()")
			exit(0)
			return None


if __name__ == '__main__':
	songScreen(None)
