#!/usr/bin/python

import math

class Tile(object):

    #Makes a tile with values a, b, c, d
    def __init__(self,a,b,c,d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    #returns a
    def get_a(self):
        return self.a

    #returns b
    def get_b(self):
        return self.b

    #takes in next the tile below 
    #returns cost of adding the tile below 
    def compare_below(self, t):
        return  math.fabs((self.c-t.get_a()))+math.fabs((self.d-t.get_b()))