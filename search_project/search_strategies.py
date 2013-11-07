from Tile import Tile
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

	root = Node(tile_set, [], 0.0)

	frontier = [root] #list of nodes

	best_solution = None
	best_cost = float("inf") #set to infinity

	#runs while frontier is not empty
	while frontier:
		current_node = frontier.pop(0) #removes first node in frontier, stores in current_node
		
		#checks if current_node is a solution 
		#compares current_node to best_solution
		#stores new best solution
		if current_node.is_goal() and current_node.get_cost() < best_cost:
			best_cost = current_node.get_cost()
			best_solution = current_node

		#creates child_nodes to search 
		#adds child_nodes to frontier
		child_nodes = current_node.expand()
		for c_n in child_nodes:
			frontier.append(c_n)

	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	print best_solution

#runs a depth_first search
#prints best solution to console
def depth_first(file_name):
	tile_set = read_file(file_name) #list of tiles

	root = Node(tile_set, [], 0.0)

	frontier = [root] #list of nodes

	best_solution = None
	best_cost = float("inf") #set to infinity

	#runs while frontier is not empty
	while frontier:
		current_node = frontier.pop() #removes last node in frontier, stores in current_node
		
		#checks if current_node is a solution 
		#compares current_node to best_solution
		#stores new best solution
		if current_node.is_goal() and current_node.get_cost() < best_cost:
			best_cost = current_node.get_cost()
			best_solution = current_node

		#creates child_nodes to search 
		#adds child_nodes to frontier
		child_nodes = current_node.expand()
		for c_n in child_nodes:
			frontier.append(c_n)

	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	print best_solution

#runs a breath_first search
#prints best solution to console
def uniform_cost(file_name):
	tile_set = read_file(file_name) #list of tiles

	root = Node(tile_set, [], 0.0)

	frontier = [root] #list of nodes

	best_solution = None
	best_cost = float("inf") #set to infinity
	keep_running = True

	#runs while frontier is not empty
	while keep_running:
	        current_cost = float("inf")
	        best_node = None
	        for i in range(len(frontier)):
	            if (frontier[i].get_cost() < current_cost):
	                current_cost = frontier[i].get_cost()
	                best_node = i
		current_node = frontier.pop(best_node) #removes best node in frontier, stores in current_node
		
		#checks if current_node is a solution 
		#compares current_node to best_solution
		#stores new best solution
		if current_node.is_goal() and current_node.get_cost() < best_cost:
			best_cost = current_node.get_cost()
			best_solution = current_node

		#creates child_nodes to search 
		#adds child_nodes to frontier
		child_nodes = current_node.expand()
		for c_n in child_nodes:
			frontier.append(c_n)
		
		keep_running = False
		for i in range(len(frontier)):
		    if (keep_running==False and frontier[i].get_cost() < best_cost):
		        keep_running = True
		
		
	#prints best solution to console
	print "HERE IS THE BEST"
	print best_cost
	print ""
	print best_solution
