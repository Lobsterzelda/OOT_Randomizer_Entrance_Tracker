#This class is the main graph which is used to store connections between different entrances and locations in OOT
#All entrances in a specific area are connected to the entrance by a node in the adjacency list with a weight of 0
#For example, DMC has the upper mountain entrance, the Darunia statue entrance, the Fire Temple entrance, the bolero warp pedastal entrance, 
#The hammer grotto, the double magic entrance, and the grotto under the bombable rock entrance. All of these locations would be represented by an integer
#in the adjacency list. Another entry in the adjacency list would represent DMC itself, and would be connected to each of these locations with a weight of 0
#(this would go both ways, so the darunia statue entrance would have a connection to DMC with weight 0, and DMC would have a connection with weight 0 to the darunia statue entrance)
#Entrances which lead to one another have a weight of 1 in the adjacency list. For example, suppose going through the darunia statue entrance in DMC leads to the main entrance to graveyard. Then, the main entrance to grave yard and the darunia statue entrance in DMC would each have a weight connection one to the other with a weight value of 1 (this would really be 2 connections in the adjacency list, since there is a path from the first to the second and the second to the first i.e. the entrances are reversible, and you can go back the way you came in either direction).

from adjacencyList import adjacencyList
from copy import deepcopy
import math


def addOneToPathHelper(pathDistResult, newIndex):
	if pathDistResult is not None:
		pathDistResult[1] = pathDistResult[1] + 1
		pathDistResult[0].insert(0, newIndex)
	return pathDistResult

class OOT_Locations_Graph:

	def __init__(self, decoupled = False, defaultStarts = True, defaultSongs = True, autoSave = True):
		self.isDecoupled = decoupled
		self.isDefaultStartPoints = defaultStarts
		self.isDefaultSongs = defaultSongs
		self.isAutosaveOn = autoSave
		self.reminderList = []

		self.entrances_locations_dictionary = {
		'Kokiri_To_Useless_Kokiri_House_By_Sword':'Kokiri_Forest', 'Kokiri_To_Useless_Kokiri_House_By_Links_House': 'Kokiri_Forest', 'Kokiri_To_Useless_Kokiri_House_By_Shop': 'Kokiri_Forest',
		'Kokiri_To_Link_House':'Kokiri_Forest', 'Kokiri_To_Kokiri_Shop':'Kokiri_Forest', 'Kokiri_To_Midos_House':'Kokiri_Forest',
		'Kokiri_To_SoS_Grotto':'Kokiri_Forest', 'Kokiri_To_Deku_Tree':'Kokiri_Forest', 'Kokiri_To_Ocarina_Bridge':'Kokiri_Forest', 'Kokiri_To_Lost_Woods_Main':'Kokiri_Forest',

		'Lost_Woods_To_Kokiri_And_Lost':'Lost_Woods', 'Lost_Woods_Bridge_To_Kokiri':'Lost_Woods', 'Lost_Woods_Bridge_To_Hyrule_Field':'Lost_Woods',
		'Lost_Woods_To_Sacred_Forest_Meadow' : 'Lost_Woods', 'Lost_Woods_To_Goron_City':'Lost_Woods',  'Lost_Woods_To_Zoras_River':'Lost_Woods',
		'Lost_Woods_To_Grotto_By_GC': 'Lost_Woods', 'Lost_Woods_To_Deku_Stage_Grotto':'Lost_Woods', 'Lost_Woods_To_Grotto_By_Sacred_Forest_Meadow':'Lost_Woods',

		'Sacred_Forest_Meadow_To_LW' : 'Sacred_Forest_Meadow', 'Sacred_Forest_Meadow_To_Rainbow_Grotto':'Sacred_Forest_Meadow', 'Sacred_Forest_Meadow_To_Central_Grotto':'Sacred_Forest_Meadow',
		'Sacred_Forest_Meadow_To_SoS_Grotto': 'Sacred_Forest_Meadow', 'Sacred_Forest_Meadow_Minuet_Pedestal':'Sacred_Forest_Meadow', 'Sacred_Forest_Meadow_To_Forest_Temple':'Sacred_Forest_Meadow',
					
		'Zoras_River_To_Hyrule_Field':'Zoras_River', 'Zoras_River_To_SoS_Grotto':'Zoras_River', 'Zoras_River_To_Bombable_Grotto':'Zoras_River',
		'Zoras_River_To_Open_Grotto':'Zoras_River', 'Zoras_River_Waterfall':'Zoras_River', 'Zoras_River_To_Lost_Woods_Shortcut':'Zoras_River',

		'Zoras_Domain_To_Zoras_River':'Zoras_Domain', 'Zoras_Domain_To_SoS_Grotto':'Zoras_Domain', 'Zoras_Domain_To_Zora_Shop':'Zoras_Domain',
		'Zoras_Domain_To_Lake_Hylia_Shortcut':'Zoras_Domain', 'Zoras_Domain_To_Zoras_Fountain':'Zoras_Domain',

		'Zoras_Fountain_To_Zoras_Domain':'Zoras_Fountain', 'Zoras_Fountain_To_Jabu_Jabu':'Zoras_Fountain', 'Zoras_Fountain_To_Ice_Cavern':'Zoras_Fountain', 'Zoras_Fountain_To_Farores_Wind':'Zoras_Fountain',

		'Kak_To_Malon_House':'Kakariko', 'Kak_To_Redead_Grotto':'Kakariko', 'Kak_To_Bazaar':'Kakariko', 'Kak_To_Potion_Shop_Front':'Kakariko', 'Kak_To_Potion_Shop_Back':'Kakariko',
		'Kak_To_Grotto_By_Potion_Shop':'Kakariko', 'Kak_To_Odd_Medicine_Building':'Kakariko', 'Kak_To_Windmill':'Kakariko', 'Kak_To_Bottom_Of_The_Well':'Kakariko', 'Kak_To_Archery':'Kakariko',
		'Kak_To_House_Of_Skulltula':'Kakariko', 'Kak_To_Cow_In_House_Front_Door':'Kakariko', 'Kak_To_Cow_In_House_Cage':'Kakariko', 'Kak_To_Graveyard':'Kakariko',
		'Kak_To_DMT_Gate':'Kakariko', 'Kak_To_Hyrule_Field':'Kakariko', 'Kak_On_Roof':'Kakariko',

		'DMT_To_Kak' : 'Death_Mountain_Trail', 'DMT_To_Dodongos_Cavern' : 'Death_Mountain_Trail', 'DMT_To_SoS_Grotto' : 'Death_Mountain_Trail',
		'DMT_To_Bombable_Grotto' : 'Death_Mountain_Trail', 'DMT_To_Magic' : 'Death_Mountain_Trail', 'DMT_Owl' : 'Death_Mountain_Trail',
		'DMT_To_Death_Mountain_Crater' : 'Death_Mountain_Trail', 'DMT_To_Goron_City' : 'Death_Mountain_Trail',

		'DMC_To_Death_Mountain_Trail' : 'Death_Mountain_Crater', 'DMC_To_Bombable_Grotto' : 'Death_Mountain_Crater', 'DMC_To_Double_Magic' : 'Death_Mountain_Crater',
		'DMC_To_Hammer_Grotto' : 'Death_Mountain_Crater', 'DMC_To_Darunias_Room' : 'Death_Mountain_Crater', 'DMC_Bolero_Pedestal' : 'Death_Mountain_Crater',
		'DMC_To_Fire_Temple' : 'Death_Mountain_Crater', 

		'Graveyard_To_Kak' : 'Graveyard', 'Graveyard_To_Dampes_Hut' : 'Graveyard', 'Graveyard_To_Shield_Grave' : 'Graveyard', 'Graveyard_To_Dampes_Gravestone' : 'Graveyard',
		'Graveyard_To_Redead_Grave' : 'Graveyard', 'Graveyard_To_Royal_Family_Suns_Song_Grave' : 'Graveyard', 'Graveyard_To_Shadow_Temple' : 'Graveyard',
		'Graveyard_Nocturne_Pedestal' : 'Graveyard',

		'Dampes_Grave_Main_Entrance' : 'Dampes_Grave', 'Dampes_Grave_To_Windmill' : 'Dampes_Grave',

		'Windmill_Front_Door' : 'Windmill', 'Windmill_From_Dampes_Grave' : 'Windmill',
			
		'Goron_City_To_Death_Mountain_Trail' : 'Goron_City', 'Goron_City_To_Lost_Woods' : 'Goron_City', 'Goron_City_Darunia_Statue' : 'Goron_City',
		'Goron_City_To_Goron_Shop' : 'Goron_City', 'Goron_City_To_Lava_Grotto' : 'Goron_City',

		'Market_Entryway_To_Hyrule_Field' : 'Market_Entryway', 'Market_Entryway_To_Market' : 'Market_Entryway', 'Market_Entryway_To_Big_Poe_House' : 'Market_Entryway',

		'Temple_Of_Time_Entryway_To_Market' : 'Temple_Of_Time_Entryway', 'Temple_Of_Time_Entryway_To_Temple_Of_Time' : 'Temple_Of_Time_Entryway',

		'Market_To_Mask_Shop' : 'Market', 'Market_To_Bazaar' : 'Market', 'Market_To_Potion_Shop' : 'Market', 'Market_To_Shooting_Gallery' : 'Market',
		'Market_To_Bombchu_Bowling' : 'Market', 'Market_To_Lens_Game' : 'Market', 'Market_To_Bombchu_Shop' : 'Market', 'Market_To_Back_Alley_Useless_House' : 'Market',
		'Market_To_Market_Entryway' : 'Market', 'Market_To_Castle' : 'Market', 'Market_To_Temple_Of_Time_Entryway' : 'Market',

		'Temple_Of_Time_Front_Interior' : 'Temple_Of_Time', 'Temple_Of_Time_Prelude_Pedestal' : 'Temple_Of_Time',

		'Castle_To_Market' : 'Castle', 'Castle_To_Dins_Fire' : 'Castle', 'Castle_To_SoS_Grotto' : 'Castle', 'Castle_To_Ganons_Castle' : 'Castle', 'Castle_To_Double_Defense' : 'Castle',

		'Gerudo_Valley_To_Hyrule_Field' : 'Gerudo_Valley', 'Gerudo_Valley_To_Silver_Rock_Grotto' : 'Gerudo_Valley', 'Gerudo_Valley_To_SoS_Grotto' : 'Gerudo_Valley',
		'Gerudo_Valley_To_Tent' : 'Gerudo_Valley', 'Gerudo_Valley_To_Gerudos_Fortress' : 'Gerudo_Valley', 'Gerudo_Valley_To_Lake_Hylia' : 'Gerudo_Valley',		

		'Gerudos_Fortress_To_Gerudo_Valley' : 'Gerudos_Fortress', 'Gerudos_Fortress_To_Gerudos_Fortress_Interior': 'Gerudos_Fortress', 'Gerudos_Fortress_To_Gerudo_Training_Ground' : 'Gerudos_Fortress',
		'Gerudos_Fortress_To_Wasteland' : 'Gerudos_Fortress', 'Gerudos_Fortress_To_SoS_Grotto' : 'Gerudos_Fortress',

		'Haunted_Wasteland_To_Gerudos_Fortress' : 'Haunted_Wasteland', 'Haunted_Wasteland_To_Desert_Colossus' : 'Haunted_Wasteland',

		'Desert_Colossus_To_Wasteland' : 'Desert_Colossus', 'Desert_Colossus_To_Nayrus_Love' : 'Desert_Colossus', 'Desert_Colossus_Requiem_Pedestal' : 'Desert_Colossus',
		'Desert_Colossus_To_Silver_Rock_Grotto' : 'Desert_Colossus', 'Desert_Colossus_To_Spirit_Temple_Main_Entrance' : 'Desert_Colossus',
		'Desert_Colossus_To_Silver_Guantlets_Spirit_Entrance' : 'Desert_Colossus', 'Desert_Colossus_To_Mirror_Shield_Spirit_Entrance' : 'Desert_Colossus',			

		'Lake_Hylia_To_Hyrule_Field' : 'Lake_Hylia', 'Lake_Hylia_To_Zoras_Domain' : 'Lake_Hylia', 'Lake_Hylia_To_Lakeside_Laboratory' : 'Lake_Hylia',
		'Lake_Hylia_To_Fishing_Pond' : 'Lake_Hylia', 'Lake_Hylia_Owl' : 'Lake_Hylia', 'Lake_Hylia_To_Gravestone' : 'Lake_Hylia', 'Lake_Hylia_To_Water_Temple' : 'Lake_Hylia',
		'Lake_Hylia_Serenade_Pedestal' : 'Lake_Hylia', 'Lake_Hylia_To_Gerudo_Valley' : 'Lake_Hylia',

		'Lon_Lon_Ranch_To_Malons_House' : 'Lon_Lon_Ranch', 'Lon_Lon_Ranch_To_Stables' : 'Lon_Lon_Ranch', 'Lon_Lon_Ranch_To_Grotto' : 'Lon_Lon_Ranch',
		'Lon_Lon_Ranch_To_Heart_Piece_Tower' : 'Lon_Lon_Ranch', 'Lon_Lon_Ranch_To_Hyrule_Field' : 'Lon_Lon_Ranch',

		'Hyrule_Field_To_Lake_Hylia' : 'Hyrule_Field', 'Hyrule_Field_To_South_Open_Grotto' : 'Hyrule_Field', 'Hyrule_Field_To_Far_South_Bombable_Grotto' : 'Hyrule_Field',
		'Hyrule_Field_To_South_Bombable_Rock_Grotto' : 'Hyrule_Field', 'Hyrule_Field_To_Kokiri_Forest' : 'Hyrule_Field', 
		'Hyrule_Field_To_Lon_Lon_Ranch' : 'Hyrule_Field', 'Hyrule_Field_To_Zoras_River' : 'Hyrule_Field', 'Hyrule_Field_To_Grotto_By_Kak' : 'Hyrule_Field', 
		'Hyrule_Field_To_Market_Entrance' : 'Hyrule_Field', 'Hyrule_Field_Owl_Dropoff' : 'Hyrule_Field', 
		'Hyrule_Field_To_Bombable_Rock_Grotto_By_Market' : 'Hyrule_Field', 'Hyrule_Field_To_Kak' : 'Hyrule_Field',
		'Hyrule_Field_To_North_West_Most_Bombable_Rock_Grotto' : 'Hyrule_Field', 'Hyrule_Field_To_North_West_Tree_Grotto' : 'Hyrule_Field',
		'Hyrule_Field_To_Grotto_By_Gerudo_Valley' : 'Hyrule_Field', 'Hyrule_Field_To_Gerudo_Valley' : 'Hyrule_Field',

		'Spirit_Temple_Main_Interior' : 'Spirit_Temple', 'Spirit_Temple_Silver_Gauntlets_Interior' : 'Spirit_Temple', 'Spirit_Temple_Mirror_Shield_Interior' : 'Spirit_Temple' }

		self.overworldLocations = [
		'Kokiri_Forest', 'Lost_Woods', 'Zoras_River', 'Zoras_Domain', 'Zoras_Fountain', 'Kakariko_Village', 'Death_Mountain_Trail',
		'Death_Mountain_Crater', 'Goron_City', 'Graveyard', 'Market_Entryway', 'Market', 'Temple_Of_Time_Entryway', 'Castle',
		'Gerudo_Valley', 'Gerudos_Fortress', 'Haunted_Wasteland', 'Desert_Colossus', 'Lake_Hylia', 'Lon_Lon_Ranch',
		'Hyrule_Field', 'Sacred_Forest_Meadow' ]

		self.dungeonLocations = [
		'Deku_Tree', 'Dodongos_Cavern', 'Jabu_Jabu', 'Forest_Temple', 'Fire_Temple', 'Water_Temple', 'Shadow_Temple', 'Spirit_Temple',
		'Bottom_Of_The_Well', 'Ice_Cavern', 'Gerudo_Training_Ground', 'Gerudos_Fortress', 'Ganons_Castle' ]

		self.grottoLocations = [
		'Suns_Song_Royal_Family_Grave_Interior', 'Suns_Song_Lone_Redead_Grave_Interior', 'Grave_With_Shield_Chest_Interior', 'Generic_Chest_Grotto_Interior',
		'Two_Business_Scrubs_Grotto_Interior', 'Three_Business_Scrubs_Grotto_Interior', 'One_Business_Scrub_Grotto_Interior', 'Deku_Stage_Grotto_Interior',
		'Rainbow_Grotto_Interior', 'Generic_Fairy_Fountain_Grotto_Interior', 'Kak_Redead_Grotto_Interior', 'Cow_Grotto_Interior', 'Bombable_Wall_Skulltula_Grotto_Interior',
		'Money_Grotto_Interior', 'Skulltula_High_On_Ceiling_Grotto_Interior', 'Underwater_Heart_Piece_Grotto_Interior', 'Webbed_Skulltula_Grotto_Interior']

		self.houseLocations = [
		'Links_House_Interior', 'Useless_Kokiri_House_By_Sword_Interior', 'Useless_Kokiri_House_By_Links_House_Interior', 'Useless_Kokiri_House_By_Shop_Interior',
		'Kokiri_Shop_Interior', 'Midos_House_Interior', 'Zoras_Domain_Shop_Interior', 'Zoras_Fountain_Farores_Wind_Interior', 'Kak_Malon_House_Interior',
		'Kak_Bazaar_Interior', 'Kak_Potion_Shop_Front_Interior', 'Kak_Potion_Shop_Back_Interior', 'Kak_Odd_Medicine_Interior', 'Kak_Archery_Interior', 'Kak_House_Of_Skulltula_Interior',
		'Kak_Cow_In_House_Front_Door_Interior', 'Kak_Cow_In_House_Cage_Interior', 'DMT_Magic_Interior', 'DMC_Double_Magic_Interior', 'Goron_Shop_Interior', 'Dampes_Hut_Interior', 
		'Big_Poe_House_Interior', 'Mask_Shop_Interior', 'Market_Bazaar_Interior', 'Market_Potion_Shop_Interior', 'Market_Shooting_Gallery_Interior',
		'Bombchu_Bowling_Interior', 'Lens_Game_Interior', 'Market_Back_Alley_Useless_House_Interior', 'Castle_Dins_Fire_Interior', 'Castle_Double_Defense_Interior', 'Bombchu_Shop_Interior',
		'Gerudo_Valley_Tent_Interior', 'Gerudos_Fortress_Interior', 'Desert_Colossus_Nayrus_Love_Interior',
		'Lakeside_Laboratory_Interior', 'Fishing_Pond_Interior', 'Lon_Lon_Ranch_Malons_House_Interior', 'Lon_Lon_Ranch_Stables_Interior', 'Lon_Lon_Ranch_Heart_Piece_Tower_Interior'
		]	

		self.adjacency = adjacencyList()
		self.string_to_ID_dictionary = {}
		self.ID_to_string_dictionary = {}
		self.initializeGraph()

		#Now setting the start and song location ID vals (or setting them to -1 if they are not known yet)
		self.childStartID = -1
		self.adultStartID = -1
		if self.isDefaultStartPoints:
			self.childStartID = self.string_to_ID_dictionary['Links_House_Interior']
			self.adultStartID = self.string_to_ID_dictionary['Temple_Of_Time_Prelude_Pedestal']

		#Now setting the location ID vals for the warp songs in the game (or setting them to -1 if they are not known yet)
		self.minuetID = -1
		self.boleroID = -1
		self.serenadeID = -1
		self.nocturneID = -1
		self.requiemID = -1
		self.preludeID = -1
		if self.isDefaultSongs:
			self.minuetID = self.string_to_ID_dictionary['Sacred_Forest_Meadow_Minuet_Pedestal']
			self.boleroID = self.string_to_ID_dictionary['DMC_Bolero_Pedestal']
			self.serenadeID = self.string_to_ID_dictionary['Lake_Hylia_Serenade_Pedestal']
			self.nocturneID = self.string_to_ID_dictionary['Graveyard_Nocturne_Pedestal']
			self.requiemID = self.string_to_ID_dictionary['Desert_Colossus_Requiem_Pedestal']
			self.preludeID = self.string_to_ID_dictionary['Temple_Of_Time_Prelude_Pedestal']
		self.hasMinuet = False
		self.hasBolero = False
		self.hasSerenade = False
		self.hasNocturne = False
		self.hasRequiem = False
		self.hasPrelude = False
		self.hasTempleOfTimeAccess = False

		self.string_to_ID_dictionary['Child_Save_Warp'] = -2
		self.ID_to_string_dictionary[-2] = 'Child_Save_Warp'
		
		self.string_to_ID_dictionary['Adult_Save_Warp'] = -3
		self.ID_to_string_dictionary[-3] = 'Adult_Save_Warp'
	
		self.string_to_ID_dictionary['Minuet'] = -4
		self.ID_to_string_dictionary[-4] = 'Minuet'

		self.string_to_ID_dictionary['Bolero'] = -5
		self.ID_to_string_dictionary[-5] = 'Bolero'

		self.string_to_ID_dictionary['Serenade'] = -6
		self.ID_to_string_dictionary[-6] = 'Serenade'

		self.string_to_ID_dictionary['Nocturne'] = -7
		self.ID_to_string_dictionary[-7] = 'Nocturne'

		self.string_to_ID_dictionary['Requiem'] = -8
		self.ID_to_string_dictionary[-8] = 'Requiem'

		self.string_to_ID_dictionary['Prelude'] = -9
		self.ID_to_string_dictionary[-9] = 'Prelude'

		self.string_to_ID_dictionary['Become_Adult'] = -10
		self.ID_to_string_dictionary[-10] = 'Become_Adult'

		self.string_to_ID_dictionary['Become_Child'] = -11
		self.ID_to_string_dictionary[-11] = 'Become_Child'
		

	def addReminder(self, myString):
		self.reminderList.append(myString)

	def editReminder(self, position, myString):
		self.reminderList[position] = myString

	def deleteReminder(self, position):
		self.reminderList.pop(position)

	def addLocationHelperFunction(self, newLocationName):
		newLocationID = self.adjacency.addNewNode()
		self.string_to_ID_dictionary[newLocationName] = newLocationID
		self.ID_to_string_dictionary[newLocationID] = newLocationName

	def initializeGraph(self):
		mainLocationsList = ['Kokiri_Forest', 'Lost_Woods', 'Sacred_Forest_Meadow', 'Zoras_River', 'Zoras_Domain', 'Zoras_Fountain',
		'Kakariko', 'Death_Mountain_Trail', 'Death_Mountain_Crater', 'Graveyard', 'Dampes_Grave', 'Windmill', 'Goron_City', 'Market_Entryway', 'Temple_Of_Time_Entryway',
		'Market', 'Temple_Of_Time', 'Castle', 'Gerudo_Valley', 'Gerudos_Fortress', 'Haunted_Wasteland', 'Desert_Colossus', 'Lake_Hylia',
		'Lon_Lon_Ranch', 'Hyrule_Field', 'Spirit_Temple' ]
		
		
		for mainLocationName in mainLocationsList:
			#Adding main location to dictionary and graph (ex. Hyrule Field)
			newMainLocationID = self.adjacency.addNewNode()
			self.string_to_ID_dictionary[mainLocationName] = newMainLocationID
			self.ID_to_string_dictionary[newMainLocationID] = mainLocationName
			
			for subLocation in self.entrances_locations_dictionary:
				#If the sublocation was in the main location, we add it to the dictionaries, and connect it to the main location in the graph with a weight of 0 in both directions
				if self.entrances_locations_dictionary[subLocation] == mainLocationName:
					newSubLocationID = self.adjacency.addNewNode()
					self.string_to_ID_dictionary[subLocation] = newSubLocationID
					self.ID_to_string_dictionary[newSubLocationID] = subLocation
					self.adjacency.addNewDestinationToSource(newMainLocationID, newSubLocationID, 0.0)
					self.adjacency.addNewDestinationToSource(newSubLocationID, newMainLocationID, 0.0)	
		
		#Now adding the dungeons to the graph and dictionaries
		for dungeon in self.dungeonLocations:
			if dungeon != 'Spirit_Temple':
				self.addLocationHelperFunction(dungeon)

		#Adding all of the interior houses to the graph and dictionaries
		for house in self.houseLocations:
			self.addLocationHelperFunction(house)

		self.addLocationHelperFunction("Generic_House_Interior_1")
		#Now adding all unique grottos to the graph and dictionaries. Grottos which are useless or repeat (ex. generic chest grotto) are NOT added.
		#A new generic grotto is added whenever the user finds a generic grotto.
		for grotto in self.grottoLocations:
			if grotto != 'Generic_Chest_Grotto_Interior' and grotto != 'Two_Business_Scrubs_Grotto_Interior' and grotto != 'Three_Business_Scrubs_Grotto_Interior' and grotto != 'One_Business_Scrub_Grotto_Interior' and grotto != 'Generic_Fairy_Fountain_Grotto_Interior' and grotto != 'Cow_Grotto_Interior' and grotto != 'Money_Grotto_Interior':
				self.addLocationHelperFunction(grotto)
			else:
				self.addLocationHelperFunction(grotto + "_1")
	
		kakPotionFront = self.string_to_ID_dictionary['Kak_Potion_Shop_Front_Interior']
		kakPotionBack = self.string_to_ID_dictionary['Kak_Potion_Shop_Back_Interior']
		self.adjacency.addNewDestinationToSource(kakPotionBack, kakPotionFront, 0.0)
		self.adjacency.addNewDestinationToSource(kakPotionFront, kakPotionBack, 0.0)

		dampeGraveInterior = self.string_to_ID_dictionary['Dampes_Grave_To_Windmill']
		windmillInterior = self.string_to_ID_dictionary['Windmill_From_Dampes_Grave']

		self.adjacency.addNewDestinationToSource(dampeGraveInterior, windmillInterior, 1.0)	


	def printAdjacencyListWithNames(self):
		print("Current Adjacency List: (source -> Destination1--WeightWeight1, Destination2-WeightWeight2...)")
		for element in self.adjacency.locationsList:
			print(self.ID_to_string_dictionary[element[0]], " -> ", end = "")
			currentLocationNode = element[1]
			while(currentLocationNode is not None):
				print(self.ID_to_string_dictionary[currentLocationNode.destination], "---Weight", str(currentLocationNode.weight), ", ", sep="", end = "")
				currentLocationNode = currentLocationNode.next
			print("", end = "\n")
		print()


	def printAdjacencyListWithNamesAbridged(self):
		print("Current Adjacency List (non-zero connections only): (source -> Destination1--WeightWeight1, Destination2-WeightWeight2...)")
		isNonZero = False
		for element in self.adjacency.locationsList:
			if self.ID_to_string_dictionary[element[0]] == 'Dampes_Grave_To_Windmill':
				continue
			isNonZero = False
			currentNode = element[1]
			while currentNode is not None:
				if currentNode.weight != 0.0:
					isNonZero = True
					break
				currentNode = currentNode.next
			if isNonZero == False:
				continue

			print(self.ID_to_string_dictionary[element[0]], " -> ", end = "")
			currentNode = element[1]
			while(currentNode is not None):
				print(self.ID_to_string_dictionary[currentNode.destination], "---Weight", str(currentNode.weight), ", ", sep = "", end = "")
				currentNode = currentNode.next
			print("", end = "\n")

		print()


	
	#AddLink() is used to add all links between entrances (except for setting starting locations and the locations of warp songs, which must be set seperately).	
	#If an entrance is supposed to be linked in a 2-way fashion with another entrance, then a link between each entrance to the other entrance is created in this function. Thus, to set a 2-way link between 2 entrances, this function need only be called once with one entrance arbitrarily made the source and the other as the destination
	#We return -2 if the source is an invalid source location
	#We return -1 if the destination is an invalid destination location
	#We return 0 if we added a link from the source to the destination only
	#We return 1 if we added a link from the source to the destination and a link from the destination to the source as well.
	def addLink(self, sourceID, destinationID):
		sourceLocationName = self.ID_to_string_dictionary[sourceID]
		destinationLocationName = self.ID_to_string_dictionary[destinationID]
		#Checking to see if the source location is somwehere that can only be a destination. If this is the case, then an error occured, and we return -1
		if sourceLocationName == 'Sacred_Forest_Meadow_Minuet_Pedestal' or sourceLocationName == 'DMC_Bolero_Pedestal' or sourceLocationName == 'Lake_Hylia_Serenade_Pedestal' or sourceLocationName == 'Graveyard_Nocturne_Pedestal' or sourceLocationName == 'Desert_Colossus_Requiem_Pedestal' or sourceLocationName == 'Temple_Of_Time_Prelude_Pedestal' or sourceLocationName == 'Kak_On_Roof' or sourceLocationName == 'Hyrule_Field_Owl_Dropoff':
			return -2 
		
		#Checking to see if the destination location is somewhere that can only be a source. If it is, then an error occured, and we return -2.
		if destinationLocationName == 'Lake_Hylia_Owl' or destinationLocationName == 'DMT_Owl':
			return -1

		#Since an entrance can only lead to one other destination, we now remove any other links from source that lead elsewhere:
		#Also, we need to remove all 2-way connections between the source and other locations
		for tempDestElem in self.adjacency.getAllNonZeroDestinationsOfSource(sourceID):
			for tempSourceElem in self.adjacency.getAllNonZeroDestinationsOfSource(tempDestElem):
				if tempSourceElem == sourceID:
					self.adjacency.removeConnection(tempDestElem, tempSourceElem)

			self.adjacency.removeConnection(sourceID, tempDestElem)

		#Now adding connection with a weight of 1:
		self.adjacency.addNewDestinationToSource(sourceID, destinationID, 1.0)

		#If any of these condtions are true, then there is no connection back from the destination to the source. Therefore, we can 
		#Succesfully return with a code of 0
		if self.isDecoupled == True or sourceLocationName == 'Lake_Hylia_Owl' or sourceLocationName == 'DMT_Owl' or destinationLocationName == 'Sacred_Forest_Meadow_Minuet_Pedestal' or destinationLocationName == 'DMC_Bolero_Pedestal' or destinationLocationName == 'Lake_Hylia_Serenade_Pedestal' or destinationLocationName == 'Graveyard_Nocturne_Pedestal' or destinationLocationName == 'Desert_Colossus_Requiem_Pedestal' or destinationLocationName == 'Temple_Of_Time_Prelude_Pedestal' or destinationLocationName == 'Kak_On_Roof' or destinationLocationName == 'Hyrule_Field_Owl_Dropoff':
			return 0
		
		#Otherwise, we need to add a connection from the destination back to the source...
		#First, we have to remove any links that already exist from the destination to any other locations
		#Also, we need to remove all 2-way connections between the destination and another location
		for tempDestElem in self.adjacency.getAllNonZeroDestinationsOfSource(destinationID):
			for tempSourceElem in self.adjacency.getAllNonZeroDestinationsOfSource(tempDestElem):
				if tempSourceElem == destinationID:
					self.adjacency.removeConnection(tempDestElem, tempSourceElem)

			self.adjacency.removeConnection(destinationID, tempDestElem)

		#Now adding connection with a weight of 1:
		self.adjacency.addNewDestinationToSource(destinationID, sourceID, 1.0)

		#Now returning succesfully with a code of 1
		return 1

	def getIDHelperFunc(self, name):
		return self.string_to_ID_dictionary[name]

	
	#Returns true if myName is a repeating/generic grotto name or generic house, and false otherwise
	def isGenGrotto(self, myName):
		if 'Generic_Chest_Grotto_Interior' in myName or 'Two_Business_Scrubs_Grotto_Interior' in myName or 'Three_Business_Scrubs_Grotto_Interior' in myName or 'One_Business_Scrub_Grotto_Interior' in myName or 'Generic_Fairy_Fountain_Grotto_Interior' in myName or 'Cow_Grotto_Interior' in myName or 'Money_Grotto_Interior' in myName or 'Generic_House_Interior' in myName:
			return True
		else:
			return False


	#Takes as input a generic grotto/house name, and outputs true if this is the last of its kind
	def isLastGenGrotto(self, myName):
		stringList = myName.split("_")
		grotNum = int(stringList[len(stringList) - 1])
		i = len(myName) - 1
		baseString = ""
		while i > 0:
			if myName[i] == '_':
				baseString = myName[0:i]
				break
			i -= 1
		if baseString == "":
			return

		for location in self.string_to_ID_dictionary:
			if baseString in location:
				stringList = location.split("_")
				newNum = int(stringList[len(stringList) - 1])
				if newNum > grotNum:
					return False
		return True


	#Adds a new grotto/house of the same type as myName to the dictionaries (assumes myName is the last of its kind/highest number in the dictionary)
	def addGenGrotto(self, myName):
		stringList = myName.split("_")
		grotNum = int(stringList[len(stringList) - 1])
		i = len(myName) - 1
		baseString = ""
		while i > 0:
			if myName[i] == '_':
				baseString = myName[0:i]
				break
			i -= 1
		if baseString == "":
			return
	
		self.addLocationHelperFunction(baseString + "_" + str(grotNum + 1))


	def addLinkBetweenStrings(self, string1, string2):
		if self.isGenGrotto(string1) and self.isLastGenGrotto(string1):
			self.addGenGrotto(string1)
		if self.isGenGrotto(string2) and self.isLastGenGrotto(string2):
			self.addGenGrotto(string2)

		return self.addLink(self.getIDHelperFunc(string1), self.getIDHelperFunc(string2))		

	#Returns the id of the closest node in the unvisited array, and pops it from the unvisited array
	def getShortestUnvisitedHelper(self, unvisitedArray, distanceDictionary):
		shortestIndex = 0 #index in the unvisited array
		shortestSize = distanceDictionary[unvisitedArray[shortestIndex]] #the smallest number found in the distanceDictionary
		for index in range(1, len(unvisitedArray)):
			if distanceDictionary[unvisitedArray[index]] < shortestSize:
				shortestSize = distanceDictionary[unvisitedArray[index]]
				shortestIndex = index
		return unvisitedArray.pop(shortestIndex)
		 

	#findShortestPath takes as input the ID number of the source location (ex. the ID for Kokiri_Forest) and the ID number of the 
	#destination location (ex. the ID for Fire_Temple). The function also takes as input an exclusion list, which is a list whose
	#entries are lists of the form [source, dest], which represents a connection that should be excluded from the search
	#For example, if exclusionList = [ [3, 5], [4, 2] ], then that means that the connection from node 3 to node 5 may not be used
	#in the search, and the connection from node 4 to node 2 may not be used in the search. If there are no excluded terms, then
	#the exclusion list should be the empty list (i.e. [])
		

	#The function returns a list of the IDs of the nodes which are traversed in the shortest path, along with the total length of the path (this is a list of 2 items)
	#For example, if the function returned [ [4, 5, 6, 8], 10 ], that would mean that the shortest path from node 4 to node 8 is to travel from node 4 to node 5, from node 5 to node 6, and from node 6 to node 8. Additionally, this path would have a cost of 10
	#If the source is the destination, then [ [], 0] will be returned.
	#If there is no path from the source to the destination, then None is returned
	
	#NOTE: This function uses Dijkstra's Algorithm
	def findShortestPath(self, sourceID, destinationID, exclusionList):
		adjacencyCopy = deepcopy(self.adjacency)
		if exclusionList is not None and exclusionList != []:
			for pair in exclusionList:
				adjacencyCopy.removeConnection(pair[0], pair[1])	
		if sourceID == destinationID:
			return [[], 0]
		unvisitedArray = [] #Format: [4, 5, 6], where nodes 4, 5 and 6 have not been visited yet
		distanceDictionary = {} #Format: { 3 : 4, 5 : 2, 1 : +INF }, where node 3 is 4 away from the start with the shortest found path (so far), node 5 is 2 away, and node 1 is inifinite distance away (i.e. no path has been found to it yet)
		prevDictionary = {} #Format: {3 : 4, 4 : 0, 1 : -1 }, where the shortest path to node 3 (so far) involves going through node 4, node 4 is the start node, and no path to node 1 has been found yet
		for element in adjacencyCopy.locationsList:
			if element[0] == sourceID:
				distanceDictionary[element[0]] = 0.0
			else:
				distanceDictionary[element[0]] =  math.inf
			unvisitedArray.append(element[0])
			prevDictionary[element[0]] =  -1
	
		while len(unvisitedArray) > 0:
			currentNodeID = self.getShortestUnvisitedHelper(unvisitedArray, distanceDictionary)
			if currentNodeID == destinationID:
				break
			if distanceDictionary[currentNodeID] == math.inf:
				return None
			#Now getting the node in the adjacency list with the ID of currentNodeID:
			sourceElement = None
			for element in adjacencyCopy.locationsList:
				if element[0] == currentNodeID:
					sourceElement = element
					break

			#Now iterating through the neighbors of this node...
			neighborNode = sourceElement[1]
			while neighborNode is not None:
				if neighborNode.destination in unvisitedArray and distanceDictionary[currentNodeID] + neighborNode.destination < distanceDictionary[neighborNode.destination]:
					distanceDictionary[neighborNode.destination] = distanceDictionary[currentNodeID] + neighborNode.weight
					prevDictionary[neighborNode.destination] = currentNodeID
				neighborNode = neighborNode.next


			#Now getting the path from the source to the target:
		finalPath = []
		iterationID = destinationID
		while prevDictionary[iterationID] != -1:
			finalPath.insert(0, iterationID)
			iterationID = prevDictionary[iterationID]
	
		finalPath.insert(0, sourceID)
		return [finalPath, distanceDictionary[destinationID]]

	def findShortestPathString(self, location1, location2, exclusionList):
		return self.findShortestPath(self.string_to_ID_dictionary[location1], self.string_to_ID_dictionary[location2], exclusionList)
	
	def locationIsDefined(self, myLocation):
		if myLocation in self.string_to_ID_dictionary:
			return True
		return False


	#SongName is either Minuet, Bolero, Serenade, Nocturne, Requiem, or Prelude (corresponding to the song that will be set). locID is unused if isDefaultSongs is True.
	#This function sets a flag that the user has the song passed in as an argument, and if isDefaultSongs is False, then it sets the location of the warp song to the
	#number stored in locID. Note that this function can also be called again to change the location that a warp song takes you if the user made a mistake typing
	#in the location. 
	def setSongFound(self, songName, locID = -1):

		if songName == 'Minuet':
			self.hasMinuet = True
			if self.isDefaultSongs == False:
				self.minuetID = locID

		elif songName == 'Bolero':
			self.hasBolero = True
			if self.isDefaultSongs == False:
				self.boleroID = locID

		elif songName == 'Serenade':
			self.hasSerenade = True
			if self.isDefaultSongs == False:
				self.serenadeID = locID

		elif songName == 'Nocturne':
			self.hasNocturne = True
			if self.isDefaultSongs == False:
				self.nocturneID = locID

		elif songName == 'Requiem':
			self.hasRequiem = True
			if self.isDefaultSongs == False:
				self.requiemID = locID

		elif songName == 'Prelude':
			self.hasPrelude = True
			if self.isDefaultSongs == False:
				self.preludeID = locID

		else:
			print("Error: Song name in setSongFound() function was " + str(songName) + ". The only valid options were Minuet, Bolero, Serenade, Nocturne, Requiem & Prelude.")


	#Deletes a song from the user's inventory (if the user accidentilly said they have a song which they don't really have).
	def removeSongFromInventory(self, songName):
		if songName == 'Minuet':
			self.hasMinuet = False
		elif songName == 'Bolero':
			self.hasBolero = False
		elif songName == 'Serenade':
			self.hasSerenade = False
		elif songName == 'Nocturne':
			self.hasNocturne = False
		elif songName == 'Requiem':
			self.hasRequiem = False
		elif songName == 'Prelude':
			self.hasPrelude = False
		else:
			print("Error: Unknown song named " + str(songName) + " was passed as an argument to removeSongFromInventory. Valid songNames are Minuet, Bolero, Serenade, Nocturne, Requiem, and Prelude")


	def setChildSpawnPoint(self, spawnID):
		if self.isDefaultStartPoints:
			print("Error: setChildSpawnPoint() can only be called if the defaultStartPoints option is turned off...")
		else:
			self.childStartID = spawnID

	
	def setAdultSpawnPoint(self, spawnID):
		if self.isDefaultStartPoints:
			print("Error: setAdultSpawnPoint() can only be called if the defaultStartPoints option is turned off...")
		else:
			self.adultStartID = spawnID



	def removeUselessNodesHelperFunction(self, pathList):
		myPath = pathList[0]
		index = 0
		while index < len(myPath) - 1:
			myConnection = self.adjacency.getConnection(myPath[index], myPath[index + 1])
			if index != 0 and index + 1 != len(myPath) - 1 and myConnection is not None and myConnection.weight == 0.0:
				myPath.pop(index + 1)
				index -= 1
			index += 1	


	def combineLists(self, list1, list2):
		if list1 is None or list2 is None:
			return None

		finalList = list1
		finalList[1] = finalList[1] + list2[1]

		for element in list2[0]:
			finalList[0].append(element)

		return finalList

	#Returns the shortest path from source to destination, including warp songs and save warping. 
	#Additionally, the resulting path has all connections with a weight of 0 stripped out of it for readability.
	#Essentially, this function calls the Dijkstra's algorithm function with several different starting locations to
	#Figure out whether it is faster to warp somewhere or to start from where we are
	def fullGetShortestPathAlgorithm(self, startingID, destinationID, exclusionList, specialExclusionList, isChild):
		originalPath = self.findShortestPath(startingID, destinationID, exclusionList)

		childSpawnPath = None
		adultSpawnPath = None

		minuetPath = None
		boleroPath = None
		serenadePath = None
		nocturnePath = None
		requiemPath = None
		preludePath = None
		changeAgePath = None

		finalPathChoice = None
		if isChild and self.childStartID != -1 and self.string_to_ID_dictionary['Child_Save_Warp'] not in specialExclusionList:
			childSpawnPath = addOneToPathHelper(self.findShortestPath(self.childStartID, destinationID, exclusionList), self.string_to_ID_dictionary['Child_Save_Warp'])
		elif isChild == False and self.adultStartID != -1 and self.string_to_ID_dictionary['Adult_Save_Warp'] not in specialExclusionList:
			adultSpawnPath = addOneToPathHelper(self.findShortestPath(self.adultStartID, destinationID, exclusionList), self.string_to_ID_dictionary['Adult_Save_Warp'])

		if self.hasMinuet and self.minuetID != -1 and self.string_to_ID_dictionary['Minuet'] not in specialExclusionList:
			minuetPath = addOneToPathHelper(self.findShortestPath(self.minuetID, destinationID, exclusionList), self.string_to_ID_dictionary['Minuet'])

		if self.hasBolero and self.boleroID != -1 and self.string_to_ID_dictionary['Bolero'] not in specialExclusionList:
			boleroPath = addOneToPathHelper(self.findShortestPath(self.boleroID, destinationID, exclusionList), self.string_to_ID_dictionary['Bolero'])
	
		if self.hasSerenade and self.serenadeID != -1 and self.string_to_ID_dictionary['Serenade'] not in specialExclusionList:
			serenadePath = addOneToPathHelper(self.findShortestPath(self.serenadeID, destinationID, exclusionList), self.string_to_ID_dictionary['Serenade'])

		if self.hasNocturne and self.nocturneID != -1 and self.string_to_ID_dictionary['Nocturne'] not in specialExclusionList:
			nocturnePath = addOneToPathHelper(self.findShortestPath(self.nocturneID, destinationID, exclusionList), self.string_to_ID_dictionary['Nocturne'])

		if self.hasRequiem and self.requiemID != -1 and self.string_to_ID_dictionary['Requiem'] not in specialExclusionList:
			requiemPath = addOneToPathHelper(self.findShortestPath(self.requiemID, destinationID, exclusionList), self.string_to_ID_dictionary['Requiem'])

		if self.hasPrelude and self.preludeID != -1 and self.string_to_ID_dictionary['Prelude'] not in specialExclusionList:
			preludePath = addOneToPathHelper(self.findShortestPath(self.preludeID, destinationID, exclusionList), self.string_to_ID_dictionary['Prelude'])

		lowestCost = math.inf
		if originalPath is not None and originalPath[1] < lowestCost:
			lowestCost = originalPath[1]
			finalPathChoice = originalPath

		if childSpawnPath is not None and childSpawnPath[1] < lowestCost:
			lowestCost = childSpawnPath[1]
			finalPathChoice = childSpawnPath

		if adultSpawnPath is not None and adultSpawnPath[1] < lowestCost:
			lowestCost = adultSpawnPath[1]	
			finalPathChoice = adultSpawnPath

		if minuetPath is not None and minuetPath[1] < lowestCost:
			lowestCost = minuetPath[1]
			finalPathChoice = minuetPath

		if boleroPath is not None and boleroPath[1] < lowestCost:
			lowestCost = boleroPath[1]
			finalPathChoice = boleroPath

		if serenadePath is not None and serenadePath[1] < lowestCost:
			lowestCost = serenadePath[1]
			finalPathChoice = serenadePath

		if nocturnePath is not None and nocturnePath[1] < lowestCost:
			lowestCost = nocturnePath[1]
			finalPathChoice = nocturnePath

		if requiemPath is not None and requiemPath[1] < lowestCost:
			lowestCost = requiemPath[1]
			finalPathChoice = requiemPath

		if preludePath is not None and preludePath[1] < lowestCost:
			lowestCost = preludePath[1]
			finalPathChoice = preludePath


		if self.hasTempleOfTimeAccess == True and self.ID_to_string_dictionary[destinationID] != 'Temple_Of_Time_Front_Interior' and self.ID_to_string_dictionary[destinationID] != 'Temple_Of_Time_Prelude_Pedestal':
			ToTPath = [[], 0]
			if self.ID_to_string_dictionary[startingID] != 'Temple_Of_Time_Front_Interior' and self.ID_to_string_dictionary[startingID] != 'Temple_Of_Time_Prelude_Pedestal':
				ToTPath = self.fullGetShortestPathAlgorithm(startingID, self.string_to_ID_dictionary['Temple_Of_Time_Front_Interior'], exclusionList, specialExclusionList, isChild)	
			if isChild == True and self.adultStartID != -1 and self.string_to_ID_dictionary['Become_Adult'] not in specialExclusionList:	
				if ToTPath is not None:
					ToTPath[0].append(self.string_to_ID_dictionary['Become_Adult'])
					ToTPath[1] = ToTPath[1] + 1.0
					ToTPath[0].append(self.string_to_ID_dictionary['Adult_Save_Warp'])
					ToTPath[1] = ToTPath[1] + 1.0
					lastPartPath = self.findShortestPath(self.adultStartID, destinationID, exclusionList)


					if(lastPartPath is not None):
						lastPartPath = self.combineLists(ToTPath, lastPartPath)
						if lastPartPath[1] < lowestCost:
							lowestCost = lastPartPath[1]
							finalPathChoice = lastPartPath


			elif isChild == False and self.childStartID != -1 and self.string_to_ID_dictionary['Become_Child'] not in specialExclusionList:
				if ToTPath is not None:
					ToTPath[0].append(self.string_to_ID_dictionary['Become_Child'])
					ToTPath[1] = ToTPath[1] + 1.0
					ToTPath[0].append(self.string_to_ID_dictionary['Child_Save_Warp'])
					ToTPath[1] = ToTPath[1] + 1.0
					lastPartPath = self.findShortestPath(self.childStartID, destinationID, exclusionList)
	
					if(lastPartPath is not None):
						lastPartPath = self.combineLists(ToTPath, lastPartPath)
						if lastPartPath[1] < lowestCost:
							lowestCost = lastPartPath[1]
							finalPathChoice = lastPartPath
		



	
		if finalPathChoice is not None:
			self.removeUselessNodesHelperFunction(finalPathChoice)

		return finalPathChoice

	def writeDataToFile(self, fileName):
		myFile = open(fileName, "w")
		writeString = ""
		#Setting up the string_to_ID dictionary
		for ID in self.ID_to_string_dictionary:
			writeString += ( str(ID) + ":")
			writeString += self.ID_to_string_dictionary[ID]
			writeString += "\n"
		writeString += "|\n"
		myFile.write(writeString)
		writeString = ""
		#Writing out the contents of the adjacency list
		for sourceElement in self.adjacency.locationsList:
			writeString += (str(sourceElement[0]) + ":")
			travelNode = sourceElement[1]
			while travelNode is not None:
				writeString += str(travelNode.destination) + "/" + str(travelNode.weight)
				travelNode = travelNode.next
				if travelNode is not None:
					writeString += ","
			writeString += "\n" 
		writeString += "|\n"
		myFile.write(writeString)
		writeString = ""
		#Lastly, writing out various flags to the bottom of the file.
		writeString += "hasMinuet:"
		if self.hasMinuet: 
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "minuetID:" + str(self.minuetID) + "\n"

		writeString += "hasBolero:"
		if self.hasBolero:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "boleroID:" + str(self.boleroID) + "\n"

		writeString += "hasSerenade:"
		if self.hasSerenade:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "serenadeID:" + str(self.serenadeID) + "\n"

		writeString += "hasNocturne:"
		if self.hasNocturne:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "nocturneID:" + str(self.nocturneID) + "\n"

		writeString += "hasRequiem:"
		if self.hasRequiem:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "requiemID:" + str(self.requiemID) + "\n"

		writeString += "hasPrelude:"
		if self.hasPrelude:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "preludeID:" + str(self.preludeID) + "\n"

		writeString += "childStartID:" + str(self.childStartID) + "\n"
		writeString += "adultStartID:" + str(self.adultStartID) + "\n"

		writeString += "isDecoupled:"
		if self.isDecoupled:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "isDefaultStartPoints:"
		if self.isDefaultStartPoints:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "isDefaultSongs:"
		if self.isDefaultSongs:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "hasTempleOfTimeAccess:"
		if self.hasTempleOfTimeAccess:
			writeString += "True\n"
		else:
			writeString += "False\n"
            
		writeString += "isAutosaveOn:"
		if self.isAutosaveOn:
			writeString += "True\n"
		else:
			writeString += "False\n"

		writeString += "|\n"
		for reminder in self.reminderList:
			print(reminder + "\n")

		writeString += "|\n"
		myFile.write(writeString)
		myFile.close()
		return 0

	#Constructs the OOT_Locations_Graph object from the file	
	def readDataFromFile(self, fileName):
		#First, clearing the contents of the current object.
		self.string_to_ID_dictionary = {}
		self.ID_to_string_dictionary = {}
		self.adjacency.locationsList = []
		self.adjacency.lastNodeAdded = -1
		self.reminderList = []
		
		#Now attempting to open the file...
		myFile = ""
		#Exit the readFile() function with an error code of -2 if an exception occurs trying to open the file
		try:
			myFile = open(fileName, "r")
		except (OSError, IOError) as e:
			return -4

		fileContents = myFile.read()
		myFile.close()
		fileLines = fileContents.split("\n")

		#This will be set to the value of the line after the string_to_id_dictionary of the file ends
		endOfDictionaryIndex = -1
		for index in range(0, len(fileLines)):
			currLine = fileLines[index].strip()
			if currLine == '|':
				endOfDictionaryIndex = index + 1
				break
			if len(currLine) == 0:
				continue
			splitLine = currLine.split(":")
			if len(splitLine) != 2:
				return -3
			integerID = -1
			try:
				integerID = int(splitLine[0])
			except ValueError:
				return -3
			stringName = splitLine[1]
			self.string_to_ID_dictionary[stringName] = integerID
			self.ID_to_string_dictionary[integerID] = stringName			

		if endOfDictionaryIndex == -1:
			return -3

		#Now setting up the graph of nodes
		indexOfEndOfGraph = -1
		for index in range(endOfDictionaryIndex, len(fileLines)):	
			if fileLines[index].strip() == '|':
				indexOfEndOfGraph = index
				break
		if indexOfEndOfGraph == -1:
			return -2
		graphLines = fileLines[endOfDictionaryIndex:indexOfEndOfGraph]
		
		if(self.adjacency.createGraphFromLines(graphLines) != 0):
			print("Error When creating graph!")
			return -2

		indexAtRemainderStart = -1
		#Now setting various flags and song IDs
		for index in range(indexOfEndOfGraph + 1, len(fileLines)):
			currLine = fileLines[index].strip()
			if len(currLine) == 0:
				continue
			if currLine == "|":
				indexAtRemainderStart = index + 1
				break

			splitLine = currLine.split(":")
			if len(splitLine) != 2:
				return -1
			myProperty = splitLine[0]
			myValue = splitLine[1]

			if myProperty[0:3] == 'has' or myProperty[0:2] == 'is':
				if myValue == "True":
					myValue = True
				elif myValue == "False":
					myValue = False
				else:
					return -1
			else:
				try:
					myValue = int(myValue)
				except ValueError:
					return -1	

			if myProperty == 'hasMinuet':
				self.hasMinuet = myValue
			elif myProperty == 'minuetID':
				self.minuetID = myValue
			elif myProperty == 'hasBolero':
				self.hasBolero = myValue
			elif myProperty == 'boleroID':
				self.boleroID = myValue
			elif myProperty == 'hasSerenade':
				self.hasSerenade = myValue
			elif myProperty == 'serenadeID':
				self.serenadeID = myValue
			elif myProperty == 'hasNocturne':
				self.hasNocturne = myValue
			elif myProperty == 'nocturneID':
				self.nocturneID = myValue
			elif myProperty == 'hasRequiem':
				self.hasRequiem = myValue
			elif myProperty == 'requiemID':
				self.requiemID = myValue
			elif myProperty == 'hasPrelude':
				self.hasPrelude = myValue
			elif myProperty == 'preludeID':
				self.preludeID = myValue
			elif myProperty == 'childStartID':
				self.childStartID = myValue
			elif myProperty == 'adultStartID':
				self.adultStartID = myValue
			elif myProperty == 'isDecoupled':
				self.isDecoupled = myValue
			elif myProperty == 'isDefaultStartPoints':
				self.isDefaultStartPoints = myValue
			elif myProperty == 'isDefaultSongs':
				self.isDefaultSongs = myValue
			elif myProperty == 'hasTempleOfTimeAccess':
				self.hasTempleOfTimeAccess = myValue
			elif myProperty == 'isAutosaveOn':
				self.isAutosaveOn = myValue
			else:
				return -1

		for index in range(indexAtRemainderStart, len(fileLines)):
			currLine = fileLines[index].strip()
			if len(currLine) == 0:
				continue
			if(currLine == "|"):
				break
			self.reminderList.append(currLine)

		#Success!
		return 0



	def isExemptFromArea(self, myKey):
		sourceLocationName = myKey
		if sourceLocationName == 'Sacred_Forest_Meadow_Minuet_Pedestal' or sourceLocationName == 'DMC_Bolero_Pedestal' or sourceLocationName == 'Lake_Hylia_Serenade_Pedestal' or sourceLocationName == 'Graveyard_Nocturne_Pedestal' or sourceLocationName == 'Desert_Colossus_Requiem_Pedestal' or sourceLocationName == 'Temple_Of_Time_Prelude_Pedestal' or sourceLocationName == 'Kak_On_Roof' or sourceLocationName == 'Hyrule_Field_Owl_Dropoff':
			return True
		return False



	def allLocationsInAreaSet(self, areaNameString):
		validFlag = False
		for myKey in self.entrances_locations_dictionary:
			if self.entrances_locations_dictionary[myKey] == areaNameString:
				validFlag = True
				if self.adjacency.getAllNonZeroDestinationsOfSource(self.string_to_ID_dictionary[myKey]) == [] and not self.isExemptFromArea(myKey):
					return False
		if validFlag == False:
			print("ERROR: Invalid name passed into allLocationsInAreaSet(). Area name was: " + str(areaNameString))
		return True			

def addLinkTestFunc(myGraph, location1, location2):
	print("Adding a link between " + location1 + " and " + location2 + "...")
	returnCode = myGraph.addLinkBetweenStrings(location1, location2)
	if returnCode == -2:
		print("Error: Could not add link because " + location1 + " can only be a destination, not a source!")
	elif returnCode == -1:
		print("Error: Could not add link because " + location2 + " can only be a source, not a destination")
	elif returnCode == 0:
		print("Added link between " + location1 + " and " + location2 + ", but not the reverse (a 1-way entrance added).")
	else:
		print("Added link between " + location1 + " and " + location2 + " and the reverse (a 2-way entrance added)")

	print("After attempting to add link, here is the new adridged adjacency list: \n")
	myGraph.printAdjacencyListWithNamesAbridged()

def pathFindingTester(graph, loc1, loc2, exclusionStringList, specialExclusionStringList, isChild):
	if(graph.locationIsDefined(loc1) == False):
		print("Error: source " + loc1 + " was undefined")
		return
	if(graph.locationIsDefined(loc2) == False):
		print("Error: destination " + loc2 + " was undefined")
		return
	
	realExclusionList = []
	realSpecialExclusionList = []
	if(exclusionStringList != []):
		print("Exclusion List:\n")
	for tempList in exclusionStringList:
		if(graph.locationIsDefined(tempList[0]) == False):
			print("Error: in the exclusion list, " + tempList[0] + " was undefined!")
			return
		if(graph.locationIsDefined(tempList[1]) == False):
			print("Error: in the exclusion list, " + tempList[1] + " was undefined!")
			return
		print(tempList[0] + " --> " + tempList[1])
		realExclusionList.append([graph.string_to_ID_dictionary[tempList[0]], graph.string_to_ID_dictionary[tempList[1]]])

	if(specialExclusionStringList != []):
		print("Special exclusion list:\n")

	for element in specialExclusionStringList:
		if(graph.locationIsDefined(element) == False):
			print("Error: in the special exclusion list, " + str(element) + " was undefined!")
			return
		realSpecialExclusionList.append(graph.string_to_ID_dictionary[element])
		print(element)

	if isChild:
		print("Age: Child")
	else:
		print("Age: Adult")

	myPath = graph.fullGetShortestPathAlgorithm(graph.string_to_ID_dictionary[loc1], graph.string_to_ID_dictionary[loc2], realExclusionList, realSpecialExclusionList, isChild)
	if myPath is None:
		print("No path found from " + loc1 + " to " + loc2)
		return
	else:
		print("Shortest path found from " + loc1 + " to " + loc2 + " had total cost of " + str(myPath[1]))
		print("Now printing the nodes of the path in order:\n\n")
		for nodeID in myPath[0]:
			print(graph.ID_to_string_dictionary[nodeID] + " -->  ", end="")
	print("\n")


if __name__ == '__main__':
	OOTGraph = OOT_Locations_Graph(False, False, True)
	OOTGraph.setChildSpawnPoint(OOTGraph.string_to_ID_dictionary['Bombchu_Bowling_Interior'])
	OOTGraph.setAdultSpawnPoint(OOTGraph.string_to_ID_dictionary['Mask_Shop_Interior'])
	"""print("Abridged adjacency list to start off with: ")
	OOTGraph.printAdjacencyListWithNamesAbridged()
	addLinkTestFunc(OOTGraph, 'Kokiri_To_Lost_Woods', 'Kak_To_Hyrule_Field')
	addLinkTestFunc(OOTGraph, 'Zoras_River_To_Hyrule_Field', 'Castle_To_Market')
	addLinkTestFunc(OOTGraph, 'Castle_To_Market', 'Kokiri_To_Lost_Woods')
	addLinkTestFunc(OOTGraph, 'Lake_Hylia_Owl', 'Castle_To_Market')
	addLinkTestFunc(OOTGraph, 'Castle_To_Market', 'Lake_Hylia_Owl')
	addLinkTestFunc(OOTGraph, 'Lake_Hylia_Serenade_Pedestal', 'Hyrule_Field_To_Lake_Hylia')
	addLinkTestFunc(OOTGraph, 'Hyrule_Field_To_Lake_Hylia', 'Lake_Hylia_Serenade_Pedestal')
	addLinkTestFunc(OOTGraph, 'DMT_Owl', 'Sacred_Forest_Meadow_Minuet_Pedestal')
	addLinkTestFunc(OOTGraph, 'Sacred_Forest_Meadow_Minuet_Pedestal', 'DMT_Owl')
	addLinkTestFunc(OOTGraph, 'Grave_With_Shield_Chest_Interior', 'Kak_To_Redead_Grotto')
	addLinkTestFunc(OOTGraph, 'Kak_House_Of_Skulltula_Interior', 'Kak_To_Redead_Grotto')
	addLinkTestFunc(OOTGraph, 'Kokiri_To_Lost_Woods', 'Graveyard_To_Kak')
	addLinkTestFunc(OOTGraph, 'Zoras_Domain_To_Zoras_River', 'Lon_Lon_Ranch_To_Hyrule_Field')
	addLinkTestFunc(OOTGraph, 'Kokiri_To_Lost_Woods', 'Lon_Lon_Ranch_To_Hyrule_Field')
	addLinkTestFunc(OOTGraph, 'Castle_To_Market', 'Gerudo_Valley_To_Hyrule_Field')
	addLinkTestFunc(OOTGraph, 'Lon_Lon_Ranch_To_Hyrule_Field', 'Castle_To_Market')
	OOTGraph.findShortestPath(1, 2, [])"""
	myFile = open("ootRegLinks.txt", "r")
	for line in myFile:
		if line is None or line == "":
			continue
		myLine = line.strip()
		if len(myLine) == 0:
			continue
		splitList = myLine.split(":")
		sourceName = splitList[0]
		destinationName = splitList[1]
		if(OOTGraph.locationIsDefined(sourceName) == False):
			print("Error: source location " + sourceName + " was not defined! terminating now!")
			exit(1)
		if(OOTGraph.locationIsDefined(destinationName) == False):
			print("Error: destination location " + destinationName + " was not defined! Terminating now!")
			exit(1)
		OOTGraph.addLinkBetweenStrings(sourceName, destinationName)		
	OOTGraph.setSongFound('Bolero')
	OOTGraph.setSongFound('Prelude')
	OOTGraph.setSongFound('Serenade')
	OOTGraph.setSongFound('Nocturne')
	OOTGraph.setSongFound('Requiem')
	OOTGraph.setSongFound('Minuet')
	OOTGraph.hasTempleOfTimeAccess = True	
	OOTGraph.addLinkBetweenStrings("Generic_Chest_Grotto_Interior_1", "Kokiri_To_SoS_Grotto")
	OOTGraph.printAdjacencyListWithNames()
	"""
	pathFindingTester(OOTGraph, "Links_House_Interior", "Fire_Temple", [], [], True)
	pathFindingTester(OOTGraph, "Zoras_River", "Lake_Hylia", [], [], True)
	pathFindingTester(OOTGraph, "Temple_Of_Time_Front_Interior", "Mask_Shop_Interior", [], [], True)
	pathFindingTester(OOTGraph, "Gerudo_Valley", "Zoras_River", [], [], False)
	pathFindingTester(OOTGraph, "Kokiri_Forest", "Graveyard", [], ['Nocturne'], False)
	pathFindingTester(OOTGraph, "Temple_Of_Time_Prelude_Pedestal", "Market_Potion_Shop_Interior", [], ['Prelude', 'Bolero'], False)
	pathFindingTester(OOTGraph, "Death_Mountain_Crater", "Haunted_Wasteland", [], [], False)
	pathFindingTester(OOTGraph, "Links_House_Interior", "Graveyard", [], [], False)
	pathFindingTester(OOTGraph, "Links_House_Interior", "Temple_Of_Time_Front_Interior", [], [], False)
	OOTGraph.writeDataToFile("myTestFile.txt")
	newGraph = OOT_Locations_Graph(False, False, True)
	errorCode =  newGraph.readDataFromFile("myTestFile.txt")
	if errorCode != 0:
		print("Error number " + str(errorCode) + " occured when reading from file!")
	newGraph.writeDataToFile("myTestFile2.txt")
	"""
