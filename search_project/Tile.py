#!/usr/bin/python

import math

class Tile(object):

    #Makes a tile with values a, b, c, d
    def __init__(self,a,b,c,d, place_holder=False, tile_list=[]):
        if (not tile_list):
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
            self.d = float(d)
            self.tile_list = []
            self.place_holder = place_holder
            self.char_weight = .1
            self.order_weight = 1
            self.tile_list_cost = 0
            self.amino_type = self.calculate_amino_type()
        else:
            self.tile_list = tile_list
            self.amino_type = 0
            self.placeholder = False
            self.char_weight = .1
            self.order_weight = 1
            
            #assigns a and b of the last tile to the a and b value
            #of combined tile
            self.a = float(tile_list[-1].a)
            self.b = float(tile_list[-1].b)

            #assigns c and d of the fist tile to the c and d value
            #of the combined tiles
            self.c = float(tile_list[0].c)
            self.d = float(tile_list[0].d)
            self.tile_list_cost = self.calculate_tile_list_cost()


    def calculate_tile_list_cost(self):
        last = len(self.tile_list)
        cost = 0
        for i in xrange(last):
            if (i==last-1):
                return cost
            else:
                cost += self.tile_list[i].compare_above(self.tile_list[i+1])

    def calculate_amino_type(self):
        if(self.b == -1.0 and 0<self.a and self.a<50.0):
            return 1 #gly
        elif(0.0<self.b and self.b<20.0 and self.a > 52 and self.a < 56):
            return 2 #ala
        elif(36.0<self.b and self.b < 45.0 and 50.0 < self.a):
            return 3 #asn, asp, leu, cyso
        elif(27.0<self.b and self.b < 35.0 and 54.0 < self.a and self.a<62.0):
            return 4 # met, gln, lys, arg, his, glu, trp, cysr
        elif(61.0<self.b and self.b < 74.0 and 59.0 < self.a and self.a<67.0):
            return 5 # ser, thr
        elif(30.0<self.b and self.b < 35.0 and 62.0 < self.a):
            return 6 #pro, val
        else:
            return 0 # no appropriate match found

    #return amino acid type
    def get_amino_type(self):
        return self.amino_type
    #returns a list of tile values
    def get_tile(self):
        return [self.a, self.b, self.c, self.d]

    #returns place holder boolean
    def get_place_holder(self):
        return self.place_holder

    #returns c
    def get_c(self):
        return self.c

    #returns d
    def get_d(self):
        return self.d
        
    def get_error(self, char):
        if(self.place_holder == True or self.a == -1 and self.b == -1):
            return 0
        elif(self.a == -1):
            return math.fabs(char[0]-self.a)*.5
        elif(self.b == -1):
            return math.fabs(char[1]-self.b)*.5
        else:
            return (math.fabs(char[0]-self.a)+math.fabs(char[1]-self.b))*.1

    #takes in next the tile above 
    #returns cost of adding the tile above 
    def compare_above(self, t): #clean up
        if(self.place_holder == True or \
            t.get_place_holder() == True or \
            self.a == -1 and self.b == -1 or \
             t.get_c() == -1 and t.get_d() ==-1 or \
              t.get_d() == -1 and self.a == -1 or \
               t.get_c() == -1 and self.b == -1):
            return 1.9
        elif(self.a == -1 or t.get_c() == -1):
            return math.fabs((self.b-t.get_d()))*4.75
        elif(self.b == -1 or t.get_d() == -1):
            return math.fabs((self.a-t.get_c()))*4.75
        else:
            return  (math.fabs((self.a-t.get_c()))+math.fabs((self.b-t.get_d())))*7



