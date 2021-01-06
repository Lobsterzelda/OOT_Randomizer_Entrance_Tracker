from tkinter import *
from OOT_Locations_Graph import *
from PIL import ImageTk, Image
try:
	from tkmacosx import *
except:
	pass

class subLocationCanvas(Canvas):
	def __init__(self, parentFrame, parentScreen, subLocationName):
		super().__init__(parentFrame, height = 790, width = 1420)
		self.pack()
		self.type = "subLocationCanvas"
		self.rectangleWidth = 40 
		self.rectangleHeight = 17
		canvasHeight = 790
		canvasWidth = 1420
		self.rootScreen = parentScreen
		self.OOT_Graph = parentScreen.controller.OOT_Graph
		#self.OOT_Graph = OOT_Locations_Graph(True, True, True, True)
		self.img = None
		self.rectanglesArray = []
		self.rect_ID_to_string_dictionary = {}
		
		if subLocationName == 'Kokiri_Forest':
			self.openImageFunction('./Kokiri_Forest.png')
			self.openKokiri()
		elif subLocationName == 'Temple_Of_Time_Entryway':
			self.openImageFunction('./Temple_Of_Time_Entryway.png')
			self.openTempleOfTimeEntryway()
		elif subLocationName == 'Temple_Of_Time':
			self.openImageFunction('./Temple_Of_Time.png')
			self.openTempleOfTime()
		elif subLocationName == 'Lake_Hylia':
			self.openImageFunction('./Lake_Hylia.png')
			self.openLakeHylia()
		elif subLocationName == 'Lon_Lon_Ranch':
			self.openImageFunction('./Lon_Lon_Ranch.png')
			self.openLonLonRanch()
		elif subLocationName == 'Haunted_Wasteland':
			self.openImageFunction('./Haunted_Wasteland.png')
			self.openHauntedWasteland()
		elif subLocationName == 'Desert_Colossus':
			self.openImageFunction('./Desert_Colossus.png')
			self.openDesertColossus()
		elif subLocationName == 'Market_Entryway':
			self.openImageFunction('./Market_Entryway.png')
			self.openMarketEntryway()

		elif subLocationName == 'Gerudos_Fortress':
			self.openImageFunction('./Gerudos_Fortress.png')
			self.openGerudosFortress()
		elif subLocationName == 'Gerudo_Valley':
			self.openImageFunction('./Gerudo_Valley.png')
			self.openGerudoValley()

		else:
			print("in subLocationCanvas(), I haven't implemented the location " + subLocationName + " yet!")


	def openKokiri(self):
		kokiriLocationsListing = [
		['Kokiri_To_Kokiri_Shop', 665, 320],
		['Kokiri_To_Midos_House', 457, 296],
 		['Kokiri_To_Useless_Kokiri_House_By_Shop', 695, 425],
		['Kokiri_To_Useless_Kokiri_House_By_Links_House', 605, 435],
		['Kokiri_To_Link_House', 525, 500],
		['Kokiri_To_Useless_Kokiri_House_By_Sword', 375, 410],
		['Kokiri_To_Lost_Woods_Main', 482, 150],
		['Kokiri_To_SoS_Grotto', 465, 186],
		['Kokiri_To_Ocarina_Bridge', 290, 312],
		['Kokiri_To_Deku_Tree', 1135, 190],
		['Kokiri_Shop_Interior', 715, 218],
		['Links_House_Interior', 910, 580],
		['Useless_Kokiri_House_By_Sword_Interior', 260, 680],
		['Useless_Kokiri_House_By_Links_House_Interior', 1215, 580],
		['Useless_Kokiri_House_By_Shop_Interior', 1210, 485],
		['Midos_House_Interior', 260, 403]
		]

		
		self.setupRectangles(kokiriLocationsListing)

	def openLostWoods(self):
		pass

	def openSacredForestMeadow(self):
		pass

	def openHyruleField(self):
		pass

	def openLonLonRanch(self):
		lonLonListing = [
		['Lon_Lon_Ranch_To_Hyrule_Field', 1000, 18],
		['Lon_Lon_Ranch_To_Malons_House', 923, 98],
		['Lon_Lon_Ranch_To_Stables', 850, 128],
		['Lon_Lon_Ranch_To_Heart_Piece_Tower', 250, 643],
		['Lon_Lon_Ranch_Stables_Interior', 685, 135],
		['Lon_Lon_Ranch_Malons_House_Interior', 1115, 93],
		['Lon_Lon_Ranch_Heart_Piece_Tower_Interior', 210, 704],
		['Lon_Lon_Ranch_To_Grotto', 1130, 630]
		]
		self.setupRectangles(lonLonListing)

	def openZorasRiver(self):
		pass

	def openZorasDomain(self):
		pass
	
	def openZorasFountain(self):
		pass

	def openKak(self):
		pass

	def openGraveyard(self):
		pass

	def openDMT(self):
		pass

	def openGoronCity(self):
		pass

	def openDMC(self):
		pass

	def openMarketEntryway(self):
		marketLocations = [
		['Market_Entryway_To_Hyrule_Field', 1250, 200],
		['Market_Entryway_To_Market', 470, 600],
		['Market_Entryway_To_Big_Poe_House', 816, 240]
		]
		self.setupRectangles(marketLocations)

	def openMarket(self):
		pass

	def openTempleOfTimeEntryway(self):
		templeOfTimeLocationsListings = [
		['Temple_Of_Time_Entryway_To_Market', 1000, 600],
		['Temple_Of_Time_Entryway_To_Temple_Of_Time', 540, 235]
		]
		self.setupRectangles(templeOfTimeLocationsListings)


	def openTempleOfTime(self):
		templeOfTimeLocationsListings = [
		['Temple_Of_Time_Prelude_Pedestal', 635, 380],
		['Temple_Of_Time_Front_Interior', 420, 370]
		]
		self.setupRectangles(templeOfTimeLocationsListings)

	def openCastle(self):
		pass

	def openGerudoValley(self):
		gerudoLocations = [
		['Gerudo_Valley_To_Hyrule_Field', 1365, 420],
		['Gerudo_Valley_To_Gerudos_Fortress', 190, 180],
		['Gerudo_Valley_To_Lake_Hylia', 1000, 715],
		['Gerudo_Valley_To_Tent', 700, 270],
		['Gerudo_Valley_To_Silver_Rock_Grotto', 937, 465],
		['Gerudo_Valley_Tent_Interior', 430, 450],
		['Gerudo_Valley_To_SoS_Grotto', 715, 200]
		]
		self.setupRectangles(gerudoLocations)
		pass

	def openGerudosFortress(self):
		gerudoLocations = [
		['Gerudos_Fortress_To_Gerudo_Valley', 725, 645],
		['Gerudos_Fortress_To_Wasteland', 195, 100],
		['Gerudos_Fortress_To_Gerudos_Fortress_Interior', 980, 220],
		['Gerudos_Fortress_To_SoS_Grotto', 1035, 328],
		['Gerudos_Fortress_To_Gerudo_Training_Ground', 950, 426]

		]
		self.setupRectangles(gerudoLocations)

	def openHauntedWasteland(self):
		hauntedWastelandLocations = [
		['Haunted_Wasteland_To_Gerudos_Fortress', 1245, 503],
		['Haunted_Wasteland_To_Desert_Colossus', 40, 290]		
		]
		self.setupRectangles(hauntedWastelandLocations)

	def openDesertColossus(self):
		desertLocations = [
		['Desert_Colossus_To_Wasteland', 1150, 350],
		['Desert_Colossus_To_Nayrus_Love', 905, 205],
		['Desert_Colossus_Requiem_Pedestal', 380, 145],
		['Desert_Colossus_To_Silver_Rock_Grotto', 535, 230],
		['Desert_Colossus_Nayrus_Love_Interior', 1140, 145],
		['Desert_Colossus_To_Spirit_Temple_Main_Entrance', 290, 390],
		['Desert_Colossus_To_Silver_Guantlets_Spirit_Entrance', 242, 443],
		['Desert_Colossus_To_Mirror_Shield_Spirit_Entrance', 248, 345]

		]
		self.setupRectangles(desertLocations)

	def openLakeHylia(self):
		lakeHyliaLocations = [
		['Lake_Hylia_Serenade_Pedestal', 553, 629],
		['Lake_Hylia_Owl', 280, 456],
		['Lake_Hylia_To_Gravestone', 230, 505],
		['Lake_Hylia_To_Water_Temple', 570, 548],
		['Lake_Hylia_To_Fishing_Pond', 930, 246],
		['Lake_Hylia_To_Hyrule_Field', 390, 15],
		['Lake_Hylia_To_Gerudo_Valley', 63, 92],
		['Lake_Hylia_To_Zoras_Domain', 575, 204],
		['Lake_Hylia_To_Lakeside_Laboratory', 355, 255],
		['Fishing_Pond_Interior', 1200, 245],
		['Lakeside_Laboratory_Interior', 215, 60]
		
		]
		self.setupRectangles(lakeHyliaLocations)



	#rectanglesList is a list, where each element is a list of 3 elements: [location_name, x_top_left_coord, y_top_left_coord]
	#Ex. rectanglesList = [	['Kokiri_To_Kokiri_Shop', 500, 200], ['Kokiri_To_Midos_House', 300, 142] ]
	def setupRectangles(self, rectanglesList):
		for entry in rectanglesList:
			entryName = entry[0]
			x_coord = entry[1]
			y_coord = entry[2]
			myFill = "white"
			myOOT_ID = self.OOT_Graph.string_to_ID_dictionary[entryName]
			if(self.OOT_Graph.adjacency.getAllNonZeroDestinationsOfSource(myOOT_ID) != []):
				myFill = "yellow"

			elif(entryName == 'Sacred_Forest_Meadow_Minuet_Pedestal' or entryName == 'DMC_Bolero_Pedestal' or entryName == 'Lake_Hylia_Serenade_Pedestal' or entryName == 'Graveyard_Nocturne_Pedestal' or entryName == 'Desert_Colossus_Requiem_Pedestal' or entryName == 'Temple_Of_Time_Prelude_Pedestal' or entryName == 'Kak_On_Roof' or entryName == 'Hyrule_Field_Owl_Dropoff'):	
				myFill = "red"

			myRectangleID = self.create_rectangle(x_coord, y_coord, x_coord + self.rectangleWidth, y_coord + self.rectangleHeight, fill = myFill, activefill = "blue")	
			self.rectanglesArray.append(myRectangleID)
			self.rect_ID_to_string_dictionary[myRectangleID] = entryName

	def openImageFunction(self, imageName):
		self.img = ImageTk.PhotoImage(Image.open(imageName).resize((1420, 760)))
		self.create_image(0, 0, anchor = NW, image = self.img)		


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
	myCanvas = subLocationCanvas(myFrame, tk, 'Gerudo_Valley')
	tk.mainloop()

