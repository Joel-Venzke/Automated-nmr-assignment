"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: Contains a state and the cost and parent of the state.
"""
from State import State

class Node(object):

	#Makes a Nodes with State s, Cost c, and parent node p
	def __init__(self, s, c, p):
		self.state = s
		self.cost = c
		self.parent = p
		self.child_nodes = []
		self.child_states = []

	#sets State to s
	def set_state(self,s):
		self.state = s

	#sets Cost to c
	def set_cost(Self, c):
		self.cost = c

	#sets Parent node to p
	def set_parent(self, p):
		self.parent = p

	#returns State
	def get_state(self):
		return self.state

	#returns cost
	def get_cost(self):
		return self.cost

	#returns parent Node
	def get_parent(self):
		return self.parent

	#prints out Node 
	def print_node(self):
		print "======================" #divides nodes 
		self.state.print_state()

	#returns a list of child nodes
	def expand(self):
		self.child_states = self.state.generate_successor()

		#adds child_states to child_nodes
		for self.c_s in self.child_states:
			self.c = Node(self.c_s, self.cost + self.c_s.step_cost(), self)
			self.cost - self.c_s.step_cost()
			self.child_nodes.append(self.c)
		return self.child_nodes


