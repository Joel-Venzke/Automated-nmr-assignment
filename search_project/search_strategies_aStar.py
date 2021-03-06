from Tile_aStar import Tile
from Node_aStar import Node
import sys
import re
import random
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.jvm as jvm
import weka.core.serialization as serialization
import time
from heapq import *

"""
calculates and stores heuristic values for 
all tiles with data compared with the characteristic 
protein sequence
"""
def calculate_char_heuristic(tile_set, characteristic):
	temp = 0
	lowest = float("inf")
	for tile in tile_set:
		for char in characteristic:
			temp = tile.get_error(char)
			if (temp<lowest):
				lowest = temp
		tile.heuristic_cost += lowest

"""
calculates and stores heuristic values for 
all tiles with data compared with all other 
tiles
"""
def calculate_order_heuristic(tile_set):
	temp = 0
	for tile in tile_set:
		# print "HERE"
		# print tile.get_tile()
		lowest = float("inf")
		for tile_comp in tile_set:
			temp = tile_comp.compare_below(tile)
			if (temp<lowest):
				# print tile_comp.get_tile(),
				# print temp
				lowest = temp
		tile.heuristic_cost += lowest
		# print lowest
		tile.heuristic_order_cost = lowest #save to remove when the first tile is placed

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
	print "Pro Count: " + str(pro_count) + "\nMissing: " + str(gap)
	if gap > 0:
		for n in range(gap):
			# print "making"
			tile_set.append(Tile(-1, -1, -1, -1, nmrClass, heuristic=1.9)) # add place holder tiles to tile set
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
		ch = ch.lower().strip() # deal with case problems and returns
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
Take in a list of Nodes and converts it to a 
heap with the cost of a node being the value
used to create the heap
"""
def listToHeap(data):
	for i in xrange(len(data)):
		data[i] = (data[i].cost, data[i])
	heapify(data)

"""
prints results to console
take in a solution node and the number of nodes generated
"""
def output_soultion(finalNode, nodeCount):
	# Uncomment to record results to data file for scripted runs
	
	# with open("../Results_Winter_2014-15/spring2k15_missing.dat", "a") as dataFile:
	# 	dataFile.write(str(len(finalNode.characteristic)) + "\t" + str(nodeCount) + "\n")

	#prints best solution to console
	print "HERE IS THE BEST"
	print "Cost: " + str(finalNode.cost)
	print ""
	print finalNode
	print "Char cost:  " + str(finalNode.char_cost)
	print "Order Cost:  " + str(finalNode.order_cost)
	print "Nodes: " + str(nodeCount)


"""
This search will select 20 random tiles to assign, run a uniform cost search and then group tiles until a final state is found
Takes in a list of tiles 
Returns a single tile that contains a lits of tiles
"""
def puzzle_building_search(frontier, numSolutions, depthVal):
	#make this maintain the list of nodes being used to start and end the uniform cost search
	# uniform cost search may want to have 3 variables: 
	# one for the frontier (some changes will need to make this happen)
	# one for the depth needed for termination of that layer of the search (the number I talked about in the meeting)
	# one for the number of nodes to return at the completion of the search
	return frontier


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
	# start jvm: the jvm is used for the machine learning filtering 
	# so that weka can be run
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
			# adds a new Tile to tile_set_list if its not a placeholder
			if (not (a==-1 and b==-1 and c==-1 and d==-1)): # needed for proline checking
				tile_set_list.append(Tile(a, b, c, d, nmrClass)) 
	return tile_set_list, characteristic, nmrClass


"""
runs the search on the data
takes in file name and search type number
outputs results to console
"""
def start_search(file_name, type):
	start = time.clock() # time Preprocessing
	tile_set, characteristic, nmrClass = read_file(file_name)
	calculate_char_heuristic(tile_set, characteristic) # do before you add the place holder tiles
	tile_set = generate_placeholders(tile_set, characteristic, nmrClass) # gets place holder tiles
	# kill jvm that was started after calling read file
	# the jvm is used for the machine learning filtering 
	# so that weka can be run
	jvm.stop() 
	calculate_order_heuristic(tile_set)

	# add up heuristic from all tiles and make starting node
	heuristic_val = 0
	for tile in tile_set:
		heuristic_val += tile.heuristic_cost
		# print tile.heuristic_order_cost,
		# print tile.get_tile()
	root = Node(tile_set, [], heuristic_val, characteristic,0,0, heuristic=heuristic_val) # makes start state for search

	end = time.clock() # time Preprocessing
	print "Preprocessing Time:  " + str(end-start)
	
	# picks algorithm
	if (int(type) == 0): # uniform cost search
		best_solution, node_count = aStar([root])
		output_soultion(best_solution, node_count)
	elif (int(type) == 1): # puzzle building
		best_solution = puzzle_building_search([root]) 


"""
preforms a uniform cost search on a node
takes in a starting node for the search 
returns the best solution
"""
# @profile
# TODO take in node count, number of tiles to place, and number of solutions to return
def aStar(frontier): 
	# frontier = [root] # holds list of node that need exploring
	# # the following code is for setting up new machine learning models
	# # if the is your goal, uncomment this and talk to Joel Venzke on how to use it
	# lowest = 1.0
	# for i in range(len(root.unplaced_tiles)):
	# 	if (root.unplaced_tiles[i].amino_type[root.characteristic[i][2]] < lowest):
	# 		lowest = root.unplaced_tiles[i].amino_type[root.characteristic[i][2]]
	# print "lowest cutoff: " + str(lowest)
	
	# make the fronter into a heap
	# this allows for more than one node to be passed in
	listToHeap(frontier) 
	node_count = 1
	best_solution = None
	best_cost = float("inf") 
	keep_running = True

	while keep_running: # loop till the best solution has been found

		# Get best node to start loop
		current_node = heappop(frontier)[1] 

		# checks if a new best solution has been found
		# if it has the solution is stored
		if (current_node.is_goal() and current_node.cost < best_cost):
			best_cost = current_node.cost
			best_solution = current_node

		# creates child_nodes to search 
		# adds child_nodes to frontier
		node_count+=current_node.expand(frontier)
		
		# checks to see if the best solution is the true best solution
		# and if there are any other solutions left to explore
		# restarts loop if the best solution is not proven optimal
		keep_running = False
		if (frontier and frontier[0][0] < best_cost):
			keep_running = True 

	# returns best solution and number of nodes generated
	# TODO make this return more than one solution
	return best_solution, node_count

