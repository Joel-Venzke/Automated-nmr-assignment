import math

class Tile(object):
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def set_a(self,i):
        self.a = i
    def set_b(self,i):
        self.b = i
    def set_c(self, i):
        self.c = i
    def set_d(self, i):
        self.d = i
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_c(self):
        return self.c
    def get_d(self):
        return self.d
    def compare_below(self, t):
        self.compare = math.fabs((self.c+self.d)-(t.get_a()+t.get_b()))
        return self.compare