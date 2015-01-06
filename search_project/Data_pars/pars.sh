END=61;
for i in $(seq 1 $END); do
	echo ../Data/Data_Fall_2014_$i.txt;
	python pars.py ../Data/Data_Fall_2014_fix.txt $i > ../Data/Data_Fall_2014_$i.txt; 
done