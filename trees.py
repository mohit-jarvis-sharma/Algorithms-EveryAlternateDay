"""
Source: https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c
Author: Mohit Sharma

"""
"""class Queue:
	def __init__(self):
		self.cur_q = []
		self.cur_elem = -1

	def put(self, value):
		self.cur_q.append(value)

	def get(self):
		if self.cur_elem == -1:
			return -1
		else:
			temp = self.cur_q[self.cur_elem]
			self.cur_elem -= 1
			return temp

	def empty(self):
		if self.cur_elem <= 0:
			return 0
		else:
			return cur_elem"""

from queue import *

class BinaryTree:
	
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

	def insert_left(self,value):
		if self.leftChild == None:
			self.leftChild = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.leftChild = self.leftChild
			sel.leftChild = new_node

	def insert_right(self,value):
		if self.rightChild == None:
			self.rightChild = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.rightChild = self.rightChild
			sel.rightChild = new_n

	def pre_order(self):
		print(self.value)

		if self.leftChild:
			self.leftChild.pre_order()

		if self.rightChild:
			self.rightChild.pre_order()

	def in_order(self):
		if self.leftChild:
			self.leftChild.in_order()

		print(self.value)

		if self.rightChild:
			self.rightChild.in_order()

	def post_order(self):
		if self.leftChild:
			self.leftChild.post_order()

		if self.rightChild:
			self.rightChild.post_order()

		print(self.value)

	def bfs(self):
		queue = Queue()
		queue.put(self)

		while not queue.empty():
			current_node = queue.get()
			print(current_node.value)

			if current_node.leftChild:
				queue.put(current_node.leftChild)

			if current_node.rightChild:
				queue.put(current_node.rightChild)

class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

	def insert_node(self, value):
		if value <= self.value and self.leftChild:
			self.leftChild.insert_node(value)
		elif value <= self.value:
			self.leftChild = BinarySearchTree(value)
		elif value > self.value and self.rightChild:
			self.rightChild.insert_node(value)
		else:
			self.rightChild = BinarySearchTree(value)

	def find_node(self, value):
		if value < self.value and self.leftChild:
			return self.leftChild.find_node(value)
		if value > self.value and self.rightChild:
			return self.rightChild.find_node(value)

		return value == self.value

	def find_minimum_value(self):
		if self.leftChild:
			return self.leftChild.find_minimum_value()
		else:
			return self.value

	def clear_node(self):
		self.value = None
		self.leftChild = None
		self.rightChild = None

	def remove_node(self, value, parent):
		if value < self.value and self.leftChild:
			self.leftChild.remove_node(value, self)
		elif value < self.value:
			return False
		elif value > self.value and self.rightChild:
			self.rightChild.remove_node(value, self)
		elif value > self.value:
			return False
		else:
			if self.leftChild is None and self.rightChild is None and self == parent.leftChild:
				parent.left_child = None
				self.clear_node()
			elif self.leftChild is None and self.rightChild is None and self == parent.rightChild:
				parent.right_child = None
				self.clear_node()
			elif self.leftChild and self.rightChild is None and self == parent.leftChild:
				parent.leftChild = self.leftChild
				self.clear_node()
			elif self.leftChild and self.rightChild is None and self == parent.rightChild:
				parent.rightChild = self.leftChild
				self.clear_node()
			elif self.leftChild is None and self.rightChild and self == parent.leftChild:
				parent.leftChild = self.rightChild
				self.clear_node()
			elif self.leftChild is None and self.rightChild and self == parent.rightChild:
				parent.rightChild = self.rightChild
				self.clear_node()
			else:
				self.value = self.rightChild.find_minimum_value()
				self.rightChild.remove_node(self.value, self)

			return True

a_node = BinaryTree(1)
a_node.insert_left(2)
a_node.insert_right(5)

b_node = a_node.leftChild
b_node.insert_right(4)
b_node.insert_left(3)

c_node = a_node.rightChild
c_node.insert_left(6)
c_node.insert_right(7)



bst = BinarySearchTree(15)
bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)