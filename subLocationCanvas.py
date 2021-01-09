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
		elif subLocationName == 'Ganons_Castle':
			self.openImageFunction('./Ganons_Castle.png')
			self.openGanonsCastle()
		elif subLocationName == 'Castle':
			self.openImageFunction('./Castle.png')
			self.openCastle()
		elif subLocationName == 'Lost_Woods':
			self.openImageFunction('./Lost_Woods.png')
			self.openLostWoods()
		elif subLocationName == 'Sacred_Forest_Meadow':
			self.openImageFunction('./Sacred_Forest_Meadow.png')
			self.openSacredForestMeadow()
		elif subLocationName == 'Hyrule_Field':
			self.openImageFunction('./Hyrule_Field.png')
			self.openHyruleField()
		elif subLocationName == 'Market':
			self.openImageFunction('./Market.png')
			self.openMarket()
		elif subLocationName == 'Zoras_River':
			self.openImageFunction('./Zoras_River.png')
			self.openZorasRiver()
		elif subLocationName == 'Zoras_Domain':
			self.openImageFunction('./Zoras_Domain.png')
			self.openZorasDomain()
		elif subLocationName == 'Zoras_Fountain':
			self.openImageFunction('./Zoras_Fountain.png')
			self.openZorasFountain()		
		elif subLocationName == 'Graveyard':
			self.openImageFunction('./Graveyard.png')
			self.openGraveyard()
		elif subLocationName == 'Death_Mountain_Crater':
			self.openImageFunction('./Death_Mountain_Crater.png')
			self.openDMC()
		elif subLocationName == 'Goron_City':
			self.openImageFunction('./Goron_City.png')
			self.openGoronCity()
		elif subLocationName == 'Death_Mountain_Trail':
			self.openImageFunction('./Death_Mountain_Trail.png')
			self.openDMT()
		elif subLocationName == 'Kakariko':
			self.openImageFunction('./Kakariko.png')
			self.openKak()

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
		woodsListing = [
		['Lost_Woods_To_Kokiri_And_Lost', 574, 438],
		['Lost_Woods_Bridge_To_Kokiri', 275, 624],
		['Lost_Woods_Bridge_To_Hyrule_Field', 107, 624],
		['Lost_Woods_To_Goron_City', 825, 230],
		['Lost_Woods_To_Zoras_River', 1330, 285],
		['Lost_Woods_To_Sacred_Forest_Meadow', 828, 35],
		['Lost_Woods_To_Grotto_By_GC', 868, 260],
		['Lost_Woods_To_Grotto_By_Sacred_Forest_Meadow', 755, 50],
		['Lost_Woods_To_Deku_Stage_Grotto', 605, 180],
		['Deku_Stage_Grotto_Interior', 395, 155]	
		]
		self.setupRectangles(woodsListing)

	def openSacredForestMeadow(self):
		sacredListing = [
		['Sacred_Forest_Meadow_Minuet_Pedestal', 760, 99],
		['Sacred_Forest_Meadow_To_Forest_Temple', 760, 20],
		['Sacred_Forest_Meadow_To_SoS_Grotto', 820, 135],
		['Sacred_Forest_Meadow_To_LW', 708, 700],
		['Sacred_Forest_Meadow_To_Rainbow_Grotto', 695, 645],
		['Sacred_Forest_Meadow_To_Central_Grotto', 772, 443],
		['Rainbow_Grotto_Interior', 504, 680]
		]
		self.setupRectangles(sacredListing)

	def openHyruleField(self):
		hyruleListing = [
		['Hyrule_Field_To_Kokiri_Forest', 1215, 405],
		['Hyrule_Field_To_Market_Entrance', 865, 95],
		['Hyrule_Field_To_Gerudo_Valley', 200, 373],
		['Hyrule_Field_To_Lake_Hylia', 435, 700],
		['Hyrule_Field_To_Kak', 1105, 84],	
		['Hyrule_Field_To_Zoras_River', 1305, 207],
		['Hyrule_Field_To_Lon_Lon_Ranch', 715, 315],
		['Hyrule_Field_To_South_Open_Grotto', 555, 615],
		['Hyrule_Field_To_Far_South_Bombable_Grotto', 500, 650],
		['Hyrule_Field_To_South_Bombable_Rock_Grotto', 860, 520],
		['Hyrule_Field_To_Grotto_By_Kak', 1010, 60],
		['Hyrule_Field_To_North_West_Most_Bombable_Rock_Grotto', 565, 42],
		['Hyrule_Field_To_North_West_Tree_Grotto', 505, 150],
		['Hyrule_Field_To_Bombable_Rock_Grotto_By_Market', 745, 105],
		['Hyrule_Field_Owl_Dropoff', 865, 150],
		['Hyrule_Field_To_Grotto_By_Gerudo_Valley', 303, 340],
		['Webbed_Skulltula_Grotto_Interior', 225, 290],
		['Skulltula_High_On_Ceiling_Grotto_Interior', 910, 50],
		['Underwater_Heart_Piece_Grotto_Interior', 380, 180]
		
		]
		self.setupRectangles(hyruleListing)


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
		zoraLocations = [
		['Zoras_River_To_Hyrule_Field', 125, 733],
		['Zoras_River_To_SoS_Grotto', 163, 335],
		['Zoras_River_To_Bombable_Grotto', 623, 285],
		['Zoras_River_To_Open_Grotto', 490, 396],
		['Zoras_River_Waterfall', 1300, 64],
		['Zoras_River_To_Lost_Woods_Shortcut', 1265, 165]
		]
		self.setupRectangles(zoraLocations)

	def openZorasDomain(self):
		zoraLocations = [
		['Zoras_Domain_To_Zoras_River', 160, 575],
		['Zoras_Domain_To_SoS_Grotto', 315, 500],
		['Zoras_Domain_To_Lake_Hylia_Shortcut', 520, 580],
		['Zoras_Domain_To_Zora_Shop', 743, 650],
		['Zoras_Domain_To_Zoras_Fountain', 680, 35],
		['Zoras_Domain_Shop_Interior', 1250, 710]
		]
		self.setupRectangles(zoraLocations)

	
	def openZorasFountain(self):
		zoraLocations = [
		['Zoras_Fountain_To_Zoras_Domain', 215, 425],
		['Zoras_Fountain_To_Jabu_Jabu', 455, 347],
		['Zoras_Fountain_To_Ice_Cavern', 750, 130],
		['Zoras_Fountain_To_Farores_Wind', 895, 696],
		['Zoras_Fountain_Farores_Wind_Interior', 1173, 570]
		]
		self.setupRectangles(zoraLocations)

	def openKak(self):
		kakLocations = [
		['Kak_To_Hyrule_Field', 300, 464],
		['Kak_To_DMT_Gate', 863, 105],
		['Kak_To_Graveyard', 1225, 510],
		['Kak_To_Redead_Grotto', 760, 375],
		['Kak_To_Grotto_By_Potion_Shop', 1005, 280],
		['Kak_To_Bottom_Of_The_Well', 1015, 418],
		['Kak_To_Windmill', 1100, 390],
		['Kak_To_Malon_House', 855, 342],
		['Kak_To_Bazaar', 830, 225],
		['Kak_To_Potion_Shop_Front', 893, 240],
		['Kak_To_Potion_Shop_Back', 980, 240],
		['Kak_To_Odd_Medicine_Building', 1012, 320],
		['Kak_To_Archery', 930, 420],
		['Kak_To_House_Of_Skulltula', 810, 455],
		['Kak_To_Cow_In_House_Front_Door', 790, 550],
		['Kak_To_Cow_In_House_Cage', 915, 550],
		['Kak_On_Roof', 855, 530],
		['Kak_Malon_House_Interior', 270, 287],
		['Kak_Bazaar_Interior', 440, 80],
		['Kak_Potion_Shop_Front_Interior', 1235, 60],
		['Kak_Potion_Shop_Back_Interior', 1160, 40],
		['Kak_Archery_Interior', 1160, 118],
		['Kak_Odd_Medicine_Interior', 1295, 175],
		['Windmill_Front_Door', 1254, 318],
		['Kak_House_Of_Skulltula_Interior', 585, 600],
		['Kak_Cow_In_House_Cage_Interior', 960, 705],
		['Kak_Cow_In_House_Front_Door_Interior', 715, 705],
		['Kak_Redead_Grotto_Interior', 350, 570]
		]
		self.setupRectangles(kakLocations)
		pass

	def openGraveyard(self):
		graveLocations = [
		['Graveyard_To_Kak', 120, 365],
		['Graveyard_To_Dampes_Hut', 320, 425],
		['Graveyard_To_Shield_Grave', 380, 333],
		['Graveyard_To_Dampes_Gravestone', 320, 214],
		['Graveyard_To_Redead_Grave', 500, 367],
		['Graveyard_To_Royal_Family_Suns_Song_Grave', 678, 311],
		['Graveyard_Nocturne_Pedestal', 765, 311],
		['Graveyard_To_Shadow_Temple', 1130, 311],
		['Dampes_Hut_Interior', 420, 560],
		['Dampes_Grave_Main_Entrance', 279, 685],
		['Suns_Song_Royal_Family_Grave_Interior', 300, 70],
		['Suns_Song_Lone_Redead_Grave_Interior', 717, 540],
		['Grave_With_Shield_Chest_Interior', 717, 435]
		]
		self.setupRectangles(graveLocations)

	def openDMT(self):
		dmtLocations = [
		['DMT_To_Kak', 570, 680],
		['DMT_To_Dodongos_Cavern', 510, 450],
		['DMT_To_Goron_City', 965, 400],
		['DMT_To_SoS_Grotto', 1008, 445],
		['DMT_To_Bombable_Grotto', 638, 460],
		['DMT_To_Magic', 700, 170],
		['DMT_To_Death_Mountain_Crater', 775, 120],
		['DMT_Magic_Interior', 575, 100],
		['DMT_Owl', 760, 205]
		]
		self.setupRectangles(dmtLocations)

	def openGoronCity(self):
		goronLocations = [
		['Goron_City_To_Death_Mountain_Trail', 675, 710],
		['Goron_City_To_Lost_Woods', 863, 700],
		['Goron_City_To_Goron_Shop', 530, 400],
		['Goron_Shop_Interior', 400, 160],
		['Goron_City_Darunia_Statue', 689, 50],
		['Goron_City_To_Lava_Grotto', 1067, 147]
		]
		self.setupRectangles(goronLocations)

	def openDMC(self):
		dmcLocations = [
		['DMC_Bolero_Pedestal', 677, 300],
		['DMC_To_Darunias_Room', 245, 308],
		['DMC_To_Death_Mountain_Trail', 470, 585],
		['DMC_To_Bombable_Grotto', 685, 540],
		['DMC_To_Hammer_Grotto', 272, 215],
		['DMC_To_Double_Magic', 328, 450],
		['DMC_To_Fire_Temple', 680, 46],
		['DMC_Double_Magic_Interior', 292, 518]
		]
		self.setupRectangles(dmcLocations)

	def openMarketEntryway(self):
		marketLocations = [
		['Market_Entryway_To_Hyrule_Field', 1250, 200],
		['Market_Entryway_To_Market', 470, 600],
		['Market_Entryway_To_Big_Poe_House', 816, 240]
		]
		self.setupRectangles(marketLocations)

	def openMarket(self):
		marketLocations = [
		['Market_To_Market_Entryway', 702, 420],
		['Market_To_Castle', 702, 105],
		['Market_To_Temple_Of_Time_Entryway', 900, 140],
		['Market_To_Potion_Shop', 802, 232],
		['Market_To_Bazaar', 802, 305],	
		['Market_To_Bombchu_Bowling', 598, 257],
		['Market_To_Shooting_Gallery', 645, 125],
		['Market_To_Mask_Shop', 770, 125],
		['Market_To_Bombchu_Shop', 400, 400],
		['Market_To_Lens_Game', 615, 380],
		['Market_To_Back_Alley_Useless_House', 350, 115],
		['Bombchu_Shop_Interior', 570, 590],
		['Market_Bazaar_Interior', 1200, 400],
		['Market_Potion_Shop_Interior', 1200, 275],
		['Mask_Shop_Interior', 880, 100],
		['Market_Shooting_Gallery_Interior', 630, 22],
		['Market_Back_Alley_Useless_House_Interior', 245, 45],
		['Bombchu_Bowling_Interior', 550, 280],
		['Big_Poe_House_Interior', 850, 645],
		['Lens_Game_Interior', 1360, 165]
		]
		self.setupRectangles(marketLocations)

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
		castleLocations = [
		['Castle_To_Market', 488, 685],
		['Castle_To_Dins_Fire', 1165, 374],
		['Castle_Dins_Fire_Interior', 1120, 467],
		['Castle_To_SoS_Grotto', 715, 191],
		['Bombable_Wall_Skulltula_Grotto_Interior', 1050, 115]
		]
		self.setupRectangles(castleLocations)

	def openGanonsCastle(self):
		ganonLocations = [
		['Castle_To_Market', 578, 727],
		['Castle_To_Ganons_Castle', 518, 270],
		['Castle_To_Double_Defense', 1150, 262],
		['Castle_Double_Defense_Interior', 1155, 314]

		]
	
		self.setupRectangles(ganonLocations)


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
	myCanvas = subLocationCanvas(myFrame, tk, 'Kakariko')
	tk.mainloop()

