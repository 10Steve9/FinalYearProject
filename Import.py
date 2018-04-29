# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:21:48 2018

@author: Stephen
"""

import pandas as pd
import glob
import MySQLdb

mydb = MySQLdb.connect(host='127.0.0.1:3306',
    user='root',
    passwd='root',
    db='fyp_data')
cursor = mydb.cursor()

path =r'C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\'
filenames = glob.glob(path + "/*.csv")

for file_ in filenames:
    csv_data = pd.read_csv(file_,'C:\\Users\\Stephen\\Desktop\\College Stuff\\Semester8\\FYP\\0000Dataset.csv')
for row in csv_data:
    cursor.execute('INSERT INTO testcsv(siteId,Date,Time,Count,Direction,vehicleClass,Speed,Length,classScheme)' \
          'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print("Done")
