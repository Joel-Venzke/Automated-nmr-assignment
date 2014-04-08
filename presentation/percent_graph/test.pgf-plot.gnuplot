set table "test.pgf-plot.table"; set format "%.5f"
set format "%.7e";; fac(x) = (int(x)==0) ? 1.0 : int(x) * fac(int(x)-1.0); g(x) = (a*x**2+b*x+c)/(d*x+e); fit g(x) 'percent.dat' using 1:(log10($2/fac($1))) via a,b,c,d,e; plot 'percent.dat' using 1:(log10($2/fac($1))) title 'Data', g(x); 
