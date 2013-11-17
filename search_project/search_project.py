"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: takes in a list of tiles and finds the order with the lowest 'cost'
"""


import search_strategies
import time

#User inputs file name
file_name = raw_input("What file do you want to use? ")

strategy = raw_input("What search strategy do you want to use?\na) breadth_first \nb) depth_first \nc) uniform_cost\n")

if(strategy == "a"):
        start = time.clock()
	search_strategies.breadth_first(file_name)
	end = time.clock()
	print ("Run Time:  ", end-start)
elif(strategy == "b"):
        start = time.clock()
	search_strategies.depth_first(file_name)
	end = time.clock()
	print ("Run Time:  ", end-start)
else:
        start = time.clock()
	search_strategies.uniform_cost(file_name)
	end = time.clock()
	print "Run Time:  " + str(end-start)
