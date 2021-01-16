#This is the main program that is run by the user to track entrances locations

import sys
from OOT_Locations_Graph import *

import faulthandler; faulthandler.enable()
import threading
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from setupRandomizerScreen import *
from helpScreen import *

try:
	from tkmacosx import *
except:
	pass

def donothing():
	return

class firstScreen:
	def __init__(self, parent):
		self.gui = Toplevel()
		self.gui.title("Lobsterzelda's OOT Entrance Randomizer Tracker")
		self.gui.geometry('1000x8000')
		self.popUpLoaded = False
		self.fileName = ""
		self.doneWithFirstScreen = False
		self.OOT_Graph = OOT_Locations_Graph(False, True, True)
		self.decoupled = False
		self.defaultStarts = True
		self.defaultSongs = True
		self.autosaveEnabled = True
		self.parent = parent
		self.terminatingSignalSent = False	
	

		menuBar = Menu(self.gui)
		self.gui.config(menu = menuBar)
		fileMenu = Menu(menuBar)
		fileMenu.add_command(label = "New Randomizer", command = self.newRandomizerFunction)
		fileMenu.add_command(label = "Load Randomizer", command = self.loadRandomizerFunction)
		fileMenu.add_separator()
		fileMenu.add_command(label = "Exit Program", command =	self.exitProgram)
		menuBar.add_cascade(label = "File", menu = fileMenu)

		helpMenu = Menu(menuBar)
		helpMenu.add_command(label = "Help", command = self.loadHelp)
		menuBar.add_cascade(label = "Help", menu = helpMenu)
		
		self.mainText = Label(self.gui, text="Welcome to Lobsterzelda's OOT Entrance Randomizer Tracker!\nPlease select whether you would like to create a new randomizer or load a randomizer you have already created!\nNote: you can use the help option in the menu to answer any questions you have about this app", font = "Times 20 bold")
		self.mainText.config(anchor=CENTER)
		self.mainText.pack(side = TOP)
		
		self.newButton = Button(self.gui, text = "New Randomizer", activebackground = "red", highlightbackground = "red", font = ("Heveltica", 30, "bold"), bg = "blue", fg = "white", command = self.newRandomizerFunction)
		self.newButton.pack(side = LEFT, expand = True, fill = BOTH, padx = (10,100), pady = (10,350))
		self.loadButton = Button(self.gui, text = "Load Randomizer", highlightbackground = "red", activebackground = "red", font = ("Heveltica", 30, "bold"), bg = "blue", fg = "white", command = self.loadRandomizerFunction)
		self.loadButton.pack(side = RIGHT, expand = True, fill = BOTH, padx = (0,30), pady = (10, 350))


		self.newButton.bind("<Enter>", lambda x: self.changeRed(self.newButton))
		self.newButton.bind("<Leave>", lambda x: self.changeBlue(self.newButton))

		self.loadButton.bind("<Enter>", lambda x: self.changeRed(self.loadButton))
		self.loadButton.bind("<Leave>", lambda x: self.changeBlue(self.loadButton))

		self.gui.protocol("WM_DELETE_WINDOW", self.exitProgram)
		self.gui.mainloop()

	def loadHelp(self):
		helpScreen(self)

	def changeBlue(self, button):
		button.config(background = "blue")

	def changeRed(self, button):
		if button == self.newButton:
			self.changeBlue(self.loadButton)
		else:
			self.changeBlue(self.newButton)
		button.config(background = "red")


	#This function causes the first screen, the background thread of the first screen, and the create new randomizer screen to all terminate. After this function has finished, control returns to the mainController class.
	def exitProgram(self):
		if self.popUpLoaded == False:
			self.gui.destroy()		
			self.gui.quit()

	def loadRandomizerFunction(self):
		if self.popUpLoaded == False:
			self.popUpLoaded = True
			self.fileName = ""
			self.fileName = askopenfilename()
			returnCode = self.coreLoadRandoFunction()
			self.popUpLoaded = False
			if returnCode == 0:
				self.parent.OOT_Graph = self.OOT_Graph
				self.parent.fileName = self.fileName
				self.parent.readyForMainMapScreen = True
				self.gui.destroy()
				self.gui.quit()

	def coreLoadRandoFunction(self):
		if self.fileName.strip() != "": 
			try:
				if self.OOT_Graph.readDataFromFile(self.fileName) != 0:
					messagebox.showerror("Invalid File", "Error: The file you selected was either not found or was not correctly formatted. Please check that you have selected an OOT Randomizer Data File created by this program and then try again.", icon = "warning") 
					return -1 
				else:
					messagebox.showinfo("Success!", "Randomizer Data File Successfully Launched!", icon = "info")
					return 0 
			except:
				messagebox.showerror("Invalid File", "Error: The file you selected was either not found or was not correctly formatted. Please check that you have selected an OOT Randomizer Data File created by this program and then try again.", icon = "warning")
				return -1
		return -1

	def newRandomizerFunction(self):
		if self.popUpLoaded == False:
			self.popUpLoaded = True
			self.customizeScreen = setupRandomizerScreen(self)
			if self.parent.readyForMainMapScreen == True:
				self.parent.OOT_Graph = self.OOT_Graph
				self.parent.fileName = self.fileName
				self.gui.destroy()
				self.gui.quit()

if __name__ == '__main__':
	mainFileName = ""
	myFirstScreen = firstScreen()
