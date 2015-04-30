#!/bin/bash

cd ..

for i  in $(seq 1 50); 
do 
	echo Data/Spring_2015_$i.txt
	echo | tee -a Scripts/spring_2k15_no_aStar.log
	echo ================================== | tee -a Scripts/spring_2k15_no_aStar.log
	echo Data/Spring_2015_$i.txt | tee -a Scripts/spring_2k15_no_aStar.log
	echo ================================== | tee -a Scripts/spring_2k15_no_aStar.log
	python search_project.py Data/Spring_2015_$i.txt | tee -a Scripts/spring_2k15_no_aStar.log
done
