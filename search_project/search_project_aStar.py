"""
Name: Joel Venzke, Katie Roth, Paxten Johnson, Rachel Davis, Leah Robison, John Emmons, Tim Urness, Adina Kilpatrick
Date created: October 12th, 2013
Description: This program automates the assignment of NMR data. 
				The data is read in from a file and then the search will begin.
				A uniform cost search is used if a 0 is given in the run command
				A "puzzle building" search is completed if a 1 is given in the run command
				
				For further infromation on the project please see our paper:
				http://www.micsymposium.org/mics2014/ProceedingsMICS_2014/mics2014_submission_35.pdf
				or email joel.venzke@drake.edu

				To run the code use the following command:
				shell$ python search_project.py Path/To/Data/File.txt NumberOfSearchType
"""


import search_strategies_aStar
import time
import sys

# Error if not enough data is provided
if len(sys.argv) < 2:
	exit("NO INPUT DATA FILE OR MISSING SEARCH TYPE NUMBER\n\nPlease type: \nshell$ python search_project.py Path/To/Data/File.txt NumberOfSearchType\
		\n\nSearch Type Numbers:\nUniform Cost: 0\nPuzzle Building: 1")

# time and run search
start = time.clock()
search_strategies_aStar.start_search(sys.argv[1],sys.argv[2])
end = time.clock()

print "Run Time:  " + str(end-start)