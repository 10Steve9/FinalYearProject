# -*- coding: utf-8 -*-\
"""
Created on Sun Feb 18 20:04:03 2018

@author: Stephen
"""

import pandas as pd
import glob

path =r'SetUpThePathHere'
filenames = glob.glob(path + "/*.txt")

#iterating through all files in a repository, analysing all files that end in .txt.

list_ = []
for file_ in filenames:
    df = pd.read_csv(file_,
                 delim_whitespace=True, 
                 usecols=[0, 2, 3, 4, 5, 6, 7, 9, 10],
                 names=['siteId','Date','Time','Count','Direction','vehicleClass','Speed','Length','classScheme'],
                 parse_dates=[['Date', 'Time']])
    list_.append(df)
frame = pd.concat(list_)

#Creating a pandas df that will be the required data. You select the features/ columns by the usecols function. 
#Creating a file out of all the files being analyised. 

frame.to_csv("SetUpThePathHereForTheEndFile", index=False, header=True)

#End result for me was a csv file with over 1.5 million rows. 
