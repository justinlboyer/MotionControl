# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:40:56 2017

@author: justinlboyer
"""

# this script calculates total raw score and the weighted score
#from fixCategoricalValues import sht1
import numpy as np
from vectorSubsets import importanceFull, taskFull
#from fixValuesCategoricalNoNaN import fixValuesCategoricalNoNaN


def taskScored(df):
    df["taskScore"] = df[taskFull].sum(axis=1)
    return

def weightedTotalScore(df):
    dt = np.dot(df[taskFull],df[importanceFull].transpose())
    df["weightedTaskScore"] = np.diag(dt)
    return