"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: takes in a list of tiles and finds the order with the lowest 'cost'
"""
from Tile import Tile
from State import State
from Node import Node

#takes in a file 
#returns list of tiles from the file
def read_file(file_name):
	tile_set_list = []

	#runs while file is open
	with open(file_name) as f:

		#reads in all lines in the file
		for line in f:

			#reads each line, splits data at spaces, and adds a new Tile to tile_set_list
			#file format "a b c d"
			a, b, c, d = (s for s in line.split(' '))
			tile_set_list.append(Tile(a, b, c, d))
	return tile_set_list

#takes in a file
#runs a breath_first search
#prints best solution to console
def breadth_first(file_name):
	tile_set = read_file(file_name) #list of tiles
	start_state = State([],tile_set) #State with no placed tiles
	root = Node(start_state, 0.0, None) #First Node, no cost, no parent
	frontier = [root] #list of nodes
	best_solution = State([],[]) #stores best solution
	best_cost = float("inf") #set to infinity

	#runs while frontier is not empty
	while frontier:
		current_node = frontier.pop(0) #removes first node in frontier, stores in current_node
		
		#checks if current_node is a solution 
		#compares current_node to best_solution
		#stores new best solution
		if current_node.get_state().is_goal() and current_node.get_cost() < best_cost:
			best_cost = current_node.get_cost()
			best_solution = current_node.get_state()

		#creates child_nodes to search 
		#adds child_nodes to frontier
		child_nodes = current_node.expand()
		for c_n in child_nodes:
			frontier.append(c_n)

	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	best_solution.print_state()

#User inputs file name
file_name = raw_input("What file do you want to use? ")

#starts breath first search
breadth_first(file_name)