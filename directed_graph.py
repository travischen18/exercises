class Graph(object):
	def __init__(self):
		nodes = []

	def addNode(self, newNode):
		nodes.append(newNode)

class Node(object):
	def __init__(self, data):
		self.name = data
		children = []