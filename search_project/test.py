#!/usr/bin/python

from Tile import Tile

my_tile = Tile(1,2,3,4)
my_tile2 = Tile(3,4,1,2)

print my_tile.compare_below(my_tile2)

