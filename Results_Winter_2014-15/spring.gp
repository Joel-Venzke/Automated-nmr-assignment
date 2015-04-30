set term pdf
set output "tmp.pdf"
set log y
set nokey
plot  'spring_2k15_no_aStar.dat' w l, 'spring2k15_missing.dat' w l