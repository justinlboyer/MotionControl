# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:19:24 2017

@author: justinlboyer
"""
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#%matplotlib inline
from driverCleanData import cleanData
[sht, shtNan] = cleanData()