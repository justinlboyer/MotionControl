# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:12:07 2017

@author: justinlboyer
"""

# this script normalizes opus -- It takes the opus score on the tasks that respondents use their prosthesis for and divides it by the total number of tasks the respondent uses the prosthesis for
#
# Inputs
# 
# df = data frame
# variable = column name of score to be nomalized
# columnSumTasks = the column name of the summed tasks
# newColumnNameKey = The new name for the column that will be created


def normalizeOp(df, variable, columnSumTasks, newColumnNameKey):
    df[newColumnNameKey] = df[variable]/df[columnSumTasks]
    return