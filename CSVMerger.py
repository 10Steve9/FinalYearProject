# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:51:04 2018

@author: Stephen
"""

import shutil
import glob

#import csv files from folder
path = r'C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\CSVData'
allFiles = glob.glob(path + "/*.csv")
with open('FinalisedData.csv', 'wb') as outfile:
    for i, fname in enumerate(allFiles):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()  # Throw away header on all but first file
            # Block copy rest of file from input to output without parsing
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")