#!/usr/bin/python
import math

class Node(object):

	# Makes a Nodes with State s, Cost c, and parent node p
	def __init__(self, ut, pt, cost, characteristic):
		self.unplaced_tiles = ut
		self.placed_tiles = pt
		self.cost = cost
		self.characteristic = characteristic

	def is_goal(self):
		return not bool(self.unplaced_tiles)

	#prints out Node 
	def __str__(self):
		for tile in self.placed_tiles:
			print tile.get_tile()
		return ""

	# returns cost
	def get_cost(self):
		return self.cost

	# returns a list of child nodes
	def expand(self):
		new_nodes = []
		for i in range(len(self.unplaced_tiles)):

			temp_ut = list(self.unplaced_tiles)
			placed_tile = temp_ut.pop(i)

			temp_pt = list(self.placed_tiles)
			temp_pt.append(placed_tile)

			if(self.placed_tiles):
				c = self.placed_tiles[-1].compare_below(placed_tile) + math.fabs(self.placed_tile.get_sum() - self.characteristic[len(placed_tiles) + 1].get_sum())
			else:
				c = math.fabs(self.placed_tile.get_sum() - self.characteristic[0].get_sum())

			new_nodes.append(Node(temp_ut, temp_pt, self.cost + c))
			#this is where the things would change, cost of tile making sense. 
		
		return new_nodes