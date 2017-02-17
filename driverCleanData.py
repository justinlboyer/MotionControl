# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:00:40 2017

@author: justinlboyer
"""
# This driver runs the necessary scripts to clean the data returns two df's and then optionally writes two csvs of the cleaned data
def cleanData(writecsv=False):
    "Function cleans and returns two data sets sht1 contains NaN, shtNoNan does not contain NaN.  The function also writes a two csvs if writecsv=True"
    # load the packages I typically use
    #import pandas as pd
    #import numpy as np
    #from scipy import stats
    
    # load the data
    from loadData import shtNoNan, sht1, sht2

    # fix binary and blanks
    from fixBlankValues import fixValuesAnyWord, fixValuesYesNo
    from vectorSubsets import yesNo
    # fix binary for TD
    from vectorSubsets import TDs
    for i in TDs:
        fixValuesAnyWord(sht1,i)
        fixValuesAnyWord(shtNoNan,i)    
    # loop over all instances of yesNo
    for i in yesNo:
        fixValuesYesNo(sht1,i)
        fixValuesYesNo(shtNoNan,i)
        
    # fix funky white spaces
    from removeWhitespace import fixFunky
    fixFunky(sht1,'PrimaryTerminalDevice')
    fixFunky(shtNoNan,'PrimaryTerminalDevice')
    # fix categorical values -- Not using because we don't have enough data, maybe once data >500 could include
    #from fixCategoricalValues import sht1
    
    # fix categorical but remove NaN
    from fixCategoricalValuesNoNan import fixValuesCategoricalNoNaN
    from fixCategoricalValues import fixValuesCategorical
    from vectorSubsets import opus, importanceOpus, importanceFull, taskFull
    # code opus values
    for i in opus:
        fixValuesCategoricalNoNaN(shtNoNan,i)
        fixValuesCategorical(sht1,i)
    # code importance for opus
    for i in importanceOpus:
        fixValuesCategoricalNoNaN(shtNoNan,i)
        fixValuesCategorical(sht1,i)
        # code task values
    for i in taskFull:
        fixValuesCategoricalNoNaN(shtNoNan,i)
        fixValuesCategorical(sht1,i)
        # code importance values
    for i in importanceFull:
        fixValuesCategoricalNoNaN(shtNoNan,i)
        fixValuesCategorical(sht1,i)
        
    # added opusScore and weighted opus score
    from opusScore import opusScored, weightedOpusScore
    opusScored(sht1)
    opusScored(shtNoNan)
    weightedOpusScore(sht1)
    weightedOpusScore(shtNoNan)
    
    # add fullScore and weighted full score
    from totalScore import taskScored, weightedTotalScore
    taskScored(shtNoNan)
    taskScored(sht1)
    weightedTotalScore(shtNoNan)
    weightedTotalScore(sht1)
        
    # add score conditioned on whether or not respondendents use their prosthesis
    from doYouUseProsOpus import useProsthesisScore
    from vectorSubsets import taskFull
    # add opus conditioned on use of prosthesis
    useProsthesisScore(shtNoNan, 0, 20,  'doYouUseProsthesisOpus')
    useProsthesisScore(sht1, 0, 20, 'doYouUseProsthesisOpus')
    # add full task conditioned onuse of prosthesis
    useProsthesisScore(shtNoNan, 0, 28, 'doYouUseProsthesisFull')
    useProsthesisScore(sht1, 0, 28, 'doYouUseProsthesisFull')
    # add taskFull - Opus conditioned on use of prosthesis
    task = taskFull[20:28]
    useProsthesisScore(shtNoNan, 20, 28, 'doYouUseProsthesisTask')     
    useProsthesisScore(sht1, 20, 28, 'doYouUseProsthesisTask')    
    
    # add sum of tasks completed
    from sumTasks import sumTasks
    # add sum of opus tasks completed
    sumTasks(shtNoNan, 'numberTasksUseProsthesisOpus', 0, 20)
    sumTasks(sht1, 'numberTasksUseProsthesisOpus', 0, 20)
    # add sum of all tasks completed
    sumTasks(shtNoNan, 'numberTasksUseProsthesisFull', 0, 28)
    sumTasks(sht1, 'numberTasksUseProsthesisFull', 0, 28)
    # add sum of AllTasks-OpusTasks completed
    sumTasks(shtNoNan, 'numberTasksUseProsthesisTask', 20, 28)
    sumTasks(sht1, 'numberTasksUseProsthesisTask', 20, 28)
    
    # add score which is normalized by dividing their score by the number of tasks they actually complete
    from normalizeScore import normalizeScore   
    # add normalizedOpus
    normalizeScore(shtNoNan, 'doYouUseProsthesisOpus', 'numberTasksUseProsthesisOpus', 'normalizedOpus')
    normalizeScore(sht1, 'doYouUseProsthesisOpus', 'numberTasksUseProsthesisOpus', 'normalizedOpus')
    # add normalizedFull
    normalizeScore(shtNoNan, 'doYouUseProsthesisFull', 'numberTasksUseProsthesisFull', 'normalizedFull')
    normalizeScore(sht1, 'doYouUseProsthesisFull', 'numberTasksUseProsthesisFull', 'normalizedFull') 
    # add normalize task
    normalizeScore(shtNoNan, 'doYouUseProsthesisTask', 'numberTasksUseProsthesisTask', 'normalizedTask') 
    normalizeScore(sht1, 'doYouUseProsthesisTask', 'numberTasksUseProsthesisTask', 'normalizedTask') 
    
    # reset indices
    shtNoNan = shtNoNan.reset_index(drop=True)
    sht1 = sht1.reset_index(drop=True)
    sht2 = sht2.reset_index(drop=True)
    

    
    # write to csvs if writecsv=True
    if writecsv==True:
        sht1.to_csv("sht1_CLEAN.csv")
        shtNoNan.to_csv("shtNoNan_CLEAN.csv")
    
    # returns cleaned data sets
    return [shtNoNan, sht1]

