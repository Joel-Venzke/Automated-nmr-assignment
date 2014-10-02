#!/usr/bin/python

import math


"""
A Tile contains the NMR data for a single amino acid or a list of amino acids
"""

class Tile(object):

    """
    To generate a tile provide (a,b,c,d) or (tile_list)
    a: carbon alpha value for residue i
    b: carbon beta value for residue i
    c: carbon alpha value for residue i-1
    d: carbon beta value for residue i-1
    tile_list: A list of tiles that have been grouped together
    """
    def __init__(self,a=0 ,b=0 ,c=0 ,d=0, tile_list=[]):
        if (not tile_list): # not given a tile list
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
            self.d = float(d)
            self.tile_list = []
            self.char_weight = .1
            self.order_weight = 1
            self.tile_list_cost = 0
            self.amino_type = self.calculate_amino_type()
        else: # create a tile form the tile_list
            self.tile_list = tile_list
            self.amino_type = 0
            self.char_weight = .1
            self.order_weight = 1
            
            #assigns a and b of the last tile to the a and b value of combined tile
            self.a = float(tile_list[-1].a)
            self.b = float(tile_list[-1].b)

            #assigns c and d of the fist tile to the c and d value of the combined tiles
            self.c = float(tile_list[0].c)
            self.d = float(tile_list[0].d)

            # calculate the cost of the tile
            self.tile_list_cost = self.calculate_tile_list_cost()


    """
    Group tiles by expected amino acid type 
    """
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


    """
    calculate the cost inside the list of tiles
    """
    def calculate_tile_list_cost(self):
        last = len(self.tile_list)
        cost = 0
        for i in xrange(last): # loop though tiles
            if (i==last-1): # if last tile return cost
                return cost
            else: # calculated cost of 
                cost += self.tile_list[i].compare_below(self.tile_list[i+1])

    """
    Calculates order cost
    Take in the tile placed bellow the current tile 
    returns cost of placing that tile after the current tile
    """
    def compare_below(self, t): #clean up
        if(self.a == -1 and self.b == -1 or \
            t.get_c() == -1 and t.get_d() ==-1 or \
             t.get_d() == -1 and self.a == -1 or \
              t.get_c() == -1 and self.b == -1): # place holder tile or too much missing data
            return 1.9
        elif(self.a == -1 or t.get_c() == -1): # missing carbon alpha data
            return math.fabs((self.b-t.get_d()))*4.75
        elif(self.b == -1 or t.get_d() == -1): # missing carbon beta data 
            return math.fabs((self.a-t.get_c()))*4.75
        else: # all data exist
            return  (math.fabs((self.a-t.get_c()))+math.fabs((self.b-t.get_d())))*7

    """
    return the expected amino acid group 
    """
    def get_amino_type(self):
        return self.amino_type

    """
    returns the carbon alpha value for residue i-1
    """
    def get_c(self):
        return self.c

    """
    returns the carbon beta value for residue i-1
    """
    def get_d(self):
        return self.d

    """
    returns the cost of the tile compared to an amino acid in the characteristic protein sequence
    """
    def get_error(self, char):
        if( self.a == -1 and self.b == -1): # place holder tile
            return 0
        elif(self.a == -1): # no carbon alpha 
            return math.fabs(char[0]-self.a)*.5
        elif(self.b == -1): # no carbon beta
            return math.fabs(char[1]-self.b)*.5
        else: # has both carbon alpha and beta
            return (math.fabs(char[0]-self.a)+math.fabs(char[1]-self.b))*.1

    """
    return a list of the tile's carbon shift values
    """
    def get_tile(self):
        return [self.a, self.b, self.c, self.d]
