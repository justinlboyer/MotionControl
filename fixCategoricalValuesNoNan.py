# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:45:56 2017

@author: justinlboyer
"""

import numpy as np
#from loadData import shtNoNan
#from vectorSubsets import opus, importance, isVector

# this script replaces all categorical values with numerical ones
#
# ~~~~ Coding is ~~~~~~
# Cannot Perform = 0
# Choose Not To Perform = 1
# Very Difficult = 2
# Slightly Difficult = 3
# Easy = 4
# anythingelse = nan
#  ~~~~~~~~~~~`
# Not Important = 0
# Moderately Important = 1
# Very Important = 2
#   ~~~~~~~~~~~
# Strongly Disagree = 0
# Disagree = 1
# Agree = 2
# Strongly Agree = 3


def fixValuesCategoricalNoNaN(df,variable):
    df[variable] = df[variable].replace("Cannot Perform", 0)
    df[variable] = df[variable].replace("Choose Not to Perform", 1)
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
    df[variable] = df[variable].replace("^[a-zA-Z]\s*", 0, regex=True)
    df[variable] = df[variable].replace("I'm bald - I don't have hair", 0)
    df[variable] = df[variable].replace("^I.*", 0, regex=True)
    return
    
#def fixValuesCategoricalNoNaN(df,variable):
#    df[variable] = df[variable].replace("Cannot Perform", 0)
#    df[variable] = df[variable].replace("Choose Not to Perform", 1)
#    df[variable] = df[variable].replace("Very Difficult", 2)
#    df[variable] = df[variable].replace("Slightly Difficult", 3)
#    df[variable] = df[variable].replace("Easy", 4)
#    df[variable] = df[variable].replace("Not Important", 0)
#    df[variable] = df[variable].replace("Moderately Important", 1)
#    df[variable] = df[variable].replace("Very Important", 2)
#    df[variable] = df[variable].replace("Strongly Agree", 0)
#    df[variable] = df[variable].replace("Disagree", 1)
#    df[variable] = df[variable].replace("Agree", 2)
#    df[variable] = df[variable].replace("Strongly Agree", 3)
#    df[variable] = df[variable].replace("^[a-zA-Z]\s*", 0, regex=True)
#    df[variable] = df[variable].replace("I'm bald - I don't have hair", 0)
#    return
  
  
# fix all the agree/disagree/etc
#for i in isVector:
#    fixValuesCategoricalNoNaN(shtNoNan,i)