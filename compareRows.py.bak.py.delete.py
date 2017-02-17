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
    boolDf['sum']= np.nan
    findDf = pd.DataFrame(index=index, columns=columns)
# add new boolean column that tells us False not a duplicate, or True a duplicate
 #   dupColumns = columns[10:numC]
#    df['is_duplicated'] = df.duplicated(dupColumns)
    for i in range(1,numR):
        findDf['sum'] = np.nan
        comRow = df.loc[i,:]
        comRow = comRow.to_dict()
        comRow = {key: [value] for key, value in comRow.items()}
        findDf.loc[i+1:,:] = df.loc[i+1:,:].isin(comRow)
        findDf['sum'] = findDf.sum(axis=1)
        if i%10==0:
            print("Iteration {0}, Max sum {1}, row {2}".format(i, findDf['sum'].loc[i+1:].max(), findDf['sum'].idxmax()))
        else:
            print("~")
        boolDf.loc[i+1:,:] = findDf[findDf['sum']>=p*numC].loc[i+1:,:]
    fraudIndex = boolDf.dropna().index
    return(boolDf, fraudIndex)
        
