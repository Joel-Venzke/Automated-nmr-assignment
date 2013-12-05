from Tile import Tile
from Node import Node

#takes in a file 
#returns list of tiles from the file
def read_file(file_name):
	tile_set_list = []
	characteristic = []

	#runs while file is open
	with open(file_name) as f:

		# READ THE LINE OF CHARACTERISTICS IN HERE
		tile_characteristic = f.readline()
		characteristic = (tile_characteristic.split(' '))

		#reads in all lines in the file
		for line in f:

			#reads each line, splits data at spaces, and adds a new Tile to tile_set_list
			#file format "a b c d"
			a, b, c, d = (s for s in line.split(' '))
			tile_set_list.append(Tile(a, b, c, d))
		tile_set_list.insert(0, characteristic)
	return tile_set_list

def letters_to_numbers(characteristic):
	temp = []
	new_characteristic = []
	for ch in characteristic:
		ch = ch.lower()
		temp = []
		if ch == "ala":
			temp = [54.8, 18.3]
		elif ch == "cyso":
			temp = [58.0, 39.4]
		elif ch == "cysr":
			temp = [61.3, 27.8]
		elif ch == "asp":
			temp = [56.7, 40.5]
		elif ch == "glu":
			temp = [59.1, 29.4]
		elif ch == "phe":
			temp = [60.8, 38.8]
		elif ch == "gly":
			temp = [46.9, float("inf")]
		elif ch == "his":
			temp = [59.0, 29.5]
		elif ch == "ile":
			temp = [64.6, 37.6]
		elif ch == "lys":
			temp = [58.9, 32.3]
		elif ch == "leu":
			temp = [57.5, 41.6]
		elif ch == "met":
			temp = [58.1, 32.3]
		elif ch == "asn":
			temp = [55.5, 38.6]
		elif ch == "pro":
			temp = [65.5, 31.5]
		elif ch == "gln":
			temp = [58.5, 28.5]
		elif ch == "arg":
			temp = [58.9, 30.1]
		elif ch == "ser":
			temp = [60.9, 63.1]
		elif ch == "thr":
			temp = [65.6, 68.9]
		elif ch == "val":
			temp = [66.2, 31.5]
		elif ch == "trp":
			temp = [60.0, 29.3]
		elif ch == "tyr":
			temp = [61.0, 38.3]
		else:
			sys.exit("Amino acid not in database")
		new_characteristic.append(temp)
	return new_characteristic


#runs a breath_first search
#prints best solution to console
def uniform_cost(file_name):
	tile_set = read_file(file_name) #list of tiles
	
	characteristic = letters_to_numbers(tile_set.pop(0)) #takes the characteristic array off of the tile_set 
	print characteristic
	root = Node(tile_set, [], 0.0, characteristic)

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
