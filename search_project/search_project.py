"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: takes in a list of tiles and finds the order with the lowest 'cost'
"""


import search_strategies
import time
import sys

#User inputs file name
file_name = sys.argv[1]

start = time.clock()
search_strategies.uniform_cost(file_name)
end = time.clock()
# print "Run Time:  " + str(end-start)

