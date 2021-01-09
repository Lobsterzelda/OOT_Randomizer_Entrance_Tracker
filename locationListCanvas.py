from tkinter import *
try:
	from tkmacosx import *
except:
	pass
from OOT_Locations_Graph import *

class locationListCanvas(Canvas):
	def __init__(self, parentFrame, parentScreen, myType):
		super().__init__(parentFrame, height = 750, width = 1400)
		self.configure(scrollregion = (0, 0, 14000, 14000))
		self.pack(side = LEFT, expand = YES, fill = BOTH)
		vbar = Scrollbar(parentFrame, orient = VERTICAL)
		vbar.pack(side = RIGHT, fill = Y)
		vbar.config(command = self.yview)
		self.config(yscrollcommand = vbar.set)
		self.parentFrame = parentFrame
		self.parentScreen = parentScreen
		self.type = myType
		self.OOT_Graph = parentScreen.controller.OOT_Graph
		self.rect_ID_to_string_dictionary = {}
		self.text_ID_to_string_dictionary = {}
		self.locationsList = []
		if self.type == 'Dungeon':
			self.loadDungeons()
		elif self.type == 'House':
			self.loadHouses()
		elif self.type == 'Grotto':
			self.loadGrottos()
		else:
			for e in range(0, 20):
				self.create_rectangle(40, e * 100, 440, e * 100 + 60, fill = "blue")
		
		self.configure(scrollregion = (0, 0, 1400, len(self.locationsList) * 90 + 10))

		index = 0
		for location in self.locationsList:
			extraOffset = 0
			if index == 0:
				extraOffset = 10
			myFill = "white"
			myID = self.OOT_Graph.string_to_ID_dictionary[location]
			myList = self.OOT_Graph.adjacency.getAllNonZeroDestinationsOfSource(myID)
			if myList != []:
				myFill = "yellow"
			self.rect_ID_to_string_dictionary[self.create_rectangle(300, index * 90 + extraOffset, 1100, index * 90 + 60 + extraOffset, fill = myFill, activefill = "blue")] = location
			self.text_ID_to_string_dictionary[self.create_text(700, index * 90 + 30 + extraOffset, text = location, font = "Heveltica 20 bold")] = location
			index += 1	


	def loadDungeons(self):
		self.locationsList = [
		'Deku_Tree', 'Dodongos_Cavern', 'Jabu_Jabu', 'Forest_Temple', 'Fire_Temple', 'Water_Temple',
		'Shadow_Temple', 'Spirit_Temple_Main_Interior', 'Spirit_Temple_Silver_Gauntlets_Interior', 'Spirit_Temple_Mirror_Shield_Interior',
		'Bottom_Of_The_Well', 'Ice_Cavern', 'Gerudo_Training_Ground', 'Ganons_Castle']	


	def loadHouses(self):
		self.locationsList = [
		'Links_House_Interior', 'Useless_Kokiri_House_By_Sword_Interior', 'Useless_Kokiri_House_By_Links_House_Interior', 'Useless_Kokiri_House_By_Shop_Interior',
		'Kokiri_Shop_Interior', 'Midos_House_Interior', 'Zoras_Domain_Shop_Interior', 'Zoras_Fountain_Farores_Wind_Interior', 'Kak_Malon_House_Interior',
		'Kak_Bazaar_Interior', 'Kak_Potion_Shop_Front_Interior', 'Kak_Potion_Shop_Back_Interior', 'Kak_Odd_Medicine_Interior', 'Kak_Archery_Interior', 'Kak_House_Of_Skulltula_Interior',
		'Kak_Cow_In_House_Front_Door_Interior', 'Kak_Cow_In_House_Cage_Interior', 'DMT_Magic_Interior', 'DMC_Double_Magic_Interior', 'Goron_Shop_Interior', 'Dampes_Hut_Interior', 
		'Big_Poe_House_Interior', 'Mask_Shop_Interior', 'Market_Bazaar_Interior', 'Market_Potion_Shop_Interior', 'Market_Shooting_Gallery_Interior',
		'Bombchu_Bowling_Interior', 'Lens_Game_Interior', 'Market_Back_Alley_Useless_House_Interior', 'Castle_Dins_Fire_Interior', 'Castle_Double_Defense_Interior', 'Bombchu_Shop_Interior',
		'Gerudo_Valley_Tent_Interior', 'Gerudos_Fortress_Interior', 'Desert_Colossus_Nayrus_Love_Interior',
		'Lakeside_Laboratory_Interior', 'Fishing_Pond_Interior', 'Lon_Lon_Ranch_Malons_House_Interior', 'Lon_Lon_Ranch_Stables_Interior', 'Lon_Lon_Ranch_Heart_Piece_Tower_Interior'
		]

		for tempLocation in self.OOT_Graph.string_to_ID_dictionary:
			if 'Generic_House_Interior' in tempLocation:
				self.locationsList.append(tempLocation)


		self.locationsList.sort()
	
	def loadGrottos(self):	
		self.locationsList = [
		'Suns_Song_Royal_Family_Grave_Interior', 'Suns_Song_Lone_Redead_Grave_Interior', 'Grave_With_Shield_Chest_Interior',
		'Deku_Stage_Grotto_Interior', 'Rainbow_Grotto_Interior', 'Kak_Redead_Grotto_Interior', 'Bombable_Wall_Skulltula_Grotto_Interior',
		'Skulltula_High_On_Ceiling_Grotto_Interior', 'Underwater_Heart_Piece_Grotto_Interior', 'Webbed_Skulltula_Grotto_Interior'
		]
		
		for tempLocation in self.OOT_Graph.string_to_ID_dictionary:
			if 'Generic_Chest_Grotto_Interior' in tempLocation or 'Two_Business_Scrub_Grotto_Interior' in tempLocation or 'Three_Business_Scrubs_Grotto_Interior' in tempLocation or 'One_Business_Scrub_Grotto_Interior' in tempLocation or 'Generic_Fairy_Fountain_Grotto_Interior' in tempLocation or 'Cow_Grotto_Interior' in tempLocation or 'Money_Grotto_Interior' in tempLocation:
				self.locationsList.append(tempLocation)

		self.locationsList.sort()























		
		
