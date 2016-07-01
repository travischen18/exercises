class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, head):
		self.head = head
		self.tail = head

	def append(nextNode):
		self.tail.next = nextNode
		self.tail = self.tail.next
		