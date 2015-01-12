set term jpeg
set output "plot.jpg"
set log y
set key top left
set title "Time to Completion"
set ylabel "Nodes Genorated"
set xlabel "Number of Amino Acids"
plot "Nodes_Genorated.dat" u 1:2 t "No Filter", "Nodes_Genorated.dat" u 1:3 t "DecisionTable", "Nodes_Genorated.dat" u 1:4 t "j48"