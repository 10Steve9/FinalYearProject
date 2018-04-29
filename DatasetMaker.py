# -*- coding: utf-8 -*-\
"""
Created on Sun Feb 18 20:04:03 2018

@author: Stephen
"""

import pandas as pd
import numpy
import glob
from time import time

start = time()
path =r'C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\Datasets\\UnmarkedData\\Data4.3'

filenames = glob.glob(path + "/*.txt")
#filenames = os.listdir(path)
list_ = []
for file_ in filenames:
    df = pd.read_csv(file_,
                 delim_whitespace=True, 
                 usecols=[0, 2, 3, 4, 5, 6, 7, 9, 10],
                 names=['siteId','Date','Time','Count','Direction','vehicleClass','Speed','Length','classScheme'],
                 parse_dates=[['Date', 'Time']])
    list_.append(df)
frame = pd.concat(list_)
#print(frame.shape)
#print(frame.describe())


#print(frame.describe())
#print((frame == 0).sum())
frame = frame.replace(0, numpy.NaN)
frame.dropna(inplace=True)
# summarize the number of rows and columns in the dataset
#print(frame.shape)
#print(frame.describe())
frame.to_csv("C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\FinalData43.csv", index=False, header=True)
end = time()
print('Elapsed time: {}'.format(end-start))