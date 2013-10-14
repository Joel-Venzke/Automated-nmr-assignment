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
    def setTile(self,a,b,c,d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    #sets a as i
    def setA(self,i):
        self.a = i

    #sets b as i
    def setB(self,i):
        self.b = i

    #sets c as i
    def setC(self, i):
        self.c = i

    #sets d as i
    def setD(self, i):
        self.d = i

    #returns a list of tile values
    def getTile(self):
        return [self.a, self.b, self.c, self.d]

    #returns a
    def getA(self):
        return self.a

    #returns b
    def getB(self):
        return self.b

    #returns c
    def getC(self):
        return self.c

    #returns d
    def getD(self):
        return self.d

    #takes in next the tile below 
    #returns cost of adding the tile below 
    def compare_below(self, t):
        self.compare = math.fabs((self.c-t.getA()))+math.fabs((self.d-t.getB()))
        return self.compare