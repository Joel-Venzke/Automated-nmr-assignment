from Venzke_Tile import Tile


t = Tile(1,25,1,12)
t1 = Tile(2,1,1,9)
print t.compare_below(t1)
print t1.compare_below(t)