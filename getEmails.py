# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 07:31:53 2017

@author: samij
"""

# this script retrieves a list of email addresses of respondendts who fit the stated criteria
import pandas as pd
# import data
from driverCleanData import cleanData
[sht1,_] = cleanData()
# import second sheet to get emails
from loadData import sht2
# join sht1 to sht2
fullDf = pd.merge(sht1, sht2, on='RespondentID')
# get similarity sum
foundSum = pd.read_csv('./foundSum.csv', names=["Index","Score"])
# remove bot data based on analysis in jupyter notebook (remove sums of 228, 230, 235)
nonBot = foundSum[(foundSum['Score'] != 228) & (foundSum['Score'] != 230) & (foundSum['Score'] != 235)]
fullDf = fullDf.loc[nonBot.index]
# remove people who spent less than 20 min
fullDf['timeDiff'] = fullDf.EndDate_x - fullDf.StartDate_x
fullDf['timeDiff'] = fullDf['timeDiff'].astype('timedelta64[m]')
legitTimeDiff = fullDf.timeDiff[fullDf['timeDiff'] >= 20 ]
fullDf = fullDf.loc[legitTimeDiff.index]

print("The minimum time taken on the survey of this set is {0}".format(fullDf.timeDiff.min()))
# write csv of emails if time Diff is greater than or equal to 15 min
if fullDf['timeDiff'].min()>=15:
    fullDf.EmailAddress_y.to_csv('EmailList_NonBot_Spent15minOrMore.csv')


# get emails of people who have a secondary device
emailsSecD = fullDf.EmailAddress_y[fullDf['SecondaryDevice'] != 'None']
emailsSecD.to_csv('EmailList_PrimaryAndSecondary.csv')
