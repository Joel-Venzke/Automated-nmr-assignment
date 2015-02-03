#!/bin/bash

cd ..

for i  in $(seq 43 55); 
do 
	echo | tee -a Scripts/lmt_3sd.log
	echo ================================== | tee -a Scripts/lmt_3sd.log
	echo Data/Data_Fall_2014_$i.txt | tee -a Scripts/lmt_3sd.log
	echo ================================== | tee -a Scripts/lmt_3sd.log
	python search_project.py Data/Data_Fall_2014_$i.txt | tee -a Scripts/lmt_3sd.log
done
