END=61;
for i in $(seq 1 $END); do
	echo ../Data/Data$i.txt;
	python pars.py ../Data/data50.txt $i > data$i.txt; 
done