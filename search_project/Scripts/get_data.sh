#!/bin/bash

cd ..

for i  in $(seq 1 50); 
do 
	echo Data/Spring_2015_$i.txt
	echo >> Scripts/aStar_spring2015_data.log
	echo ================================== >> Scripts/aStar_spring2015_data.log
	echo Data/Spring_2015_$i.txt >> Scripts/aStar_spring2015_data.log
	echo ================================== >> Scripts/aStar_spring2015_data.log
	python search_project_aStar.py Data/Spring_2015_$i.txt >> Scripts/aStar_spring2015_data.log
done
