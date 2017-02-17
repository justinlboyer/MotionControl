# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 10:42:07 2017

@author: justinlboyer
"""

from vectorSubsets import yesNo, taskFull
import numpy as np
# this script computes opus weighted on whether or not the respondent uses their prosthesis for the task
# yes = 1
# no = 0
#
# Inputs
#
# df = data frame
# start = where to start subsetting the tasks, for opus start=0
# end = where to stop subsetting the task, fro opus end=20
# newColumnNameKey = new column name

def useProsthesisScore(df, start, end, newColumnNameKey):
    dt = np.dot(df[taskFull[start:end]],df[yesNo[start:end]].transpose())
    df[newColumnNameKey] = np.diag(dt)
    return
