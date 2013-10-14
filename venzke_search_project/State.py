"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: Contains a list of placed Tiles and unplaced Tiles.
"""
from Tile import Tile

class State(object):
	
	#sets placedTiles as pT and unplacedTiles as uT
	def __init__(self, pT, uT):
		self.placedTiles = pT
		self.unplacedTiles = uT
		self.children = []
		self.unT = []
		self.pT = []
		self.lengthUT = range(len(self.unplacedTiles))
		self.lengthPT = range(len(self.placedTiles))
	
	#sets placedTiles as pT
	def setPlacedTiles(self, pT):
		self.placedTiles = pT

	#sets unplacedTiles as uT
	def setUnplacedTiles(self, uT):
		self.unplacedTiles = uT

	#returns placedTiles
	def getPlacedTiles(self):
		return self.placedTiles

	#returns unplacedTiles
	def getUnplacedTiles(self):
		return self.unplacedTiles

	#check to see if the State is a goal State 
	#returns boolean
	def isGoal(self):

		#if all tiles are place 
		#returns true
		if not self.unplacedTiles:
			return True

		#if not all tiles placed 
		#returns false
		else:
			return False

	#calculates step cost
	def stepCost(self):

		#if 2 or more tiles are placed 
		#returns step cost
		if len(self.placedTiles) > 1:
			return self.placedTiles[-2].compare_below(self.placedTiles[-1])
		
		#if 0 or 1 tiles are placed 
		#returns no cost
		else:
			return 0.0

	#returns a list of child states
	def generateSuccessor(self):

		#loops through all unplaced tiles
		for self.i in self.lengthUT:

			#clears unT and pT
			self.unT = []
			self.pT = []

			#fills unT with unplacedTiles
			if self.unplacedTiles:
				for self.j in self.lengthUT:
					self.unT.append(self.unplacedTiles[self.j])
			else:
				self.unT = []

			#fills pT with placedTiles
			if self.placedTiles:
				for self.j in self.lengthPT:
					self.pT.append(self.placedTiles[self.j])
			else:
				self.pT = []

			#removes ith unT tile and adds it to the end of pT
			self.pT.append(self.unT.pop(self.i))

			#adds new state to children
			self.children.append(State(self.pT, self.unT))
		return self.children

	#prints out State
	def printState(self):
		print "placed"
		for pT in self.placedTiles:
			print pT.getTile()
		print "unplaced"
		for uT in self.unplacedTiles:
			print uT.getTile()