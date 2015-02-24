set term jpeg
set datafile missing "?"
set log y
set key top left 
set key below box linestyle -1
set grid xtics ytics
set title "Machine Learning Models"
set ylabel "Nodes Generated"
set format y "$10^%01T$" #%3.0e"
set xlabel "Number of Amino Acids"
set xrange [1:63]
set output "ProFix_full.jpg"
plot "profix_no_filter.dat" u 1:2 t "No Filter" lt 3 w l,\
"profix_decisiontable_3sd.dat" u 1:2 t "Decisiontable" lt 2 w l,\
"profix_j48_3sd.dat" u 1:2 t "j48"  lt 6 w l,\
"profix_lmt_3sd.dat" u 1:2 t "LMT" lt 1 w l
#"aStar_profix_lmt_3sd.dat" u 1:2 t "A* LMT 3sd Pro fix" lt 7
#"results_decitiontable_3sd.dat" u 1:2 t "DecisionTable"  lt 4,\
#"lmt_3sd.dat" u 1:2 t "LMT 3sd" w l lt 5,\
#"lmt_5sd.dat" u 1:2 t "LMT 5sd" w l lt 2,\
#"results_nofilter.dat" u 1:2 t "No Filter" w l lt 3,\
#"results_decitiontable_3sd.dat" u 1:2 t "DecisionTable"  w l lt 4,\
#"j48_3sd.dat" u 1:2 t "j48"  w l lt 6,\
#"profix_lmt_3sd.dat" u 1:2 t "LMT 3sd Pro fix"  w l lt 1,\
#"aStar_profix_lmt_3sd.dat" u 1:2 t "A* LMT 3sd Pro fix"  w l lt 7

set output "pro_compare.jpg"
set title "Effect of Proline Identification"
set key below right box linestyle -1
plot "results_nofilter.dat" u 1:2 t "No Filter" w l lt 4,\
"profix_no_filter.dat" u 1:2 t "Proline Check No Filter" lt 3 w l,\
"lmt_3sd.dat" u 1:2 t "LMT" w l lt 2,\
"profix_lmt_3sd.dat" u 1:2 t "Proline Check LMT" lt 1 w l
