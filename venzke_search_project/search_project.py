"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: takes in a list of tiles and finds the order with the lowest 'cost'
"""
from Tile import Tile
from State import State
from Node import Node

#takes in file 
#returns list of tiles from the file
def read_file(fileName):
	tileSetList = []
	with open(fileName) as f:
		for line in f:
			t1, t2, t3, t4 = (s for s in line.split(' '))
			tileSetList.append(Tile(t1, t2, t3, t4))
	return tileSetList

#takes in file
#runs a breath_first search
#prints best solution to console
def breadth_first(fileName):
	tileSet = read_file(fileName) #list of tiles
	startState = State([],tileSet) #State with no placed tiles
	root = Node(startState, 0.0, None) #First Node, no cost, no parent
	frontier = [root] #list of nodes
	bestSolution = State([],[]) #stores best solution
	bestCost = float("inf") #set to infinity

	#runs while frontier is not empty
	while frontier:
		currentNode = frontier.pop(0) #removes first node in frontier, stores in currentNode
		
		#checks if currentNode is a solution 
		#compares currentNode to bestSolution
		#stores new best solution
		if currentNode.getState().isGoal() and currentNode.getCost() < bestCost:
			bestCost = currentNode.getCost()
			bestSolution = currentNode.getState()

		#creates childNodes to search 
		#adds childNodes to frontier
		childNodes = currentNode.expand()
		for cN in childNodes:
			frontier.append(cN)

	#prints best solution to console
	print "HERE IS THE BEST"
	print bestCost
	print ""
	bestSolution.printState()

#User inputs file name
fileName = raw_input("What file do you want to use? ")

#starts breath first search
breadth_first(fileName)