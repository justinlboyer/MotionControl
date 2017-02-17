# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:45:56 2017

@author: justinlboyer
"""

import numpy as np
#from loadData import sht1
#from vectorSubsets import opus, importance, yesNo, isVector

# this script replaces all categorical values with numerical ones
#
# ~~~~ Coding is ~~~~~~
# Cannot Perform = 0
# Choose Not To Perform = np.nan
# Very Difficult = 2
# Slightly Difficult = 3
# Easy = 4
# anythingelse = NA
#  ~~~~~~~~~~~`
# Not Important = 0
# Moderately Important = 1
# Very Important = 2
#   ~~~~~~~~~~~
# Strongly Disagree = 0
# Disagree = 1
# Agree = 2
# Strongly Agree = 3

def fixValuesCategorical(df,variable):
    df[variable] = df[variable].replace("Cannot Perform", 0)
    df[variable] = df[variable].replace("Choose Not to Perform", np.nan)
    df[variable] = df[variable].replace("Very Difficult", 2)
    df[variable] = df[variable].replace("Slightly Difficult", 3)
    df[variable] = df[variable].replace("Easy", 4)
    df[variable] = df[variable].replace("Not Important", 0)
    df[variable] = df[variable].replace("Moderately Important", 1)
    df[variable] = df[variable].replace("Very Important", 2)
    df[variable] = df[variable].replace("Strongly Agree", 0)
    df[variable] = df[variable].replace("Disagree", 1)
    df[variable] = df[variable].replace("Agree", 2)
    df[variable] = df[variable].replace("Strongly Agree", 3)
    df[variable] = df[variable].replace("^[a-zA-Z]\s*", np.nan, regex=True)
    df[variable] = df[variable].replace("I'm bald - I don't have hair", np.nan)
    return
 
# fix opus values   
#for i in opus:
#    fixValuesCategorical(sht1,i)
#    
## fix importance values
#for i in importance:
#    fixValuesCategorical(sht1,i)
#    
## fix all the agree/disagree/etc
#for i in isVector:
#    fixValuesCategorical(sht1,i)