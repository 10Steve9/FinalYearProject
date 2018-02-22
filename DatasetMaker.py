# -*- coding: utf-8 -*-\
"""
Created on Sun Feb 18 20:04:03 2018

@author: Stephen
"""

import pandas as pd
import glob

path =r'C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\Datasets\\UnmarkedData\\TestData'
filenames = glob.glob(path + "/*.txt")

list_ = []
for file_ in filenames:
    df = pd.read_csv(file_,
                 delim_whitespace=True, 
                 usecols=[0, 2, 3, 4, 5, 6, 7, 9, 10],
                 names=['siteId','Date','Time','Count','Direction','vehicleClass','Speed','Length','classScheme'],
                 parse_dates=[['Date', 'Time']])
    list_.append(df)
frame = pd.concat(list_)

frame.to_csv("C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\0000Dataset.csv", index=False, header=True)
