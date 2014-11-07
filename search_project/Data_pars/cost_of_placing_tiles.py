import search_strategies
import sys

tiles, char = search_strategies.read_file(sys.argv[1])
total_cost = 0
for i in xrange(len(tiles)-1):
	total_cost += tiles[i].compare_below(tiles[i+1]) + tiles[i].get_error(char[i])
	print str(i+1) + '\t' + str(tiles[i].compare_below(tiles[i+1])) + '\t' + str(tiles[i].get_error(char[i])) +'\t' + str(tiles[i].compare_below(tiles[i+1]) + tiles[i].get_error(char[i]))

print total_cost/(len(tiles)-1)