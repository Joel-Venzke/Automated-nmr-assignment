#!/bin/bash

cd ..
echo | tee -a Scripts/profix_lmt_3sd.log
echo ================================== | tee -a Scripts/profix_lmt_3sd.log
echo Data/Data_Fall_2014_62.txt | tee -a Scripts/profix_lmt_3sd.log
echo ================================== | tee -a Scripts/profix_lmt_3sd.log
python search_project1.py Data/Data_Fall_2014_62.txt | tee -a Scripts/profix_lmt_3sd.log