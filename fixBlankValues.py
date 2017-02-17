# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:23:37 2017

@author: justinlboyer
"""

from loadData import sht1, shtNoNan
from vectorSubsets import yesNo

# create a function to replace any text with 1 and NA with 0
def fixValuesAnyWord(df,variable):
    df[variable] = df[variable].replace('\w',1, regex=True)
    df[variable] = df[variable].fillna(0)
    return;
    

# function that replaces yes with 1 and NA and no with 0
def fixValuesYesNo(df,variable):
    df[variable] = df[variable].replace('[Y|y]es',1, regex=True)
    df[variable] = df[variable].replace('^(?![y|Y]es).*',0, regex=True)
    df[variable] = df[variable].fillna(0)
    return;
 