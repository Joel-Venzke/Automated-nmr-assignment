"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: Contains a state and the cost and parent of the state.
"""

class Node(object):

	# Makes a Nodes with State s, Cost c, and parent node p
	def __init__(self, ut, pt, cost):
		self.unplaced_tiles = ut
		self.placed_tiles = pt
		self.cost = cost

	def is_goal(self):
		return not bool(self.unplaced_tiles)

	# returns cost
	def get_cost(self):
		return self.cost

	# returns a list of child nodes
	def expand(self):
		new_nodes = []
		for i in range(len(self.unplaced_tiles)):

			# make copies of the lists
			temp_ut = list(self.unplaced_tiles)
			ut = temp_ut.pop(i)

			up = list(self.placed_tiles)

			cost = self.unplaced_tiles[-1].compare_below(self.unplaced_tiles[i])
			new_nodes.append(Node(ut, up, self.cost + cost))