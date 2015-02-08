from Tile2 import Tile
from Node2 import Node
import sys
import re
import random
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.jvm as jvm
import weka.core.serialization as serialization

"""
groups tiles together if there error is low enough
takes in a list of assigned tiles
returns a list of tiles and grouped tiles
"""
def find_matches(tiles):
	outputNode = tiles
	# lots of work needed =================================================================================
	# lots of work needed =================================================================================
	# lots of work needed =================================================================================
	# lots of work needed =================================================================================
	return outputNode


"""
Creates enough place holder tiles to do a full search
takes in the tile set and characteristic lists
returns tile list with place holder tiles
"""
def generate_placeholders(tile_set, characteristic, nmrClass):
	pro_count = 0
	for i in characteristic:
		if (i[2] ==12):
			pro_count +=1
			tile_set.append(Tile(-1,-1,-1,-1,nmrClass,pro=True))
			# print tile_set[-1].amino_type[12]
	gap = len(characteristic) - len(tile_set) # number of place holder tiles needed
	if gap > 0:
		for n in range(gap):
			# print "making"
			tile_set.append(Tile(-1, -1, -1, -1, nmrClass)) # add place holder tiles to tile set
	return tile_set


"""
Converts protein sequence strings into expected chemical shift values
takes in a list of strings
returns a list of lists that hold a carbon alpha and carbon beta value
"""
def letters_to_numbers(characteristic):
	temp = []
	new_characteristic = []
	for ch in characteristic: # loop through the whole list
		ch = ch.lower().strip() # deal with case problems
		temp = []
		# finds amino acid type and gets expected chemical shift data
		# Values come from BRMB data. The exact values are the average
		# Ca and Cb values as recorded on 01-22-2015
		# Here is the link: http://www.bmrb.wisc.edu/ref_info/statsel.htm
		# the last index is for amino acid type identification in the 
		# machine learning model
		if ch == "ala":
			temp = [53.19, 18.96, 0]
		elif ch == "cys":
			temp = [58.23, 32.85, 1]
		elif ch == "asp":
			temp = [54.70, 40.87, 2]
		elif ch == "glu":
			temp = [57.35, 29.97, 3]
		elif ch == "phe":
			temp = [58.14, 39.94, 4]
		elif ch == "gly":
			temp = [45.36, -1, 5]
		elif ch == "his":
			temp = [56.52, 30.22, 6]
		elif ch == "ile":
			temp = [61.67, 38.58, 7]
		elif ch == "lys":
			temp = [56.98, 32.77, 8]
		elif ch == "leu":
			temp = [55.69, 42.26, 9]
		elif ch == "met":
			temp = [56.13, 32.94, 10]
		elif ch == "asn":
			temp = [53.56, 38.68, 11]
		elif ch == "pro":
			temp = [63.36, 31.84, 12]
		elif ch == "gln":
			temp = [56.62, 29.16, 13]
		elif ch == "arg":
			temp = [56.82, 30.65, 14]
		elif ch == "ser":
			temp = [58.75, 63.79, 15]
		elif ch == "thr":
			temp = [62.26 , 69.71, 16]
		elif ch == "val":
			temp = [62.58, 32.71, 17]
		elif ch == "trp":
			temp = [57.74, 29.97, 18]
		elif ch == "tyr":
			temp = [58.18, 39.27, 19]

		# deal with data that is not in our list
		else:
			print ch
			sys.exit("Amino acid not in database")

		# add data to the list
		new_characteristic.append(temp)
	return new_characteristic


"""
prints results to console
take in a solution node and the number of nodes generated
"""
def output_soultion(finalNode, nodeCount):
	# Uncomment to record results to data file for scripted runs
	
	# with open("../Results_Winter_2014-15/profix_lmt_3sd.dat", "a") as dataFile:
	# 	dataFile.write(str(len(finalNode.characteristic)) + "\t" + str(nodeCount) + "\n")

	#prints best solution to console
	print "HERE IS THE BEST"
	print "Cost: " + str(finalNode.get_cost())
	print ""
	print finalNode
	print "Char cost:  " + str(finalNode.get_char_cost())
	print "Order Cost:  " + str(finalNode.get_order_cost())
	print "Nodes: " + str(nodeCount)


"""
This search will select 20 random tiles to assign, run a uniform cost search and then group tiles until a final state is found
Takes in a list of tiles 
Returns a single tile that contains a lits of tiles
"""
def puzzle_building_search(allTiles):
	while len(allTiles) > 1: # while we have more than one tile

		# get up to 20 random tiles from the list
		tempTileArray = []
		if (len(allTiles)>20):
			for i in xrange(20):
				randomNum = random.ranint(0,len(allTiles)-1)
				tempTileArray.append(allTiles.pop(randomNum))
		else: 
			tempTileArray = allTiles

		# preform a uniform cost search
		tempNode = Node(tempTileArray,[],0,[],0,0) # make a starting node for a uniform cost search
		outputNode, count = uniform_cost(tempNode) # preform search

		# group tiles together 
		newList = find_matches(outputNode.placed_tiles)

		# add tiles back onto the list of tiles
		for i in len(newList):
			allTiles.append(newList[i])
	return allTiles[0]


"""
Reads in the data from the provided file
Returns the tile set and characteristic

The first line of the file should contain the letters of the protein sequence
with each residue being represented in its 3 letter form (4 letters in the cases of cyso and cysr)
The rest of the file should contain the Carbon Shift data.
Each line should be one residue with the data in the following order with a space or tab between each data point
carbon alpha i, carbon beta i, carbon alpha i-1, carbon beta i-1
any missing data should be replaced with "na"
i.e: 
Asp Gln Leu
54.796 41.361 51.848 19.414
55.396 30.413 na 	 41.328
54.501 43.445 55.437 na
"""
def read_file(file_name):
	tile_set_list = []
	characteristic = []
	jvm.start()
	nmrClass = Classifier(jobject=serialization.read("models/lmt_3sd.model"))
	with open(file_name) as f: # opens file

		# reads in characteristic protein sequence and coverts it to expected chemical shift values
		tile_characteristic = f.readline()
		characteristic = re.findall(r'\b[A-Za-z]{3,4}\b', tile_characteristic)
		characteristic = letters_to_numbers(characteristic)

		for line in f: # reads in NMR Data
			#reads each line and grabs numbers and na data
			#file format "a b c d"
			a, b, c, d = re.findall(r'\b\d+\.\d*\b|\bna\b', line)
			# Dealing with missing data
			if (a == "na"):
				a = -1
			if (b == "na"):
				b = -1
			if (c == "na"):
				c = -1
			if (d == "na"):
				d = -1
			# adds a new Tile to tile_set_list
			if (not (a==-1 and b==-1 and c==-1 and d==-1)):
				tile_set_list.append(Tile(a, b, c, d, nmrClass)) 
	return tile_set_list, characteristic, nmrClass


"""
runs the search on the data
takes in file name and search type number
outputs results to console
"""
def start_search(file_name, type):
	tile_set, characteristic, nmrClass = read_file(file_name) # gets data from file
	tile_set = generate_placeholders(tile_set, characteristic, nmrClass) # gets place holder tiles
	jvm.stop()
	root = Node(tile_set, [], 0.0, characteristic,0,0) # makes start state for search

	# picks algorithm
	if (int(type) == 0): # uniform cost search
		best_solution, node_count = uniform_cost(root)
		output_soultion(best_solution, node_count)
	elif (int(type) == 1): # puzzle building
		best_solution = puzzle_building_search(root)


"""
preforms a uniform cost search on a node
takes in a starting node for the search 
returns the best solution
"""
def uniform_cost(root):
	frontier = [root] # holds list of node that need exploring
	# lowest = 1.0
	# for i in range(len(root.unplaced_tiles)):
	# 	if (root.unplaced_tiles[i].amino_type[root.characteristic[i][2]] < lowest):
	# 		lowest = root.unplaced_tiles[i].amino_type[root.characteristic[i][2]]
	# print lowest

	node_count = 1
	best_solution = None
	best_cost = float("inf") 
	keep_running = True

	while keep_running: # loop till the best solution has been found

		# find the lowest cost node in the frontier
		current_cost = float("inf")
		best_node = None
		for i in xrange(len(frontier)):
			if (frontier[i].get_cost() < current_cost):
				current_cost = frontier[i].get_cost()
				best_node = i
		current_node = frontier.pop(best_node) #removes best node in frontier, stores in current_node
		
		# checks if a new best solution has been found
		# if it has the solution is stored
		if (current_node.is_goal() and current_node.get_cost() < best_cost):
			best_cost = current_node.get_cost()
			best_solution = current_node

		# creates child_nodes to search 
		# adds child_nodes to frontier
		child_nodes = current_node.expand()
		node_count = node_count + len(child_nodes)
		for c_n in child_nodes:
			frontier.insert(0, c_n)

		# checks to see if the best solution is the true best solution
		# restarts loop if the best solution is not proven optimal
		keep_running = False
		for i in xrange(len(frontier)):
		    if (keep_running==False and frontier[i].get_cost() < best_cost):
		        keep_running = True 

	# returns best solution and number of nodes generated
	return best_solution, node_count

