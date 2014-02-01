#!/usr/bin/python

import math

class Tile(object):

    #Makes a tile with values a, b, c, d
    def __init__(self,a,b,c,d, place_holder):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.place_holder = place_holder
        self.char_weight = .01
        self.order_weight = .4

    #returns a list of tile values
    def get_tile(self):
        return [self.a, self.b, self.c, self.d]

    #returns place holder boolean
    def get_place_holder(self):
        return self.place_holder

    #returns a
    def get_c(self):
        return self.c

    #returns b
    def get_d(self):
        return self.d
        
    def get_error(self, char):
        if(self.place_holder == True or self.a == -1 and self.b == -1):
            return self.char_weight * .5
        elif(self.a == -1):
            return (math.fabs(char[0]-self.a)*self.char_weight*2)
        elif(self.b == -1):
            return (math.fabs(char[1]-self.b)*self.char_weight*2)
        else:
            return (self.char_weight*math.fabs(char[0]-self.a)+self.char_weight*math.fabs(char[1]-self.b))

    #takes in next the tile above 
    #returns cost of adding the tile above 
    def compare_above(self, t):
        if(self.place_holder == True or t.get_place_holder() == True or self.a == -1 and self.b == -1 or t.c == -1 and t.d ==-1 ):
            return self.order_weight * .3
        elif(self.a == -1 or t.get_c == -1):
            return math.fabs((self.b-t.get_d()))*2*self.order_weight
        elif(self.b == -1 or t.get_d == -1):
            return math.fabs((self.a-t.get_c()))*2*self.order_weight
        else:
            return  (math.fabs((self.a-t.get_c()))+math.fabs((self.b-t.get_d())))*self.order_weight
