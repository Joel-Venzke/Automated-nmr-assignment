#!/bin/bash

cd ..

for i  in $(seq 36 70); 
do 
	echo Data/Spring_2015_$i.txt
	echo >> Scripts/spring2015_data_missing.log
	echo ================================== >> Scripts/spring2015_data_missing.log
	echo Data/Spring_2015_$i.txt >> Scripts/spring2015_data_missing.log
	echo ================================== >> Scripts/spring2015_data_missing.log
	python search_project_aStar.py Data/Spring_2015_$i.txt >> Scripts/spring2015_data_missing.log
done
