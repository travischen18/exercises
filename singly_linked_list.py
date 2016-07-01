class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, head):
		self.head = head
		self.tail = head

	# Returns a string representation of the list
	def toString(self):
		output = ""
		currNode = head
		while (currNode != None):
			output = output + str(currNode.data) + " "
			currNode = currNode.next

		return output

	def append(self, nextNode):
		self.tail.next = nextNode
		self.tail = self.tail.next

	# Removes duplicate nodes in O(n^2) time
	def removeDups(self):
		currentNode = head
		while (currentNode != None):
			searchNode = currentNode
			while (searchNode.next != None):
				if searchNode.next.data == currentNode.data:
					searchNode.next = searchNode.next.next
				else:
					searchNode = searchNode.next
			currentNode = currentNode.next

		