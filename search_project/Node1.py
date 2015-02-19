#!/usr/bin/python

"""
A node contains a state in the search tree
It contains the list of placed and unplaced tiles 
It also holds the characteristic protein sequence if we have one
It also has the cost of the search state
"""

class Node(object):

	""" 
	Initializes a node
	ut: list of unplaced tiles in this node
	pt: list of placed tiles in this node
	cost: current cost associated with this node 
	characteristic: list containing the characteristic backbone protein chain
	char_cost: cost from comparing with the characteristic
	order_cost: cost from comparing tiles with the one before it
	"""
	def __init__(self, ut, pt, cost, characteristic, char_cost, order_cost):
		self.unplaced_tiles = ut
		self.placed_tiles = pt
		self.cost = cost
		self.characteristic = characteristic
		self.char_cost = char_cost
		self.order_cost = order_cost

	"""
	prints the node to the console
	"""
	def __str__(self):
		for tile in self.placed_tiles:
			print tile.get_tile()
		return ""

	"""
	Creates children nodes of the current node
	returns a list of child nodes
	"""
	def expand(self):
		new_nodes = []
		char_num = len(self.placed_tiles) # location in the protein sequence

		# If this Node contains a characteristic protein sequence we will use it
		if(self.characteristic):

			# loop through all tiles that have not been placed
			for i in range(len(self.unplaced_tiles)):

				# check to see if current tile can be placed in this location
				amino_type_list = self.unplaced_tiles[i].get_amino_type()
				amino_Idx = self.characteristic[char_num][2]
				if(amino_type_list[amino_Idx]==2.0):
					temp_ut = list(self.unplaced_tiles) 
					placed_tile = temp_ut.pop(i) 
					temp_pt = list(self.placed_tiles) 
					temp_pt.append(placed_tile)

					# add child node to list of new_nodes
					new_nodes.append(Node(temp_ut, temp_pt, self.cost, self.characteristic, self.char_cost, self.order_cost))

				elif(amino_type_list[amino_Idx] > 0.001):

					# copy unplaced and placed tile lists, remove tile from list and add it to the placed tile list
					temp_ut = list(self.unplaced_tiles) 
					placed_tile = temp_ut.pop(i) 
					temp_pt = list(self.placed_tiles) 
					temp_pt.append(placed_tile)

					# Calculated cost 
					if(self.placed_tiles): # not the first tile
						temp_char_cost = placed_tile.get_error(self.characteristic[char_num])
						temp_order_cost = self.placed_tiles[-1].compare_below(placed_tile)
					else: # first tile being placed 
						temp_char_cost = placed_tile.get_error(self.characteristic[char_num])
						temp_order_cost = 0 # no before it to compare to
					c = temp_order_cost + temp_char_cost

					# add child node to list of new_nodes
					new_nodes.append(Node(temp_ut, temp_pt, self.cost + c, self.characteristic,self.char_cost+temp_char_cost, self.order_cost+temp_order_cost))
			return new_nodes

		# Account for nodes that do not have a characteristic protein sequence
		else:
			for i in range(len(self.unplaced_tiles)):
				#no longer comparing the amino acid type of the unplaced tile to the characteristic as the characteristic does not exist

				# copy unplaced and placed tile lists, remove tile from list and add it to the placed tile list
				temp_ut = list(self.unplaced_tiles)
				placed_tile = temp_ut.pop(i)
				temp_pt = list(self.placed_tiles)
				temp_pt.append(placed_tile)

				# Calculated cost (no char_cost since there is no characteristic)
				if(self.placed_tiles): # not the first tile
					temp_order_cost = self.placed_tiles[-1].compare_below(placed_tile)
				else: # first tile being placed 
					temp_order_cost = 0
				c = temp_order_cost

				# add child node to list of new_nodes
				new_nodes.append(Node(temp_ut, temp_pt, self.cost + c,[],0, self.order_cost+temp_order_cost))
			return new_nodes

	"""
	returns the cost when compared to the characteristic
	"""
	def get_char_cost(self):
		return self.char_cost

	"""
	returns the cost of the node
	"""
	def get_cost(self):
		return self.cost

	"""
	returns the cost from comparing tiles with the one before it
	"""
	def get_order_cost(self):
		return self.order_cost

	"""
	returns if a node is in in goal state
	True if it is goal state
	False if not in goal state
	"""
	def is_goal(self):
		return not bool(self.unplaced_tiles)
