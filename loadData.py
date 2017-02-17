# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:03:33 2017

@author: justinlboyer
"""
import pandas as pd
#import numpy
from vectorSubsets import namesSht1, namesSht2

# load data
originalSht1 = pd.read_csv("./Sheet_1_140217.csv", skiprows=1, index_col=False, names=namesSht1, parse_dates=['StartDate','EndDate'])
sht1NoDup = originalSht1.copy()
originalSht2 = pd.read_csv("./Sheet_2_140217.csv", skiprows=1, index_col=False, names=namesSht2, parse_dates=['StartDate','EndDate'])
sht2NoDup = originalSht2.copy()
#sht1_num = pd.read_csv("./Sheet_1_numeric.csv", skiprows=1, index_col=False, names=namesSht1)
#sht2_num = pd.read_csv("./Sheet_2_numeric.csv", skiprows=1, index_col=False, names=namesSht2)

# remove duplicates
# find duplicate rows
emailDup = originalSht2.EmailAddress[originalSht2.EmailAddress.duplicated(keep='first')].dropna(axis=0)
for i in emailDup:
    sht1NoDup = sht1NoDup[sht2NoDup.EmailAddress != i]
    sht2NoDup = sht2NoDup[sht2NoDup.EmailAddress != i]
# remove duplicate rows
sht1NoDup = sht1NoDup[~sht2NoDup.EmailAddress.isnull()]
sht2NoDup = sht2NoDup[~sht2NoDup.EmailAddress.isnull()]
# verify no duplicates
numDup = len(sht2NoDup.EmailAddress[sht2NoDup.EmailAddress.duplicated()])
print("There are %d duplicates" % numDup )
    
sht1 = sht1NoDup.copy()
shtNoNan = sht1NoDup.copy()
sht2 = sht2NoDup.copy() 


         