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
        self.char_weight = .4
        self.order_weight = .4
        if(self.b == -1.0 and 0<self.a and self.a<50.0):
            self.amino_type = 1 #gly
        elif(0.0<self.b and self.b<20.0 and self.a > 52 and self.a < 56):
            self.amino_type = 2 #ala
        elif(36.0<self.b and self.b < 45.0 and 50.0 < self.a):
            self.amino_type = 3 #asn, asp, leu, cyso
        elif(27.0<self.b and self.b < 35.0 and 54.0 < self.a and self.a<62.0):
            self.amino_type = 4 # met, gln, lys, arg, his, glu, trp, cysr
        elif(61.0<self.b and self.b < 74.0 and 59.0 < self.a and self.a<67.0):
            self.amino_type = 5 # ser, thr
        elif(30.0<self.b and self.b < 35.0 and 62.0 < self.a):
            self.amino_type = 6 #pro, val
        else:
            self.amino_type = 0 # no appropriate match found

    #return amino acid type
    def get_amino_type(self):
        return self.amino_type
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
    def compare_above(self, t): #clean up
        if(self.place_holder == True or t.get_place_holder() == True or self.a == -1 and self.b == -1 or t.get_c() == -1 and t.get_d() ==-1 ):
            return self.order_weight * .3 
        elif(self.a == -1 or t.get_c() == -1):
            if (self.b ==-1 or t.get_d() == -1): # Cleaner way to do this?
                return self.order_weight * .3
            else:
                return math.fabs((self.b-t.get_d()))*self.order_weight
        elif(self.b == -1 or t.get_d() == -1):
            return math.fabs((self.a-t.get_c()))*self.order_weight
        else:
            return  (math.fabs((self.a-t.get_c()))+math.fabs((self.b-t.get_d())))*self.order_weight


