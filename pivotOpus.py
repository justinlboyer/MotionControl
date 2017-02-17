# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 04:03:39 2017

@author: justinlboyer
"""
from loadData import sht1NoDup
from vectorSubsets import opus, degreeOfPerformance
# this script creates new df that investigates correlation of values

# subset data
op = sht1NoDup[opus].copy()

# code any of the I... as Cannot Perform
def fixIDontNoNan(df,variable):
    df[variable] = df[variable].replace("I{1}.*","Cannot Perform", regex=True)
    return

for i in opus:
    fixIDontNoNan(op,i)

# loop over all values to create new df
# initialize df
op = op.dropna()
op = op.transpose()
observations = pd.pivot_table(op, index=opus, aggfunc='count', fill_value=0)
