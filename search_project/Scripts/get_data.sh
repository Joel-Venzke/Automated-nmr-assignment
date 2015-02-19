#!/bin/bash

cd ..

for i  in $(seq 33 62); 
do 
	echo | tee -a Scripts/profix_no_filter.log
	echo ================================== | tee -a Scripts/profix_no_filter.log
	echo Data/Data_Fall_2014_$i.txt | tee -a Scripts/profix_no_filter.log
	echo ================================== | tee -a Scripts/profix_no_filter.log
	python search_project2.py Data/Data_Fall_2014_$i.txt | tee -a Scripts/profix_no_filter.log
done
