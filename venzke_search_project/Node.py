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
		self.childNodes = []
		self.childStates = []

	#sets State to s
	def setState(self,s):
		self.state = s

	#sets Cost to c
	def setCost(Self, c):
		self.cost = c

	#sets Parent node to p
	def setParent(self, p):
		self.parent = p

	#returns State
	def getState(self):
		return self.state

	#returns cost
	def getCost(self):
		return self.cost

	#returns parent Node
	def getParent(self):
		return self.parent

	#prints out Node 
	def printNode(self):
		print "======================" #divides nodes 
		self.state.printState()

	#returns a list of child nodes
	def expand(self):
		self.childStates = self.state.generateSuccessor()

		#adds childStates to childNodes
		for self.cS in self.childStates:
			self.c = Node(self.cS, self.cost + self.cS.stepCost(), self)
			self.cost - self.cS.stepCost()
			self.childNodes.append(self.c)
		return self.childNodes


