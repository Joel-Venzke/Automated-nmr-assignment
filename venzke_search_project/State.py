"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: Contains a list of placed Tiles and unplaced Tiles.
"""
from Tile import Tile

class State(object):
	
	#sets placed_tiles as p_t and unplaced_tiles as u_t
	def __init__(self, p_t, u_t):
		self.placed_tiles = p_t
		self.unplaced_tiles = u_t
		self.children = []
		self.un_t = []
		self.p_t = []
		self.length_u_t = range(len(self.unplaced_tiles))
		self.length_p_t = range(len(self.placed_tiles))
	
	#sets placed_tiles as p_t
	def set_placed_tiles(self, p_t):
		self.placed_tiles = p_t

	#sets unplaced_tiles as u_t
	def set_unplaced_tiles(self, u_t):
		self.unplaced_tiles = u_t

	#returns placed_tiles
	def get_placed_tiles(self):
		return self.placed_tiles

	#returns unplaced_tiles
	def get_unplaced_tiles(self):
		return self.unplaced_tiles

	#check to see if the State is a goal State 
	#returns boolean
	def is_goal(self):

		#if all tiles are place 
		#returns true
		if not self.unplaced_tiles:
			return True

		#if not all tiles placed 
		#returns false
		else:
			return False

	#calculates step cost
	def step_cost(self):

		#if 2 or more tiles are placed 
		#returns step cost
		if len(self.placed_tiles) > 1:
			return self.placed_tiles[-2].compare_below(self.placed_tiles[-1])
		
		#if 0 or 1 tiles are placed 
		#returns no cost
		else:
			return 0.0

	#returns a list of child states
	def generate_successor(self):

		#loops through all unplaced tiles
		for self.i in self.length_u_t:

			#clears un_t and p_t
			self.un_t = []
			self.p_t = []

			#fills un_t with unplaced_tiles
			if self.unplaced_tiles:
				for self.j in self.length_u_t:
					self.un_t.append(self.unplaced_tiles[self.j])
			else:
				self.un_t = []

			#fills p_t with placed_tiles
			if self.placed_tiles:
				for self.j in self.length_p_t:
					self.p_t.append(self.placed_tiles[self.j])
			else:
				self.p_t = []

			#removes ith un_t tile and adds it to the end of p_t
			self.p_t.append(self.un_t.pop(self.i))

			#adds new state to children
			self.children.append(State(self.p_t, self.un_t))
		return self.children

	#prints out State
	def print_state(self):
		print "placed"
		for p_t in self.placed_tiles:
			print p_t.get_tile()
		print "unplaced"
		for u_t in self.unplaced_tiles:
			print u_t.get_tile()