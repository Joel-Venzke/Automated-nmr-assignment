fac(x) = (int(x)==0) ? 1.0 : int(x) * fac(int(x)-1.0)
g(x) = (a*x**2+b*x+c)/(d*x+e)
fit g(x) 'percent.dat' using 1:(log10($2/fac($1))) via a,b,c,d,e
set terminal jpeg #epslatex color
#set xrange [0:45]
#set yrange [-50:1]
set ylabel 'Nodes Generated'
set xlabel 'Number of Residues'
set output 'percent.jpg'#.tex'
#set xtics 5
#set ytics 5
#set grid lt 1 lc rgb '#bbbbbb' lw .1
set key top left
plot 'percent.dat' using 1:($2) t 'old' pt 7 ps 1 lc rgb 'red', 'percent.dat' using 1:($3) t 'Machine learning' pt 7 ps 1 lc rgb 'blue'#, g(x) lt 1 linecolor rgb "red"