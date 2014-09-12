#!/usr/bin/python

class Tile(object):

    #Makes a tile with values a, b, c, d
    def __init__(self,a,b,c,d, place_holder):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def print_tile(self):
        return str(self.a) + "\t" + str(self.b) + "\t" + str(self.c) + "\t" + str(self.d) 
