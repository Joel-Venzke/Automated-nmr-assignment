#!/bin/bash

cd ..

for i  in $(seq 1 62); 
do 
	echo | tee -a Scripts/test2.log
	echo ================================== | tee -a Scripts/test2.log
	echo Data/Data_Fall_2014_$i.txt | tee -a Scripts/test2.log
	echo ================================== | tee -a Scripts/test2.log
	python search_project_aStar.py Data/Data_Fall_2014_$i.txt | tee -a Scripts/test2.log
done
