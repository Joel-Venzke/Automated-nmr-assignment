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
    def __init__(self,a=0 ,b=0 ,c=0 ,d=0, model=None, pro=False):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.tile_list = []
        self.char_weight = .1
        self.order_weight = 1
        self.amino_type = self.calculate_amino_type(model,pro)


    """
    Group tiles by expected amino acid type 
    """
    def calculate_amino_type(self, model, pro):
        if pro:
            return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        i = Instance.create_instance(values=[1.0, self.a, self.b])
        if (self.a==-1 and self.b==-1 ):
            return [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        elif (self.a==-1):
            i.set_missing(1)
        elif (self.b==-1):
            i.set_missing(2)
        from weka.core.converters import Loader
        loader = Loader("weka.core.converters.ArffLoader")
        myDataset = loader.load_file("weka/testingthisthingout.arff")
        myDataset.set_class_index(0)
        i.set_dataset(myDataset)
        return model.distribution_for_instance(i)

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
            return math.fabs((self.b-t.get_d()))*3.5
        elif(self.b == -1 or t.get_d() == -1): # missing carbon beta data 
            return math.fabs((self.a-t.get_c()))*3.5
        else: # all data exist
            return  (math.fabs((self.a-t.get_c()))+math.fabs((self.b-t.get_d())))*7.0

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
