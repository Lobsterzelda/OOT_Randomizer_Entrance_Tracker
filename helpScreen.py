from tkinter import *

try:
	from tkmacosx import *
except:
	pass


class helpScreen:
	def __init__(self, parentScreen):
		self.parentScreen = parentScreen
		self.gui = Toplevel(bg = "white")
		self.gui.title('Help')
		self.gui.geometry('1400x1400')
		
		self.mainCanvas = Canvas(self.gui, bg = "white")
		self.mainCanvas.pack(side = LEFT, expand = True, fill = BOTH)

		self.verticalScroll = Scrollbar(self.gui)
		self.verticalScroll.pack(side = RIGHT, fill = Y)
		
		self.mainCanvas.config(yscrollcommand = self.verticalScroll.set)
		self.verticalScroll.config(command = self.mainCanvas.yview)

		self.mainCanvas.configure(scrollregion = (0, 0, 5000, 4065))

		lastHeight = 10
		self.mainCanvas.create_text(670, lastHeight, text = 'Help:', fill = 'red', font = 'Heveltica 32 bold', anchor = NW) 


		lastHeight += 40

		headerWidth = 50
		mainTextWidth = 100
		subTextWidth = 150
		extraSubTextWidth = 200
		bulletOffset = 50

		self.mainCanvas.create_text(headerWidth, lastHeight, text = "Getting Started:", fill = "purple", font = "Heveltica 24 bold", anchor = NW)	

		lastHeight += 40

		self.mainCanvas.create_text(mainTextWidth, lastHeight, width = 1000, fill = "black", font = "Hevletica 16", anchor = NW, text = "Welcome to Lobsterzelda's OOT Entrance Randomizer Tracker! To get started, you can click on the new randomizer button on the home screen in order to create a new randomizer seed. Additionally, you can click on the Load Randomizer button on the home screen in order to load a randomizer seed you have already created. Note that both of these options can also be accesed via the File menu at the top of the screen.")


		lastHeight += 100

		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", anchor = NW, text = "Creating A New Randomizer Tracker:")

		lastHeight += 40

		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "Once you click on the New Randomizer button, the New Randomzier menu will open up. On this menu, you have several options you can check off, which correspond to various properties of your randomizer seed:")

		lastHeight += 60

		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)

		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Has Default Start Points After Savewarping:")

		lastHeight += 25
	
		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "If this option is checked off, then that means that in your seed, when you savewarp, you respawn at the vanilla locations in OOT (i.e., you spawn in link's house as a child and the Temple Of Time as an adult after savewarping). Note that if this option is checked off, then you won't be able to change where you spawn in logic after savewarping later on.")


		lastHeight += 75
		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)

		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Has Default/Vanilla Warp Song Locations:")

		lastHeight += 25
		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "If this option is checked off, then that means playing a warp song takes you to the vanilla location for that warp song (ex. playing minuet of forest takes you to the sacred forest meadow pedestal). Note that if this option is checked off, then you won't be able to change the location that warp songs take you to in logic later on.")


		lastHeight += 75
		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Has Decoupled Entrances:")

		lastHeight += 25
		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "If this option is checked off, then that means that if you go through a door and then go back through the door, you may not wind up where you started off (ex. you may enter a grotto in the Lost Woods which leads to a business scrub grotto, and when you exit this grotto, you may wind up outside the hammer grotto in Death Mountain Crater). Note that this option cannot be changed after you create your randomizer file.")


		lastHeight += 90
		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Autosave On:")

		lastHeight += 25
		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "If this option is checked off, then whenever you add a new connection between entrances, delete a connection between entrances, change where a warp song leads to, or alter any other property of your randomzier, then your changes are immediately saved to your randomizer file. If this option is not checked off, then you must manually hit the Save option in the file menu after a change in order for it to be saved. Note that this property can be changed after creating your randomizer in the View Properties menu.")

		lastHeight += 110

		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "Once you have the correct settings for your seed for the 4 options above checked off, then you can create your new randomizer by hitting the Create Randomizer and Create Save File Button. After clicking this button, you will be prompted to type in the location of where you want your randomizer tracker save file to be created. If the filename you entered in is valid and you have permission to create a file in the directory your file is in, then your randomizer tracker file will be created and saved in the specified location, and the Main Randomizer screen will load")

		lastHeight += 120

		self.mainCanvas.create_text(headerWidth, lastHeight, fill = "purple", font = "Heveltica 24 bold", anchor = NW, text = "The Main Randomizer Screen:")

		lastHeight += 40

		self.mainCanvas.create_text(mainTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "Once you have created a new randomizer or loaded an old randomizer file, you will be taken to the Main Randomizer Screen. This is where the randomizer tracking magic happens! Below is a list of the various features of this screen, as well as the features of the subscreens that can be loaded by clicking on the menu links at the top of the screen/application.")

		lastHeight += 100


		self.mainCanvas.create_text(subTextWidth, lastHeight, width = 1000, fill = "green", font = "Heveltica 24 bold", anchor = NW, text = "The Main Location Screen:")

		lastHeight += 40

		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "When the main screen of the app first loads (after loading a randomizer or creating a new one), the Main Location Selection screen will load. This screen provides four options for the user to choose from: the Overworld Map, the Dungeon List, the Houses List, and the Grottos List. Each screen provides a way for users to view the various locations in OOT, and to select locations for the purposes of adding connections, checking routes between locations, and more options. Additionally, each screen has a back button to reload the previous screen. Below is a brief summary of how each of the four options works.")

		lastHeight += 115

		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)	
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Overworld Map:")
		lastHeight += 25

		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "Once the user clicks on the Overworld Map option, a map of the Ocarina of Time overworld is loaded. This map contains rectangles over each of the main locations on the map (ex. there is one for Kokiri Forest, one for Lon Lon Ranch, etc.). A rectangles is white if there are still any locations in its area which have not had a connection assigned to it yet. Otherwise, it is yellow (note that indoor locations/grottos in a particular area are not included for this definition). After clicking on a specific rectangle, the corresponding map for that location loads on the screen, which includes rectangles for each entrance on the map. These rectangles correspond to all overworld entrances, all indoor house entrances, and all unique grotto entrances (any grotto which is one-of-a-kind). A rectangle for a specific connection is white if the user has not set where the entrance leads to yet, and is yellow otherwise. The one exception to this are the entrances which don't lead anywhere (the song pedestals and owl dropoff locations), which are colored red. When the user clicks on a rectangle for an entrance, an info rectangle will load which says the name of this entrance, where the entrance leads to (or --------- if the entrance's destination has not been set), and has buttons for adding and deleting connections to other entrances.")

		lastHeight += 213

		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Dungeon List:")
		lastHeight += 25

		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "Once the user clicks on the Dungeon List option, a scrollable list of all dungeons and subdungeons in the game is brought up, along with the two extra entrances in the Spirit Temple. When the user clicks on a dungeon, an info rectangle for the location loads, which has the same info/buttons that the info rectangles in the Overworld Map have.")

		lastHeight += 81
		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Houses List:")
		lastHeight += 25

		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "Once the user clicks on the Houses List option, a scrollable list of all interior house doors/exits is brought up. When the user clicks on a house, an info rectangle for the location loads, which has the same info/buttons that the info rectangles in the Overworld Map have. Note that the Generic_House location will increase in number whenever the highest numbered Generic_House has a connection set (ex. if 1 Generic House exists, and the user sets the destination of Generic_House_1, then Generic_House_2 will appear as an option in the list after the user finishes setting this destination).")			


		lastHeight += 118
		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Grottos List:")
		lastHeight += 25

		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "Once the user clicks on the Grottos List option, a scrollable list of all interior grotto exits is brought up. When the user clicks on a grotto, an info rectangle for the location loads, which has the same info/buttons that the info rectangles in the Overworld Map have. Note that all non-unique (i.e. repeating) grottos have a number attached to the end of them. Whenever a destination is assigned to the highest-numbered grotto for a type of grotto, another grotto with a higher number for that location is created (ex. if 1 Two_Business_Scrubs_Grotto exists and the user sets the destination of Two_Business_Scrubs_Grotto_1, then Two_Business_Scrubs_Grotto_2 will appear as an option in the list after the user finishes setting this destination).")	
		lastHeight += 150

		self.mainCanvas.create_text(subTextWidth, lastHeight, width = 1000, fill = "green", font = "Heveltica 24 bold", anchor = NW, text = "Adding and Deleting Connections:")
		lastHeight += 40

		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "When the user first starts out the application, they are in EXPLORE mode. This mode can be differentiated from other modes because it is the only mode where a Cancel button isn't in the top right corner of the screen (Note that the user can always get back to EXPLORE mode by clicking this Cancel button). When in this mode, the user has the ability to specify where going through one entrance leads to (i.e. adding a connection from one entrance to the other). Additionally, if the user makes a mistake, they can delete a connection.")

		lastHeight += 100
		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Add Connection:")

		lastHeight += 25
		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "When the user has the info rectangle for an entrance/location on screen, they can set where the entrance leads to by clicking the Add Connection button in the info rectangle. After this, the user will enter ADD mode. When the user next clicks on a location rectangle, the info rectangle will have a Finish Connection button on it. After the user clicks this button, a connection will be set from the first entrance to the second entrance. Note that if entrance decoupling is turned off and the entrance is a reversible entrance like going through a door, then the reverse connection leading from the destination to the source will also be added automatically. Additionally, the user can use the Add Connection button to set a connection to a different entrance if the user already set the destination for a location but made a mistake (the program will delete the original connection from this entrance and the reverse connection, if it exists). After finishing the connection, the user is sent back to EXPLORE mode.")

		lastHeight += 180

		self.create_circle(extraSubTextWidth + bulletOffset, lastHeight + 10, 5)
		self.mainCanvas.create_text(extraSubTextWidth + 80, lastHeight, fill = "black", font = "Heveltica 18 bold", anchor = NW, text = "Delete Connection:")
		lastHeight += 25

		self.mainCanvas.create_text(extraSubTextWidth + 100, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "When the user is in EXPLORE or ADD mode and brings up the info rectangle for a location, then if the location already has its destination set, a Delete Button will appear on the info rectangle. When the user clicks on the Delete Button, the connection between the location and its destination is removed, as well as the reverse connection (if entrance decoupling is turned off and the entrance is a reversible entrance).")


		lastHeight += 118

		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", text = "Song Menu:", anchor = NW)

		lastHeight += 40
		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "After clicking on the Song Menu tab, the user can click the Open Song Tracker option, which in turn loads the Song Tracker. On this screen, the user can check off which songs they have (and can uncheck off songs that they don't have). Additionally, if Vanilla Warp Songs is turned off, then the user can click on the Set Destination button next to a song to select where playing the song leads to. Then, the user can click on the corresponding location that the song leads to on the screen, and in the info rectangle for the location, the user can click the Add Song Destination button to set the song's location. Note that doing this on a song which already has a location set will overwrite the location that the song takes you to the new value. Lastly, the user can click on the Delete Destination button on the Song Tracker screen in order to remove the destination that the song leads to. Note that pressing the Confirm Changes button will ensure that the songs the user has checked off that they have will be updated accordingly.")

		lastHeight += 190

		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", text = "Age Menu:", anchor = NW)
	
		lastHeight += 40
		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "After clicking on the Age tab, the user can click on the Set Age Spawn Points option, which in turn loads the Age Tracker. On this screen, the user can check or uncheck the Is-Child? box and hit the Confirm Changes button in order to alter the current age of Link in logic. Additionally, if the Default Savewarp Locations option is turned off, then the user can click the Set Destination button to set where savewarping as a specific age takes Link. Then, the user can click on the location that savewarping takes them, which will bring up an info rectangle which has a Set Age Savewarp button. After clicking this button, the spawn point for that age will then be set (this can also be used to overwrite a pre-existing savewarp location if you make a mistake). Clicking the Delete Destination button on the Age Menu will remove the destination that the savewarp leads to.") 

		lastHeight += 190
		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", text = "View/Edit Seed Properties Menu:", anchor = NW)

		lastHeight += 40
		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "After clicking on the View tab, the user can click on the View/Edit Seed Properties Option, which in turn loads the Seed Properties Viewer. On this screen, the user can see if entrances are decoupled, if songs have vanilla warp locations, and if savewarping leads to vanilla locations (note that these 3 properties can't be changed - they have to be set to the right values when the seed is created). Additionally, there are 3 checkboxes below this, which are properties which the user can change. First, the user can check off (or uncheck) the Autosave On option, which enables and disables autosaving respectively. Next is the Is-Child checkbox, which the user can check off (if they are a child) or can uncheck (if they are currently an adult). Lastly, there is the Has-Access-To-Temple-Of-Time checkbox, which the user can check off once they have changed their age at the Temple of Time at least once or have reached the Temple of Time and have the ability to change ages. Note that the user must hit the Confirm Changes button on this screen for any of the user's selections on this screen to take effect.")

		lastHeight += 230
		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", text = "Reminder Tracker Menu:", anchor = NW)

		lastHeight += 40
		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "After clicking on the Reminders tab, the user can click on the Open Reminder Tracker Option, which in turn loads the Reminder Tracker. The Reminder Tracker allows the user to enter in important messages (such as the locations of key items), and save them for later viewing. The user can also delete messages as well once they are no longer relevant. To add a new reminder, the user must type in their message in the entrybox at the bottom of the screen, and then click the Add Reminder button. To delete reminder(s), the user can click on all of the reminders in the list of reminders that they want to delete, and then click the Delete Reminders button. If the user would like to unhighlight all of the reminders that are currently selected in the list, then the user can click the Unhighlight All button.")

		
		lastHeight += 165
		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", text = "Routing Menu:", anchor = NW)

		lastHeight += 40
		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "After clicking on the Routing tab, the user can click on the Find Shortest Path Option, which in turn will switch the mode that the program is in to ROUTING mode. In this mode, the user can click on a location rectangle, which will load an info rectangle with the option to select the location as the source of a path (i.e. where the user currently is). After clicking that button, the user then needs to click on the location rectangle for the destination of the path (i.e. where the user wants to go). Then, an info rectangle will appear with the option to select the location as the destination of the path. After clicking that button, the Routing screen will load with the selected locations as the source and destination. If no path exists between the two locations, then No Path Found will be displayed. Otherwise, a list of the steps needed to reach the destination will be listed, including savewarps, warp songs, and going through loading zones. From here, the user can highlight any entrances that they want to exclude from their path and hit the Re-Run button, which will cause the algorithm to search for another path which excludes the selected entrances, and will then display the result. Note that the excluded entrances are cumulative, so if A, B, C and D are entrances, and the user excludes A -> B in the first result, and then excludes C -> D in the second result, then when the user hits the Re-Run button again, both A -> B and C -> D will be excluded. The user can also click the Unhighlight All button in order to unhighlight all of the entrances in the list.")

		lastHeight += 270
		self.mainCanvas.create_text(subTextWidth, lastHeight, fill = "green", font = "Heveltica 24 bold", text = "Help Menu:", anchor = NW)
		lastHeight += 40
		self.mainCanvas.create_text(extraSubTextWidth, lastHeight, width = 1000, fill = "black", font = "Heveltica 16", anchor = NW, text = "After clicking on the help tab, the user can click on the Help option, which will load a help menu. The help menu describes how exactly this Entrance Randomizer Tracker works, and how to use it. Of course, since you are reading this message, you have obviously already figured out how to reach this screen :D")


		lastHeight += 100
		self.mainCanvas.create_text(headerWidth, lastHeight, fill = "purple", font = "Heveltica 24 bold", anchor = NW, text = "Miscellaneous Notes:")
		lastHeight += 40

		self.mainCanvas.create_text(mainTextWidth, lastHeight, fill = "black", width = 1000, font = "Heveltica 16", anchor = NW, text = "If autosave is turned off, then to save your file, you must click on File -> Save. Note that after saving, you should wait at least one second before closing the program in order to avoid any accidental data loss. Similarly, if autosave is enabled, then whenever you change a property of the seed, a song you own, or add or delete a connection between locations, you should wait at least a second after you make the change before closing the program in order to avoid accidentally corrupting your save file. In the File menu, there are also options to create a new randomizer, and to load a different randomizer file as well. One last thing - sometimes, you may find yourself clicking on rectangles on the screen and finding that nothing happens! However, this is not a bug. What has probably happened is that you have a window open somewhere in the background such as an Info Rectangle for a location, the Song Tracker, the Age Menu, or the View Properties Menu. Any one of these windows/screens will block any other windows from opening, and will also block all activity on any other window until the window is shut. As such, before you think that there is a bug, make sure that you don't have a hidden info rectangle open somewhere in the background (and if you do have one, you can simply close it to continue using the program). And with that, this help menu is complete! Thats all for now, folks! However, if you have any questions or discover any bugs in this program, feel free to contact me at tersaderwaslink@gmail.com")

		lastHeight += 290
		self.mainCanvas.create_text(mainTextWidth + 190, lastHeight, fill = "red", font = "Heveltica 32 bold", anchor = NW, text = "Lobsterzelda's OOT Entrance Randomizer Tracker V. 1.0")



	def create_circle(self, x, y, r):
		self.mainCanvas.create_oval(x - r, y - r, x + r, y + r, fill = "black")
if __name__ == '__main__':
	helpScreen(None)

		
