from locationNode import locationNode

#This class has an adjacency list, where the first entry is a list of the form: [nodeID, locationNode], where nodeID is the ID of the new node, and locationNode is the first node of a linked list of destination nodes (or None if there are no edges pointing out from this node)
#Each new node added to the list has an ID 1 greater than the last added node (with the first added node starting at 0)
class adjacencyList:
	def __init__(self):
		self.locationsList = []
		self.lastNodeAdded = -1


	def createGraphFromLines(self, linesOfFile):
		self.locationsList = []
		self.lastNodeAdded = -1
		for currLine in linesOfFile:
			if len(currLine.strip()) == 0:
				continue
		
			if currLine.strip() == '|':
				continue

			lineMainSplit = currLine.split(":")
			sourceID = -1
			if len(lineMainSplit) == 0 or len(lineMainSplit) > 2:
				return -1
			try:
				sourceID = int(lineMainSplit[0])
			except ValueError:
				return -1

			self.locationsList.append([sourceID, None])
			if len(lineMainSplit) == 2 and len(lineMainSplit[1].strip()) != 0:
				secondHalf = lineMainSplit[1].split(",")
				destinationID = -1
				weight = -1.0
				headOfList = None
				currentIterator = None
				for pair in secondHalf:
					splitPair = pair.split("/")
					if(len(splitPair) != 2):
						print("splitPair did not have size of 2! " + str(len(splitPair)) + " was length, and first was " + splitPair[0])
						return -1
					try:
						destinationID = int(splitPair[0])
						weight = float(splitPair[1])	
					except ValueError:
						print("Value Error occured!")
						return -1

					if headOfList is None:
						headOfList = locationNode(destinationID, weight, None)
						currentIterator = headOfList
					else:
						currentIterator.next = locationNode(destinationID, weight, None)
						currentIterator = currentIterator.next
				self.locationsList[len(self.locationsList) - 1][1] = headOfList

		largestID = -1
		for node in self.locationsList:
			if node[0] > largestID:
				largestID = node[0]

		self.lastNodeAdded = largestID
		return 0

	#Tacks a new entry onto the locationsList, which initially has no destination nodes
	#This function returns the ID of the newly created node
	def addNewNode(self):
		self.locationsList.append([self.lastNodeAdded + 1, None])
		self.lastNodeAdded = self.lastNodeAdded + 1
		return self.lastNodeAdded

	def addNewDestinationToSource(self, sourceInt, destInt, weight):
		locationOfSource = -1
		for num in range(0, self.getNumNodes()):
			if(self.locationsList[num][0] == sourceInt):
				locationOfSource = num
				break
			
		if(locationOfSource == -1):
			print("Error: sourceNode with ID of " + str(sourceInt) + " was not found in the adjacency list!")
			exit()

		sourceList = self.locationsList[locationOfSource]

		if(sourceList[1] is None):
			sourceList[1] = locationNode(destInt, weight, None)
		else:
			sourceList[1] = locationNode(destInt, weight, sourceList[1])	

	def getNumNodes(self):
		return len(self.locationsList)

	def getLastIDAdded(self):
		return self.lastNodeAdded

	def deleteNode(self, nodeNum):
		#First, deleting the sourceNode with the ID of nodeNum from the adjacencyList:
		for sourceNodeIndex in range(0, self.getNumNodes()):
			if(self.locationsList[sourceNodeIndex][0] == nodeNum):
				self.locationsList.pop(sourceNodeIndex)
				break

		#Now, removing any destination nodes that reference this node in the adjacencyList:
		for sourceNodeIndex in range(0, self.getNumNodes()):
			prevLocationNode = None
			currentLocationNode = self.locationsList[sourceNodeIndex][1]
			while(currentLocationNode is not None):
				if(currentLocationNode.destination == nodeNum):
					if(prevLocationNode is None):
						self.locationsList[sourceNodeIndex][1] = self.locationsList[sourceNodeIndex][1].next
						currentLocationNode = self.locationsList[sourceNodeIndex][1]
						prevLocationNode = None
					else:
						prevLocationNode.next = currentLocationNode.next
						if(prevLocationNode.next is None):
							break
						currentLocationNode = prevLocationNode.next
				else:	
					prevLocationNode = currentLocationNode
					currentLocationNode = currentLocationNode.next

	def removeConnection(self, sourceInt, destInt):
		sourceElement = None
		for element in self.locationsList:
			if(element[0] == sourceInt):
				sourceElement = element
				break
		if(sourceElement is None):
			return
		currentLocationNode = sourceElement[1]
		prevLocationNode = None
		while(currentLocationNode is not None):
			if(currentLocationNode.destination == destInt):
				if(prevLocationNode is None):
					sourceElement[1] = currentLocationNode.next
					return
				else:
					prevLocationNode.next = currentLocationNode.next
					return
			prevLocationNode = currentLocationNode
			currentLocationNode = currentLocationNode.next
		return

	#Returns the location node specifying the connection between sourceInt and destInt, or None if there is no such connection
	def getConnection(self, sourceInt, destInt):
		sourceElement = None
		for element in self.locationsList:
			if(element[0] == sourceInt):
				sourceElement  = element
				break
		if(sourceElement is None):
			return
		currentLocationNode = sourceElement[1]
		while(currentLocationNode is not None):
			if(currentLocationNode.destination == destInt):
				return currentLocationNode
			currentLocationNode = currentLocationNode.next
		return None

	def hasDirectConnection(self, sourceInt, destInt):
		return (self.getConnection(sourceInt, destInt) is not None)


	#Returns a list of all integer IDs which are destinations of the specified source node and have a non-zero weight
	def getAllNonZeroDestinationsOfSource(self, sourceInt):
			sourceElement = None
			for element in self.locationsList:
				if(element[0] == sourceInt):
					sourceElement = element
					break
			if sourceElement is None:
				return []

			returnList = []
			currentLocationNode = sourceElement[1]
			while(currentLocationNode is not None):
				if currentLocationNode.weight > 0.0:
					returnList.append(currentLocationNode.destination)	
				currentLocationNode = currentLocationNode.next
			return returnList

	def printAdjacencyList(self):
		print("\t\tAdjacency List Representation (Source -> Dest1---WeightWeight1, Dest2---WeightWeight2, ...)")
		for element in self.locationsList:
			print(str(element[0]), " -> ", end = "")
			currentLocationNode = element[1]
			while(currentLocationNode is not None):
				print(str(currentLocationNode.destination), "---Weight", str(currentLocationNode.weight), ", ", sep="", end = "")
				currentLocationNode = currentLocationNode.next
			print("", end = "\n")
		print()

def addNewDestTestFunc(adjList, source, dest, weight):
	adjList.addNewDestinationToSource(source, dest, weight)
	print("Added connection from node " + str(source) + " to node " + str(dest) + ", with weight " + str(weight) + ":")
	adjList.printAdjacencyList()

def removeConnectionTestFunc(adjList, source, dest):
	adjList.removeConnection(source, dest)
	print("Removed connection from node " + str(source) + " to node " + str(dest))
	adjList.printAdjacencyList()

def removeNodeTestFunc(adjList, source):
		adjList.deleteNode(source)
		print("Removed node " + str(source) + " from adjacency list!")
		adjList.printAdjacencyList()

def getConnectionTestFunc(adjList, source, dest):
	myConnect = adjList.getConnection(source, dest)
	if(myConnect is None):
		print("No connection found from node " + str(source) + " to node " + str(dest) + "!")
	else:
		print("Connection between node " + str(source) + " to node " + str(myConnect.destination) + " was found with weight " + str(myConnect.weight))

def hasDirectConnectionTestFunc(adjList, source, dest):
	print("Status of there being a direct connection from node " + str(source) + " to node " + str(dest) + ": " + str(adjList.hasDirectConnection(source, dest)))

if __name__ == "__main__":
	print("Compiled!")
	myAdjacencyList = adjacencyList()
	print("Printing empty adjacency list: ")
	myAdjacencyList.printAdjacencyList()
	print("Adding new node to list:")
	myAdjacencyList.addNewNode()
	myAdjacencyList.printAdjacencyList() 
	myAdjacencyList.addNewNode()
	myAdjacencyList.addNewNode()
	myAdjacencyList.addNewNode()
	myAdjacencyList.addNewNode()
	myAdjacencyList.addNewNode()
	print("Added 5 more nodes, and printing resulting adjacency list:")
	myAdjacencyList.printAdjacencyList()
	addNewDestTestFunc(myAdjacencyList, 0, 2, 3)
	addNewDestTestFunc(myAdjacencyList, 0, 1, 15)
	addNewDestTestFunc(myAdjacencyList, 0, 4, 30)
	addNewDestTestFunc(myAdjacencyList, 0, 5, 50)
	addNewDestTestFunc(myAdjacencyList, 1, 0, 13)
	getConnectionTestFunc(myAdjacencyList, 0, 1)
	hasDirectConnectionTestFunc(myAdjacencyList, 0, 1)
	removeConnectionTestFunc(myAdjacencyList, 0, 1)
	getConnectionTestFunc(myAdjacencyList, 0, 1)
	hasDirectConnectionTestFunc(myAdjacencyList, 0, 1)
	addNewDestTestFunc(myAdjacencyList, 0, 3, 21)
	addNewDestTestFunc(myAdjacencyList, 4, 2, 43)
	addNewDestTestFunc(myAdjacencyList, 2, 3, 15)
	addNewDestTestFunc(myAdjacencyList, 1, 4, 3)
	addNewDestTestFunc(myAdjacencyList, 3, 4, 7)
	removeNodeTestFunc(myAdjacencyList, 4)
	myAdjacencyList.addNewNode()
	print("Added new node!")
	myAdjacencyList.printAdjacencyList()
	addNewDestTestFunc(myAdjacencyList, 6, 2, 13)
	print("last added number was " + str(myAdjacencyList.getLastIDAdded()))
	removeConnectionTestFunc(myAdjacencyList, 2, 3)
