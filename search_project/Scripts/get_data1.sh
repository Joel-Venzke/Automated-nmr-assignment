#!/bin/bash

cd ..

for i  in $(seq 50 62); 
do 
	echo | tee -a Scripts/profix_j48_3sd.log
	echo ================================== | tee -a Scripts/profix_j48_3sd.log
	echo Data/Data_Fall_2014_$i.txt | tee -a Scripts/profix_j48_3sd.log
	echo ================================== | tee -a Scripts/profix_j48_3sd.log
	python search_project1.py Data/Data_Fall_2014_$i.txt | tee -a Scripts/profix_j48_3sd.log
done
