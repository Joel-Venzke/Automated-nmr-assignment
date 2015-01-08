set term jpeg
set output "plot.jpg"
set log y
plot "Nodes_Genorated.dat" u 1:2 t "2", "Nodes_Genorated.dat" u 1:4 t "4"