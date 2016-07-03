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

	def peek(self):
		if self.size == 0:
			return None
		else:
			return self.top

	def isEmpty(self):
		if self.size == 0:
			return True
		return False


# algorithm that sorts a stack using an additional stack,
# in O(n^2) time and O(n) space
def sortStack(inputStack):
	newStack = Stack()

	while (not inputStack.isEmpty()):

		# If the next element in the original stack fits at the 
		# bottom of the new stack, then pop it off and push it
		if newStack.isEmpty() or (newStack.peek().data < inputStack.peek().data):
			newStack.push(inputStack.pop())
		else:
			# Pop off the next element to be sorted and store it
			tempNode = inputStack.pop()
			# Track the number of times we have to pop from the new stack
			count = 0

			while (not newStack.isEmpty and newStack.peek().data > tempNode.data):
				inputStack.push(newStack.pop())
				count = count + 1
			newStack.push(tempNode)

			# Take all the things we popped off the new stack and
			# put them back on
			for x in range(0, count):
				newStack.push(inputStack(pop))

	return newStack

def printStack(stack):

	# Have to create a new stack so the data isn't lost
	newStack = Stack()

	# Pop elements off the stack, print them, place them in the new stack for storage,
	# then at the end put them back.
	while (not stack.isEmpty()):
		print stack.peek().data
		newStack.push(stack.pop())

	while (not newStack.isEmpty()):
		stack.push(newStack.pop())


