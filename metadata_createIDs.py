#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:19:27 2020

@author: codyotoole
"""


import pandas as pd

df = pd.read_csv('/Users/codyotoole/Desktop/Research_Data/GeneDrive_Data/MetaData/gd_full_meta_20002018_10auth.csv')

author = []

df.fillna(0, inplace=True)

for n in range(0, len(df)):
    #if df['Date'][n] == 2018:
        for i in range(1,73):
            if df['Author ' + str(i)][n] == 0:
                continue
            else:
                author.append(df['Author ' + str(i)][n])

author = (list(set([x.lower() for x in author])))

df1 = pd.DataFrame({'Author': author})

df1.insert(0, 'Id', range(1000, 1000 + len(df1)))

df1.to_csv('/Users/codyotoole/Desktop/Research_Data/GeneDrive_Data/MetaData/Authors_10.csv')

df = df.applymap(lambda s:s.lower() if type(s) == str else s)


papeauth = []
for n in range(0, len(df)):
    for t in range(0, len(df1)):
    #if df['Date'][n] == 2018:
        for i in range(1,12):
            if df['Author ' + str(i)][n] == df1['Author'][t]:
                papeauth.append((df['PaperID'][n], df1['Id'][t]))

df2 = pd.DataFrame({'papeauth':papeauth}) 

df2[['PaperID', 'AuthorID']] = pd.DataFrame(df2['papeauth'].tolist(), index = df2.index) 

df2.index.names = ['ID']           

df2.drop(['papeauth'], axis=1,inplace=True)  

df2.to_csv('/Users/codyotoole/Desktop/Research_Data/GeneDrive_Data/MetaData/PaperAuthors_10.csv')





