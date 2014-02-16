from Tile import Tile
from Node import Node
import sys
import re

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
			#reads each line, grabs numbers and na data, and adds a new Tile to tile_set_list
			#file format "a b c d"
			a, b, c, d = re.findall(r'\b\d+\.\d*.*?\b|\bna\b', line)

			if (a == "na"):
				a = -1
			if (b == "na"):
				b = -1
			if (c == "na"):
				c = -1
			if (d == "na"):
				d = -1
			tile_set_list.append(Tile(a, b, c, d, False))
		tile_set_list.insert(0, characteristic)
	return tile_set_list

def letters_to_numbers(characteristic):
	temp = []
	new_characteristic = []
	for ch in characteristic:
		ch = ch.lower().strip()
		temp = []
		if ch == "ala":
			temp = [54.8, 18.3, 2]
		elif ch == "cyso":
			temp = [58.0, 39.4, 3]
		elif ch == "cysr":
			temp = [61.3, 27.8, 4]
		elif ch == "asp":
			temp = [56.7, 40.5, 3]
		elif ch == "glu":
			temp = [59.1, 29.4, 4]
		elif ch == "phe":
			temp = [60.8, 38.8, 3]
		elif ch == "gly":
			temp = [46.9, -1, 1]
		elif ch == "his":
			temp = [59.0, 29.5, 4]
		elif ch == "ile":
			temp = [64.6, 37.6, 3]
		elif ch == "lys":
			temp = [58.9, 32.3, 4]
		elif ch == "leu":
			temp = [57.5, 41.6, 3]
		elif ch == "met":
			temp = [58.1, 32.3, 4]
		elif ch == "asn":
			temp = [55.5, 38.6, 3]
		elif ch == "pro":
			temp = [65.5, 31.5, 6]
		elif ch == "gln":
			temp = [58.5, 28.5, 4]
		elif ch == "arg":
			temp = [58.9, 30.1, 4]
		elif ch == "ser":
			temp = [60.9, 63.1, 5]
		elif ch == "thr":
			temp = [65.6, 68.9, 5]
		elif ch == "val":
			temp = [66.2, 31.5, 6]
		elif ch == "trp":
			temp = [60.0, 29.3, 4]
		elif ch == "tyr":
			temp = [61.0, 38.3, 3]
		else:
			print ch
			sys.exit("Amino acid not in database")
		new_characteristic.append(temp)
	return new_characteristic

#finds how many gaps are in the data
#generates placeholder tiles for missing data
#saves new tiles in tile_set
def generate_placeholders(tile_set, characteristic):
	gap = len(characteristic) - len(tile_set)
	if gap > 0:
		for n in range(gap):
			tile_set.append(Tile(-1, -1, -1, -1, True))
	return tile_set


#runs a breath_first search
#prints best solution to console
def uniform_cost(file_name):
	tile_set = read_file(file_name) #list of tiles
	
	characteristic = letters_to_numbers(tile_set.pop(0)) #takes the characteristic array off of the tile_set 
	
	tile_set = generate_placeholders(tile_set, characteristic)

	root = Node(tile_set, [], 0.0, characteristic,0,0)

	frontier = [root] #list of nodes

	best_solution = None
	best_cost = float("inf") #set to infinity
	keep_running = True

	# the following code displays how many tiles are assigned to each tile group
	# for i in range(8):
	# 	sum = 0
	# 	for j in characteristic:
	# 		if (int(j[2]) == i):
	# 			sum += 1
	# 	print str(sum) + "\t" + str(i)

	# print " "
	# for i in range(8):
	# 	sum = 0
	# 	for j in tile_set:
	# 		if (j.get_amino_type() == i):
	# 			sum += 1
	# 	print str(sum) + "\t" + str(i)
	# for i in tile_set:
	# 	print i.get_amino_type()
	
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
			frontier.insert(0, c_n)
		
		keep_running = False
		for i in range(len(frontier)):
		    if (keep_running==False and frontier[i].get_cost() < best_cost):
		        keep_running = True
		
	
	#prints best solution to console
	print "HERE IS THE BEST"
	print "Cost: " + str(best_cost)
	print ""
	print best_solution
	print "Char cost:  " + str(best_solution.get_char_cost())
	print "Order Cost:  " + str(best_solution.get_order_cost())
