#!/usr/bin/python

import math
from weka.core.dataset import Instance
from weka.classifiers import Classifier


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
    def __init__(self,a=0 ,b=0 ,c=0 ,d=0, model=None, pro=False, heuristic=0.0):
        self.a = float(a) # carbon alpha i
        self.b = float(b) # carbon beta i
        self.c = float(c) # carbon alpha i-1
        self.d = float(d) # carbon beta i-1
        self.char_weight = .1 # Scale for characteristic weight (get_error)
        self.order_weight = 1 # Scale for order weight (compare_below)
        self.heuristic_cost = heuristic # holds total heuristic cost
        self.heuristic_order_cost = 0 # holds order cost to allow for its removal
        self.amino_type = self.calculate_amino_type(model,pro) # list of amino acids


    """
    Group tiles by expected amino acid type 
    """
    def calculate_amino_type(self, model, pro):
        if pro: # the 12th index is 2 so we can pick it out. all others are zero so it is not place in other locations
            return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        # builds a instance for the model
        i = Instance.create_instance(values=[1.0, self.a, self.b])
        if (self.a==-1 and self.b==-1 ): # place holder
            return [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        elif (self.a==-1): # update instance for missing data
            i.set_missing(1)
        elif (self.b==-1): # update instance for missing data
            i.set_missing(2)

        # read in blank dataset
        from weka.core.converters import Loader
        loader = Loader("weka.core.converters.ArffLoader")
        myDataset = loader.load_file("weka/testingthisthingout.arff")
        myDataset.set_class_index(0)

        # use model to predict amino acid type
        i.set_dataset(myDataset)
        return model.distribution_for_instance(i)


    """
    Calculates order cost
    Take in the tile placed bellow the current tile 
    returns cost of placing that tile after the current tile
    """
    def compare_below(self, t): #clean up
        if(self.a == -1 and self.b == -1 or \
            t.c == -1 and t.d ==-1 or \
             t.d == -1 and self.a == -1 or \
              t.c == -1 and self.b == -1): # place holder tile or too much missing data
            return 1.9
        elif(self.a == -1 or t.c == -1): # missing carbon alpha data
            return math.fabs((self.b-t.d))*3.5
        elif(self.b == -1 or t.d == -1): # missing carbon beta data 
            return math.fabs((self.a-t.c))*3.5
        else: # all data exist
            return  (math.fabs((self.a-t.c))+math.fabs((self.b-t.d)))*7.0

    """
    returns the cost of the tile compared to an amino acid in the characteristic protein sequence
    """
    def get_error(self, char):
        if( self.a == -1 and self.b == -1): # place holder tile
            return 0
        elif(self.a == -1): # no carbon alpha 
            return math.fabs(char[0]-self.a)*1.0
        elif(self.b == -1): # no carbon beta
            return math.fabs(char[1]-self.b)*1.0
        else: # has both carbon alpha and beta
            return (math.fabs(char[0]-self.a)+math.fabs(char[1]-self.b))*.071

    """
    return a list of the tile's carbon shift values
    """
    def get_tile(self):
        return [self.a, self.b, self.c, self.d]
