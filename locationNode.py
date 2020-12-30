"""locationNode is a class used to represent a node in a linked list. the graph of all locations in OOT uses an adjacency list, which is a list of pairs of the form [nodeID, locationNode]. Each locationNode is then used to construct a linked list of destinations from the source node
"""

class locationNode:
	"""Note: Destination is an int representing the ID of the destination, weight is an int representing the weight of the edge, and myNext is either None (if we are at the end of the list) or another locationNode in the list"""
	def __init__(self, destination, weight, myNext):
		self.destination = destination
		self.weight = weight
		self.next = myNext 
