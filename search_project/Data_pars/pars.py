import sys
from Tile import Tile
import re


def read_file(file_name):
	tile_set_list = []
	characteristic = []

	#runs while file is open
	with open(file_name) as f:

		# READ THE LINE OF CHARACTERISTICS IN HERE
		tile_characteristic = f.readline()
		characteristic = re.findall(r'\b[A-Za-z]{3,4}\b', tile_characteristic)

		#reads in all lines in the file
		for line in f:
			#reads each line, grabs numbers and na data, and adds a new Tile to tile_set_list
			#file format "a b c d"
			a, b, c, d = re.findall(r'\b\d+\.\d*\b|\bna\b', line)
			
			tile_set_list.append(Tile(a, b, c, d, False))
		tile_set_list.insert(0, characteristic)
	return tile_set_list

#User inputs file name
if len(sys.argv) < 3:
	exit("NO INPUT DATA FILE\n\nPlease type: \nshell$ python search_project.py Path/To/Data/File.txt numberOfDataPoints\n")

file_name = sys.argv[1]
num = int(sys.argv[2])


tile_set = read_file(file_name)
characteristic = tile_set.pop(0)
for i in range(num):
	print characteristic[i],
print 
for i in range(num):
	print tile_set[i].print_tile()
