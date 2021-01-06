from tkinter import *
import threading
try:
	from tkmacosx import *
except:
	pass

from firstScreen import *
from mainMapScreen import *

class mainController():
	def __init__(self, root):
		self.OOT_Graph = None
		self.fileName = ""
		self.readyForMainMapScreen = False
		self.root = root
		self.initialScreen = firstScreen(self)	
		if self.readyForMainMapScreen:
			self.mainMapScreen = mainMapScreen(self)
		else:
			exit(0)
		self.root.quit()

root = Tk()
root.withdraw()
m = mainController(root)
root.mainloop()
