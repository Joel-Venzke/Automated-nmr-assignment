END=99;
for i in $(seq 1 $END); do
	echo ../Data/Spring_2015_$i.txt;
	python pars.py ../Data/Spring_2014_100.txt $i > ../Data/Spring_2015_$i.txt; 
done