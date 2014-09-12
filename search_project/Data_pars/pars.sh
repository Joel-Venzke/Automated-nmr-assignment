END=10;
for i in $(seq 1 $END); do
	echo ../Data/Data_Fall_2014_$i.txt;
	python pars.py ../Data/Data_Fall_2014.txt $i > ../Data/Data_Fall_2014_$i.txt; 
done