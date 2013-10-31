"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: takes in a list of tiles and finds the order with the lowest 'cost'
"""

import search_strategies

#User inputs file name
file_name = raw_input("What file do you want to use? ")

strategy = raw_input("What search strategy do you want to use?\na) breadth_first \nb) depth_first \nc) uniform_cost\n")

if(strategy == "a"):
	search_strategies.breadth_first(file_name)
elif(strategy == "b"):
	search_strategies.depth_first(file_name)
else:
	search_strategies.uniform_cost(file_name)