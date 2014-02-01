#!/usr/bin/python
import math

class Node(object):

	# Makes a Nodes with State s, Cost c, and parent node p
	def __init__(self, ut, pt, cost, characteristic, char_cost, order_cost):
		self.unplaced_tiles = ut
		self.placed_tiles = pt
		self.cost = cost
		self.characteristic = characteristic
		self.char_cost = char_cost
		self.order_cost = order_cost

	def get_char_cost(self):
		return self.char_cost

	def get_order_cost(self):
		return self.order_cost

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
				temp_char_cost = placed_tile.get_error(self.characteristic[i])
				temp_order_cost = self.placed_tiles[-1].compare_above(placed_tile)
			else:
				temp_char_cost = placed_tile.get_error(self.characteristic[i])
				temp_order_cost = 0
			c = temp_order_cost + temp_char_cost

			new_nodes.append(Node(temp_ut, temp_pt, self.cost + c, self.characteristic,self.char_cost+temp_char_cost, self.order_cost+temp_order_cost))
			
		
		return new_nodes