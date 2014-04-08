fac(x) = (int(x)==0) ? 1.0 : int(x) * fac(int(x)-1.0)
g(x) = (a*x**2+b*x+c)/(d*x+e)
fit g(x) 'percent.dat' using 1:(log10($2/fac($1))) via a,b,c,d,e
set terminal jpeg 
set xrange [0:45]
set yrange [-50:1]
set ylabel 'Percent of Nodes Genorated (order of magnitude)'
set xlabel 'Number of Residues'
set output 'percent.jpeg'
set xtics 5
set ytics 5
set grid lt 1 lc rgb '#bbbbbb' lw .1
unset key 
plot 'percent.dat' using 1:(log10($2/fac($1))) pt 4 ps .5 lc rgb 'black', g(x) linecolor rgb "red"