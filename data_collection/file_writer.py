#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 6 14:11:37 2018

@author: mfr
"""
# import dependencies 
from datetime import date 

# write data to file
def pd_to_csv():
	today = date.today()
	file_name = str(today) + ".csv"
	df.to_csv(file_name)