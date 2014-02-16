"""
Name: Joel Venzke
Date created: October 12th, 2013
Description: Contains a tile where the 
             upper left value is a 
             upper right value is b
             lower left value is c and
             lower right value is d
"""
import math

class Tile(object):

    #Makes a tile with values a, b, c, d
    def __init__(self,a,b,c,d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    #sets all values in a tile
    def set_tile(self,a,b,c,d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    #sets a as i
    def set_a(self,i):
        self.a = i

    #sets b as i
    def set_b(self,i):
        self.b = i

    #sets c as i
    def set_c(self, i):
        self.c = i

    #sets d as i
    def set_d(self, i):
        self.d = i

    #returns a list of tile values
    def get_tile(self):
        return [self.a, self.b, self.c, self.d]

    #returns a
    def get_a(self):
        return self.a

    #returns b
    def get_b(self):
        return self.b

    #returns c
    def get_c(self):
        return self.c

    #returns d
    def get_d(self):
        return self.d

    #takes in next the tile below 
    #returns cost of adding the tile below 
    def compare_below(self, t):
        self.compare = math.fabs((self.c-t.get_a()))+math.fabs((self.d-t.get_b()))
        return self.compare