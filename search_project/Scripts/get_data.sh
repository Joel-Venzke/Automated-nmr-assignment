#!/bin/bash

cd ..

for i  in $(seq 1 33); 
do 
	echo | tee -a Scripts/run.log
	echo ================================== | tee -a Scripts/run.log
	echo Data/Data_Fall_2014_$i.txt | tee -a Scripts/run.log
	echo ================================== | tee -a Scripts/run.log
	python search_project.py Data/Data_Fall_2014_$i.txt | tee -a Scripts/run.log
done