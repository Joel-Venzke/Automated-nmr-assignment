set term jpeg
set output "plot.jpg"
set datafile missing "?"
set log y
set key top left
set title "Time to Completion"
set ylabel "Nodes Generated"
set xlabel "Number of Amino Acids"
set xrange [1:32]
plot "Nodes_Genorated.dat" u 1:2 t "No Filter" lt 6,\
"Nodes_Genorated.dat" u 1:3 t "DecisionTable"  lt 1,\
"Nodes_Genorated.dat" u 1:4 t "j48" lt 2,\
"lmt.dat" u 1:2 t "LMT" lt 3
set xrange [1:50]
set output "plot1.jpg"
plot "Nodes_Genorated.dat" u 1:2 t "No Filter" w l lt 6,\
"Nodes_Genorated.dat" u 1:3 t "DecisionTable"  w l lt 1,\
"Nodes_Genorated.dat" u 1:4 t "j48" w l lt 2,\
"lmt.dat" u 1:2 t "LMT" w l lt 3
