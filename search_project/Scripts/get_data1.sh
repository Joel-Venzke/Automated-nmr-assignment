#!/bin/bash

cd ..

for i  in $(seq 61 62); 
do 
	echo | tee -a Scripts/aStar_profix_lmt_3sd.log
	echo ================================== | tee -a Scripts/aStar_profix_lmt_3sd.log
	echo Data/Data_Fall_2014_$i.txt | tee -a Scripts/aStar_profix_lmt_3sd.log
	echo ================================== | tee -a Scripts/aStar_profix_lmt_3sd.log
	python search_project1.py Data/Data_Fall_2014_$i.txt | tee -a Scripts/aStar_profix_lmt_3sd.log
done
