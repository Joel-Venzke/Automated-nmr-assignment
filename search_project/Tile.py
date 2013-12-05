#!/usr/bin/python

import math

class Tile(object):

    #Makes a tile with values a, b, c, d
    def __init__(self,a,b,c,d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    #returns a list of tile values
    def get_tile(self):
        return [self.a, self.b, self.c, self.d]

    #returns a
    def get_a(self):
        return self.a

    #returns b
    def get_b(self):
        return self.b
        
    #returns the sum
    def get_error(self, char):
        return (.05*math.fabs(char[0]-self.a)/self.a+.05*math.fabs(char[0]-self.b)/self.b)

    #takes in next the tile below 
    #returns cost of adding the tile below 
    def compare_below(self, t):
        return  math.fabs((self.c-t.get_a()))+math.fabs((self.d-t.get_b()))