set term jpeg
set output "plot.jpg"
set datafile missing "?"
set log y
set key top left
set title "Time to Completion"
set ylabel "Nodes Generated"
set xlabel "Number of Amino Acids"
set xrange [1:32]
plot "lmt_3sd.dat" u 1:2 t "LMT 3sd" lt 1,\
"lmt_5sd.dat" u 1:2 t "LMT 5sd" lt 2,\
"results_nofilter.dat" u 1:2 t "No Filter" lt 3,\
"results_decitiontable_3sd.dat" u 1:2 t "DecisionTable"  lt 4,\
"j48_3sd.dat" u 1:2 t "j48"  lt 6,\
"profix_lmt_3sd.dat" u 1:2 t "LMT 3sd Pro fix"  lt 5

set xrange [1:63]
set output "plot1.jpg"
plot "lmt_3sd.dat" u 1:2 t "LMT 3sd" w l lt 1,\
"lmt_5sd.dat" u 1:2 t "LMT 5sd" w l lt 2,\
"results_nofilter.dat" u 1:2 t "No Filter" w l lt 3,\
"results_decitiontable_3sd.dat" u 1:2 t "DecisionTable"  w l lt 4,\
"j48_3sd.dat" u 1:2 t "j48"  w l lt 6,\
"profix_lmt_3sd.dat" u 1:2 t "LMT 3sd Pro fix"  w l lt 5,\
"aStar_profix_lmt_3sd.dat" u 1:2 t "A* LMT 3sd Pro fix"  w l lt 7