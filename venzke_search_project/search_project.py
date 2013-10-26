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
	nodes_generated = len(frontier)

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
		nodes_generated = len(child_nodes) + nodes_generated
		for c_n in child_nodes:
			frontier.append(c_n)

	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	best_solution.print_state()
	print "Nodes Generated: " + str(nodes_generated)

def depth_first(file_name):
	tile_set = read_file(file_name) #list of tiles
	start_state = State([],tile_set) #State with no placed tiles
	root = Node(start_state, 0.0, None) #First Node, no cost, no parent
	frontier = [root] #list of nodes
	best_solution = State([],[]) #stores best solution
	best_cost = float("inf") #set to infinity
	nodes_generated = len(frontier)

	#runs while frontier is not empty
	while frontier:
		current_node = frontier.pop() #removes first node in frontier, stores in current_node
		
		#checks if current_node is a solution 
		#compares current_node to best_solution
		#stores new best solution
		if current_node.get_state().is_goal() and current_node.get_cost() < best_cost:
			best_cost = current_node.get_cost()
			best_solution = current_node.get_state()

		#creates child_nodes to search 
		#adds child_nodes to frontier
		child_nodes = current_node.expand()
		nodes_generated = len(child_nodes) + nodes_generated
		for c_n in child_nodes:
			frontier.append(c_n)

	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	best_solution.print_state()
	print "Nodes Generated: " + str(nodes_generated)
	
#takes in a file
#runs a uniform cost search
#prints best solution to console
def uniform_cost(file_name):
	tile_set = read_file(file_name) #list of tiles
	start_state = State([],tile_set) #State with no placed tiles
	root = Node(start_state, 0.0, None) #First Node, no cost, no parent
	frontier = [root] #list of nodes
	best_solution = State([],[]) #stores best solution
	best_cost = float("inf") #set to infinity
	nodes_generated = len(frontier)
	keep_running = True
	nodes_generated = len(frontier)

	#runs while frontier is not empty
	while keep_running:
		best_cost_index = None
		current_best_cost = float("inf")
		frontier_length = range(len(frontier))
		for f in frontier_length:
			if frontier[f].get_cost() < current_best_cost:
				best_cost_index = f
				current_best_cost = frontier[f].get_cost()
				
		current_node = frontier.pop(best_cost_index) #removes best_cost_index node in frontier, stores in current_node
		
		#checks if current_node is a solution 
		#compares current_node to best_solution
		#stores new best solution
		if current_node.get_state().is_goal() and current_node.get_cost() < best_cost:
			best_cost = current_node.get_cost()
			best_solution = current_node.get_state()

		#creates child_nodes to search 
		#adds child_nodes to frontier
		child_nodes = current_node.expand()
		nodes_generated = len(child_nodes) + nodes_generated
		for c_n in child_nodes:
			frontier.append(c_n)
			frontier_length = range(len(frontier))
			keep_running = False 
		for f in frontier_length:
			if keep_running == False and frontier[f].get_cost() < best_cost:
				keep_running = True
	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	best_solution.print_state()
	print "Nodes Generated: " + str(nodes_generated)

#User inputs file name
file_name = raw_input("What file do you want to use? ")

#starts breath first search
# depth_first(file_name)
#breadth_first(file_name)
uniform_cost(file_name)
