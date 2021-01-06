from tkinter import *
from PIL import ImageTk, Image
from OOT_Locations_Graph import *
try:
	from tkmacosx import *
except:
	pass

class testClass:
	def __init__(self):
		self.controller = innerClass()


class innerClass:
	def __init__(self):
		self.OOT_Graph = OOT_Locations_Graph(True, False, False)
		self.OOT_Graph.readDataFromFile("temp")
		self.canvasBusy = False

class overworldCanvas(Canvas):

	def __init__(self, parentFrame, mainScreen):
		super().__init__(parentFrame, height = 790, width = 1420)
		self.pack()
		self.rootScreen = mainScreen
		self.type = "overworldCanvas"
		canvasHeight = 790
		canvasWidth = 1420
		self.img = ImageTk.PhotoImage(Image.open("./OOT_Overworld_Map.jpg").resize((1420, 760)))
		self.create_image(0, 0, anchor = NW, image = self.img)
		rectangleWidth = 60
		rectangleHeight = 25	
		self.OOT_Graph = self.rootScreen.controller.OOT_Graph
	
		#Setting up all the rectangles on the overworld (which take the user to a map of the location corresponding to the rectangle clicked on)

		#Setting up Hyrule Field rectangle
		hyruleX = 885
		hyruleY = 320	
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Hyrule_Field"):
			myFill = "yellow"
		self.hyruleFieldRect = self.create_rectangle(hyruleX, hyruleY, hyruleX + rectangleWidth, hyruleY + rectangleHeight, fill = myFill, activefill = "blue", tags = "hyruleField")
		
		
		#Setting up Lon Lon Ranch rectangle
		lonLonX = 765
		lonLonY = 365
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Lon_Lon_Ranch"):
			myFill = "yellow"
		self.lonLonRect = self.create_rectangle(lonLonX, lonLonY, lonLonX + rectangleWidth, lonLonY + rectangleHeight, fill = myFill, activefill = "blue", tags = "lonLonRanch")


		#Setting up Gerudo Valley rectangle
		gerudoValleyX = 515
		gerudoValleyY = 360
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Gerudo_Valley"):
			myFill = "yellow"
		self.gerudoValleyRect = self.create_rectangle(gerudoValleyX, gerudoValleyY, gerudoValleyX + rectangleWidth, gerudoValleyY + rectangleHeight, fill = myFill, activefill = "blue", tags = "gerudoValley")

		
		#Setting up Gerudo's Fortress rectangle
		gerudosFortressX = 420
		gerudosFortressY = 295
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Gerudos_Fortress"):
			myFill = "yellow"
		self.gerudosFortressRect = self.create_rectangle(gerudosFortressX, gerudosFortressY, gerudosFortressX + rectangleWidth, gerudosFortressY + rectangleHeight, fill = myFill, activefill = "blue", tags = "gerudosFortress")

		
		#Setting up Haunted Wasteland rectangle
		hauntedWastelandX = 230
		hauntedWastelandY = 264
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Haunted_Wasteland"):
			myFill = "yellow"
		self.hauntedWastelandRect = self.create_rectangle(hauntedWastelandX, hauntedWastelandY, hauntedWastelandX + rectangleWidth, hauntedWastelandY + rectangleHeight, fill = myFill, activefill = "blue", tags = "hauntedWasteland")


		#Setting up Desert Colossus Rectangle
		desertColossusX = 40
		desertColossusY = 253
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Desert_Colossus"):
			myFill = "yellow"
		self.desertColossusRect = self.create_rectangle(desertColossusX, desertColossusY, desertColossusX + rectangleWidth, desertColossusY + rectangleHeight, fill = myFill, activefill = "blue", tags = "desertColossus")


		#Setting up Lake Hylia Rectangle
		lakeHyliaX = 715
		lakeHyliaY = 615
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Lake_Hylia"):
			myFill = "yellow"
		self.lakeHyliaRect = self.create_rectangle(lakeHyliaX, lakeHyliaY, lakeHyliaX + rectangleWidth, lakeHyliaY + rectangleHeight, fill = myFill, activefill = "blue", tags = "lakeHylia")


		#Setting up the Market Entryway Rectangle	
		marketEntrywayX = 850
		marketEntrywayY = 245
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Market_Entryway"):
			myFill = "yellow"
		self.marketEntrywayRect = self.create_rectangle(marketEntrywayX, marketEntrywayY, marketEntrywayX + rectangleWidth, marketEntrywayY + rectangleHeight, fill = myFill, activefill = "blue", tags = "marketEntryway")


		
		#Setting up the Market Rectangle
		marketX = 800
		marketY = 200
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Market"):
			myFill = "yellow"
		self.marketRect = self.create_rectangle(marketX, marketY, marketX + rectangleWidth, marketY + rectangleHeight, fill = myFill, activefill = "blue", tags = "market")



		#Setting up the ToT Entryway Rectangle
		ToTEntrywayX = 900
		ToTEntrywayY = 180
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Temple_Of_Time_Entryway"):
			myFill = "yellow"
		self.ToTEntrywayRect = self.create_rectangle(ToTEntrywayX, ToTEntrywayY, ToTEntrywayX + rectangleWidth, ToTEntrywayY + rectangleHeight, fill = myFill, activefill = "blue", tags = "templeOfTimeEntryway")



		#Setting up the ToT Rectangle
		ToTX = 970
		ToTY = 160
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Temple_Of_Time"):
			myFill = "yellow"
		self.ToTRect = self.create_rectangle(ToTX, ToTY, ToTX + rectangleWidth, ToTY + rectangleHeight, fill = myFill, activefill = "blue", tags = "templeOfTime")


		#Setting up the Castle Rectangle
		castleX = 875		
		castleY = 125
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Castle"):
			myFill = "yellow"
		self.castleRect = self.create_rectangle(castleX, castleY, castleX + rectangleWidth, castleY + rectangleHeight, fill = myFill, activefill = "blue", tags = "castle")


		ganonX = 595
		ganonY = 140
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Castle"):
			myFill = "yellow"
		self.ganonRect = self.create_rectangle(ganonX, ganonY, ganonX + rectangleWidth, ganonY + rectangleHeight, fill = myFill, activefill = "blue", tags = "ganon")


		#Setting up the Kokiri Forest Rectangle
		kokiriX = 1075
		kokiriY = 542
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Kokiri_Forest"):
			myFill = "yellow"
		self.kokiriRect = self.create_rectangle(kokiriX, kokiriY, kokiriX + rectangleWidth, kokiriY + rectangleHeight, fill = myFill, activefill = "blue", tags = "kokiriForest")
	


		#Setting up the Lost Woods Rectangle
		lostWoodsX = 1060
		lostWoodsY = 478
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Lost_Woods"):
			myFill = "yellow"
		self.lostWoodsRect = self.create_rectangle(lostWoodsX, lostWoodsY, lostWoodsX + rectangleWidth, lostWoodsY + rectangleHeight, fill = myFill, activefill = "blue", tags = "lostWoods")



		#Setting up the Sacred Forest Meadow Rectangle
		sacredForestX = 1075
		sacredForestY = 420
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Sacred_Forest_Meadow"):
			myFill = "yellow"
		self.sacredForestRect = self.create_rectangle(sacredForestX, sacredForestY, sacredForestX + rectangleWidth, sacredForestY + rectangleHeight, fill = myFill, activefill = "blue", tags = "sacredForestMeadow")



		#Setting up the Kakariko Rectangle
		kakarikoX = 1000
		kakarikoY = 240
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Kakariko"):
			myFill = "yellow"
		self.kakarikoRect = self.create_rectangle(kakarikoX, kakarikoY, kakarikoX + rectangleWidth, kakarikoY + rectangleHeight, fill = myFill, activefill = "blue", tags = "kakariko")



		
		#Setting up the Zora's River Rectangle
		zorasRiverX = 1070
		zorasRiverY = 275
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Zoras_River"):
			myFill = "yellow"
		self.zorasRiverRect = self.create_rectangle(zorasRiverX, zorasRiverY, zorasRiverX + rectangleWidth, zorasRiverY + rectangleHeight, fill = myFill, activefill = "blue", tags = "zorasRiver")



		#Setting up the Graveyard Rectangle
		graveyardX = 1160
		graveyardY = 262
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Graveyard"):
			myFill = "yellow"
		self.graveyardRect = self.create_rectangle(graveyardX, graveyardY, graveyardX + rectangleWidth, graveyardY + rectangleHeight, fill = myFill, activefill = "blue", tags = "graveyard")



		#Setting up the Zora's Domain Rectangle
		zorasDomainX = 1245
		zorasDomainY = 270
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Zoras_Domain"):
			myFill = "yellow"
		self.zorasDomainRect = self.create_rectangle(zorasDomainX, zorasDomainY, zorasDomainX + rectangleWidth, zorasDomainY + rectangleHeight, fill = myFill, activefill = "blue", tags = "zorasDomain")



		#Setting up the Zora's Fountain Rectangle
		zorasFountainX = 1320
		zorasFountainY = 210
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Zoras_Fountain"):
			myFill = "yellow"
		self.zorasFountainRect = self.create_rectangle(zorasFountainX, zorasFountainY, zorasFountainX + rectangleWidth, zorasFountainY + rectangleHeight, fill = myFill, activefill = "blue", tags = "zorasFountain")



		#Setting up the Death Mountain Trail Rectangle
		dmtX = 1060
		dmtY = 160
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Death_Mountain_Trail"):
			myFill = "yellow"
		self.dmtRect = self.create_rectangle(dmtX, dmtY, dmtX + rectangleWidth, dmtY + rectangleHeight, fill = myFill, activefill = "blue", tags = "dmt")



		#Setting up the Goron City Rectangle
		goronCityX = 1150
		goronCityY = 105
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Goron_City"):
			myFill = "yellow"
		self.goronCityRect = self.create_rectangle(goronCityX, goronCityY, goronCityX + rectangleWidth, goronCityY + rectangleHeight, fill = myFill, activefill = "blue", tags = "goronCity")



		#Setting up the Death Mountain Crater Rectangle
		dmcX = 1110
		dmcY = 33
		myFill = "white"
		if self.OOT_Graph.allLocationsInAreaSet("Death_Mountain_Crater"):
			myFill = "yellow"
		self.dmcRect = self.create_rectangle(dmcX, dmcY, dmcX + rectangleWidth, dmcY + rectangleHeight, fill = myFill, activefill = "blue", tags = "dmc")

if __name__ == '__main__':
	tk = Tk()
	topFrame = Frame(tk, relief = RIDGE, borderwidth = 0)
	topFrame.grid(row = 0, column = 0, sticky = W)
	myText = Label(topFrame, text = "Exploration Mode!", fg = "red", font = "Heveltica 32 bold")
	myText.grid(row = 0, column = 1, sticky = N)
	myBackButton = Button(topFrame, text = "Back", bg = "blue", fg = "white")
	myBackButton.grid(row = 0, column = 0, sticky = W, padx = (10, 500))
	myFrame = Frame(tk, relief = RIDGE, borderwidth = 1)
	myFrame.grid(row = 1, column = 0)
	t = testClass()
	myCanvas = overworldCanvas(myFrame, t)	
	tk.mainloop()
		
