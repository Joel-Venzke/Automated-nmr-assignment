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
    def get_c(self):
        return self.c

    #returns b
    def get_d(self):
        return self.d
        
    #returns the sum
    def get_error(self, char):

        #if its not a gly then error will be inf
        if char[1] == "gly" and self.a > 48:
            return float("inf")
        #if its a gly return error of 0
        elif char[1] == "gly" and self.a < 48:
            return (.05*math.fabs(char[0]-self.a)/self.a)

        #all non gly
        else:
            return (.05*math.fabs(char[0]-self.a)/self.a+.05*math.fabs(char[0]-self.b)/self.b)

    #takes in next the tile below 
    #returns cost of adding the tile below 
    def compare_below(self, t):
        return  math.fabs((self.a-t.get_c()))+math.fabs((self.b-t.get_d()))