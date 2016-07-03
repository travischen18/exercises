class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack(object):
	def __init__(self, top = None):
		self.top = top
		self.size = 0

	def push(self, el):
		if self.size == 0:
			self.top = el
		else:
			el.next = self.top
			self.top = el

		self.size = self.size + 1

	def pop(self):
		if self.size == 0:
			return None
		else:
			returnVal = self.top
			self.top = self.top.next
			self.size = self.size - 1
			return returnVal



stack = Stack()

stack.push(Node(30))
stack.push(Node(83))
stack.push(Node(2))
stack.push(Node(29))
stack.push(Node(100))
stack.push(Node(33))
stack.push(Node(15))

while (stack.size != 0):
	print stack.pop().data
