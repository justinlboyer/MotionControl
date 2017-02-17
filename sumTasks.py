# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 10:56:43 2017

@author: justinlboyer
"""

# this script counts the number of tasks the respondent uses their prosthesis for
# and adds a column numberTasksUseProsthesis
#
# Inputs
# df = data frame
# newcolumnkey = a string specifying the name of the newcolumn
# start = where to start subsetting yesN0
# end = where to stop subsetting yesNo

from vectorSubsets import yesNo
def sumTasks(df, newcolumnkey, start, end):
    df[newcolumnkey] = df[yesNo[start:end]].sum(axis=1)