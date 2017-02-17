# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:50:50 2017

@author: samij
"""

# this script find all the rows that have p percent of items in common
#
# Inputs
# df = data frame
# p = percentage of similar data
#
# Outputs
# fraudIndex = the index of the data suspected to be fraudlent

def compareRows(df, p):
    # initizalize botDf
    columns = df.columns
    numR = df.shape[0]
    numC = df.shape[1]
    index = list(range(0,numR))
    boolDf = pd.DataFrame(index=index, columns=columns)
    boolDf['Sum']= np.nan
    findDf = pd.DataFrame(index=index, columns=columns)
    foundSum = pd.Series(index=index)
    foundSum.fillna(0, inplace=True)
# add new boolean column that tells us False not a duplicate, or True a duplicate
 #   dupColumns = columns[10:numC]
#    df['is_duplicated'] = df.duplicated(dupColumns)
    for i in range(0,numR):
        findDf['tempSum'] = np.nan
        comRow = df.loc[i,:]
        comRow = comRow.to_dict()
        comRow = {key: [value] for key, value in comRow.items()}
        findDf.loc[i+1:numR,:] = df.loc[i+1:numR,:].isin(comRow)
        findDf['tempSum'] = findDf.sum(axis=1)
        for j in range(i+1,numR):
            if findDf['tempSum'].iloc[j] > foundSum.iloc[j]:
                foundSum.iloc[j] = findDf['tempSum'].iloc[j]
                foundSum.iloc[i] = findDf['tempSum'].max()
        if i%10==0:
            print("Iteration {0}, Max sum {1}, row {2}".format(i, foundSum.loc[i+1:numR].max(), foundSum.loc[i+1:numR].idxmax()))
#        if foundSum.any() >= p*numC:
#            boolDf.loc[i+1:numR,:] = findDf[foundSum>=p*numC].loc[i+1:numR,:]
#            boolDf.loc[i,:] = findDf.loc[i,:]
#    fraudIndex = boolDf.dropna().index
        boolDf = boolDf[foundSum >= p*numC]
    return(boolDf, foundSum)
        
[t1,tix] = compareRows(sht,0.85)