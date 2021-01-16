from tkinter import *
try:
	from tkmacosx import *
except:
	pass

from OOT_Locations_Graph import *

class shortestPathScreen:
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
	
		self.OOT_Graph = self.parentScreen.controller.OOT_Graph	
		self.pathSource = self.parentScreen.pathSource
		self.pathDest = self.parentScreen.pathDest

		self.regularExclusionList = []
		self.specialExclusionList = []

		self.gui = Toplevel(bg = "white")
		self.gui.title("Shortest Path")
		
		self.topFrame = Frame(self.gui, bg = "white")
		self.topFrame.grid(row = 0, column = 0, sticky = W)


		self.mainFrame = Frame(self.gui, bg = "white")
		self.mainFrame.grid(row = 1, column = 0, sticky = W, padx = (50, 50))

		self.bottomFrame = Frame(self.gui, bg = "white")
		self.bottomFrame.grid(row = 2, column = 0, sticky = NSEW, pady = (0, 180))

		self.titleLabel = Label(self.topFrame, text = "Path Finder: ", fg = "red", bg = "white", font = "Heveltica 48 bold")
		self.titleLabel.grid(row = 0, column = 0, sticky = W, padx = (600, 200))

	
		self.locationsLabel = Label(self.topFrame, text =  self.pathSource + "\nTo\n" + self.pathDest, bg = "white", fg = "black", font = "Heveltica 16 bold")
		self.locationsLabel.grid(row = 1, column = 0, sticky = NSEW, padx = (600, 200))	
		

		self.listbox = Listbox(self.mainFrame, bg = "white", fg = "black", font = "Heveltica 16", height = 15, width = 100, selectmode = MULTIPLE)
		self.listbox.grid(row = 0, column = 0, sticky = W, padx = (50, 0))
		self.horizontalScroll = Scrollbar(self.mainFrame, orient = HORIZONTAL)
		self.horizontalScroll.grid(row = 1, column = 0, sticky = S, padx = (50, 0))
		self.listbox.config(xscrollcommand = self.horizontalScroll.set)
		self.horizontalScroll.config(command = self.listbox.xview)
		self.verticalScroll = Scrollbar(self.mainFrame)
		self.verticalScroll.grid(row = 0, column = 1, sticky = E)
		self.listbox.config(yscrollcommand = self.verticalScroll.set)
		self.verticalScroll.config(command = self.listbox.yview)


		self.reRunButton = Button(self.bottomFrame, text = "Re-Run With\nHighlighted Entrances\nExcluded", bg = "blue", fg = "white", command = self.runAlgorithm)
		self.reRunButton.grid(row = 0, column = 0, padx = (200, 20), sticky = NSEW)

		
		self.clearButton = Button(self.bottomFrame, text = "Unhighlight All", bg = "blue", fg = "white", command = self.clearAll)
		self.clearButton.grid(row = 0, column = 1, padx = (20, 20), sticky = NSEW)


		self.runAlgorithm()

		self.gui.mainloop()



	def clearAll(self):
		self.listbox.select_clear(0, END)	


	def runAlgorithm(self):	
		for index in self.listbox.curselection():
			entranceString = self.listbox.get(index)
			if entranceString.strip() == 'No Path Found!':
				return

			if '->' in entranceString:
				splitList = entranceString.split('->')
				sourceString = splitList[0].strip()
				destinationString = splitList[1].strip()
				self.regularExclusionList.append( [self.OOT_Graph.string_to_ID_dictionary[sourceString], self.OOT_Graph.string_to_ID_dictionary[destinationString]])

			else:
				specialString = entranceString.strip()
				self.specialExclusionList.append(self.OOT_Graph.string_to_ID_dictionary[specialString])

	
		self.listbox.delete(0, END)

		finalPath = self.OOT_Graph.fullGetShortestPathAlgorithm(self.OOT_Graph.string_to_ID_dictionary[self.pathSource], self.OOT_Graph.string_to_ID_dictionary[self.pathDest], self.regularExclusionList, self.specialExclusionList)

		if finalPath is None:
			self.listbox.insert(END, " No Path Found!")
			return


		finalPath = finalPath[0]

		index = 0
		while index < len(finalPath):
			if finalPath[index] < -1:
				self.listbox.insert(END, " " + self.OOT_Graph.ID_to_string_dictionary[finalPath[index]])
			elif index + 1 < len(finalPath):
				self.listbox.insert(END, " " + self.OOT_Graph.ID_to_string_dictionary[finalPath[index]] + " -> " + self.OOT_Graph.ID_to_string_dictionary[finalPath[index + 1]])

			index += 1

		

if __name__ == '__main__':
	shortestPathScreen(None)		




			
