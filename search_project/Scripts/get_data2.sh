#!/bin/bash

cd ..

for i  in $(seq 1 50); 
do 
	echo Data/Spring_2015_$i.txt
	echo | tee -a Scripts/lmt_spring2015_data.log
	echo ================================== | tee -a Scripts/lmt_spring2015_data.log
	echo Data/Spring_2015_$i.txt | tee -a Scripts/lmt_spring2015_data.log
	echo ================================== | tee -a Scripts/lmt_spring2015_data.log
	python search_project1.py Data/Spring_2015_$i.txt | tee -a Scripts/lmt_spring2015_data.log
done
