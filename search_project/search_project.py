"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: takes in a list of tiles and finds the order with the lowest 'cost'
"""


import search_strategies
import time
import sys

#User inputs file name
if len(sys.argv) < 2:
	exit("NO INPUT DATA FILE\n\nPlease type: \nshell$ python search_project.py Path/To/Data/File.txt\n")

file_name = sys.argv[1]


start = time.clock()
search_strategies.start_search(file_name,sys.argv[2])
end = time.clock()

print "Run Time:  " + str(end-start)

