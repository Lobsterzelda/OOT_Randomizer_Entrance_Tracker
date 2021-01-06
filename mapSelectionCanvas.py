from tkinter import *
try:
	from tkmacosx import *
except:
	pass

class mapSelectionCanvas(Canvas):
	def __init__(self, frame, rootScreen):
		super().__init__(frame, height = 790, width = 1420)
		self.pack()
		self.rootScreen = rootScreen
		self.type = "mapSelectionCanvas"
		canvasHeight = 790
		canvasWidth = 1420

		mainText = self.create_text(canvasWidth // 2, 25, text="Select a Map Screen to Use!", font = ("Times", 32, "bold"))

		X1 = canvasWidth // 2 - 160
		X2 = canvasWidth // 2 + 150		

		firstY1 = 100
		firstY2 = firstY1 + 50

		secondY1 = firstY2 + 50
		secondY2 = secondY1 + 50

		thirdY1 = secondY2 + 50
		thirdY2 = thirdY1 + 50

		fourthY1 = thirdY2 + 50
		fourthY2 = fourthY1 + 50

		self.overworldMap_Rectangle = self.create_rectangle(X1, 100, X2, 150, fill = "blue", tags = "overworldButton")
		overworldText = self.create_text(canvasWidth // 2, (firstY1 + firstY2) // 2, text = "Overworld Map", font = ("Heveltica", 26), fill = "white", tags = "overworldText")
		
		self.tag_bind("overworldButton", "<Enter>", self.changeRectOverworldColorRed)
		self.tag_bind("overworldButton", "<Leave>", self.changeRectOverworldColorBlue)
		self.tag_bind("overworldText", "<Enter>", self.changeRectOverworldColorRed)


		self.dungeonList_Rectangle = self.create_rectangle(X1, secondY1, X2, secondY2, fill = "blue", tags = "dungeonButton")
		self.dungeonText = self.create_text(canvasWidth // 2, (secondY1 + secondY2) // 2, text = "Dungeon List", font = ("Heveltica", 26), fill = "white", tags = "dungeonText")

		self.tag_bind("dungeonButton", "<Enter>", self.changeRectDungeonColorRed)
		self.tag_bind("dungeonButton", "<Leave>", self.changeRectDungeonColorBlue)
		self.tag_bind("dungeonText", "<Enter>", self.changeRectDungeonColorRed)
		

		self.housesList_Rectangle = self.create_rectangle(X1, thirdY1, X2, thirdY2, fill = "blue", tags = "housesButton")
		self.housesText = self.create_text(canvasWidth // 2, (thirdY1 + thirdY2) // 2, text = "Houses List", font = ("Heveltica", 26), fill = "white", tags = "housesText")

		self.tag_bind("housesButton", "<Enter>", self.changeRectHousesColorRed)
		self.tag_bind("housesButton", "<Leave>", self.changeRectHousesColorBlue)
		self.tag_bind("housesText", "<Enter>", self.changeRectHousesColorRed)

		
		self.grottosList_Rectangle = self.create_rectangle(X1, fourthY1, X2, fourthY2, fill = "blue", tags = "grottosButton")
		self.grottosText = self.create_text(canvasWidth // 2, (fourthY1 + fourthY2) // 2, text = "Grottos List", font = ("Heveltica", 26), fill = "white", tags = "grottosText")

		self.tag_bind("grottosButton", "<Enter>", self.changeRectGrottosColorRed)
		self.tag_bind("grottosButton", "<Leave>", self.changeRectGrottosColorBlue)
		self.tag_bind("grottosText", "<Enter>", self.changeRectGrottosColorRed)



	def changeRectOverworldColorBlue(self, args):
		self.itemconfig(self.overworldMap_Rectangle, fill = "blue")

	def changeRectOverworldColorRed(self, args):
		self.itemconfig(self.overworldMap_Rectangle, fill = "red")
		self.changeRectDungeonColorBlue(None)
		self.changeRectHousesColorBlue(None)
		self.changeRectGrottosColorBlue(None)

	def changeRectDungeonColorBlue(self, args):
		self.itemconfig(self.dungeonList_Rectangle, fill = "blue")

	def changeRectDungeonColorRed(self, args):
		self.itemconfig(self.dungeonList_Rectangle, fill = "red")
		self.changeRectOverworldColorBlue(None)
		self.changeRectHousesColorBlue(None)
		self.changeRectGrottosColorBlue(None)

	def changeRectHousesColorBlue(self, args):
		self.itemconfig(self.housesList_Rectangle, fill = "blue")

	def changeRectHousesColorRed(self, args):
		self.itemconfig(self.housesList_Rectangle, fill = "red")
		self.changeRectOverworldColorBlue(None)
		self.changeRectDungeonColorBlue(None)
		self.changeRectGrottosColorBlue(None)
	
	def changeRectGrottosColorBlue(self, args):
		self.itemconfig(self.grottosList_Rectangle, fill = "blue")
		
	def changeRectGrottosColorRed(self, args):
		self.itemconfig(self.grottosList_Rectangle, fill = "red")
		self.changeRectOverworldColorBlue(None)
		self.changeRectDungeonColorBlue(None)
		self.changeRectHousesColorBlue(None)



	def openOverworldMap(self, args):
		print("Clicked open overworld map button")
		pass 
		if self.rootScreen.controller.canvasBusy:
			return
		self.rootScreen.controller.canvasBusy = True
	
		self.rootScreen.controller.canvasBusy = False


	def openDungeonList(self, args):
		print("Clicked openDungeons Button")
		pass
		if self.rootScreen.controller.canvasBusy:
			return
		self.rootScreen.controller.canvasBusy = True
		
		self.rootScreen.controller.canvasBusy = False

	def openHousesList(self, args):
		print("Clicked openHouses Button")
		pass
		if self.rootScreen.controller.canvasBusy:
			return
		self.rootScreen.controller.canvasBusy = True

		self.rootScreen.controller.canvasBusy = False


	def openGrottosList(self, args):
		print("Clicked openGrottos Button")
		pass
		if self.rootScreen.controller.canvasBusy:
			return
		self.rootScreen.controller.canvasBusy = True

		self.rootScreen.controller.canvasBusy = False


if __name__ == '__main__':
	root = Tk()
	myFrame = Frame(root, relief = RAISED, borderwidth = 1)
	myFrame.pack(anchor = CENTER, fill = BOTH, expand = TRUE)
	mapSelectionCanvas(myFrame)
	root.mainloop()
