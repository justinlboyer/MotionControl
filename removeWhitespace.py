# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:06:21 2017

@author: justinlboyer
"""

# Fix funky values
def fixFunky(df,variable):
    df[variable] = df[variable].replace(u'\xa0', u' ')
    df[variable] = df[variable].replace('(Otto Bock)\sG.*', 'Otto BockGreifer', regex=True) # fix funky Otto Bock Greifer
    # string = string.replace(u'\xa0', u' ')
    return