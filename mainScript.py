import pandas as pd
import numpy as np
import anaconda_mode as md
#import tkinter as tk
m_dictStructure = {}
m_bins =0



def readStructure (pathToStructureInfoFile):
    file = open(pathToStructureInfoFile,"r")
    for line in file:
        tmp = line.split(' ')
        if (tmp [2][len(tmp[2])-1]):
            tmp[2]= tmp [2][:-1]
        if ( tmp[2] != 'NUMERIC'):
            tmp[2]= tmp [2][:-1]
            tmp[2]= tmp [2][1:]
            tmp[2] = tmp[2].split(',')

        m_dictStructure[tmp [1]]= tmp [2]

    return



def fillMissingValuesAndDiscretization():
    tmp = 'NUMERIC'

    for x in m_dictStructure:
        if(m_dictStructure[x]== 'NUMERIC'):
            df[x].fillna(df[x].mean(), inplace=True)
            df[x] =binning(df["x"])
            print df[x]
        else:
            df[x].fillna(df.mode()[x][0], inplace=True) # find the most comman value in month



    #print(df.apply(lambda x: sum(x.isnull()), axis=0)) # print the missing values in eche colmn

    return

def binning(col, cut_points ):
    labels = None
    minval = col.min()
    maxval = col.max()
    cut_points = maxval-minval
    break_points = [minval] + cut_points + [maxval]
    if not labels:
        labels = range(len(cut_points)+1)
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin



df = pd.read_csv("C:\Users\\nitzan\Desktop\\train.csv")

#df['education'].fillna('No', inplace=True)
#df['education'].fillna(df['education'].mean(), inplace=True)

df1 = pd.DataFrame({'A': [1, 2, 1, 2, 1, 2, 3, 1] , 'B': [1, 2, 1, 2, 1, 2, 3, 2]})
#print (df1.mode()['B'][0])

#print( df.mode()['month'][0]) # find the most comman value in month

#print(df.apply(lambda x: sum(x.isnull()), axis=0)) # print the missing values in eche colmn

readStructure ("C:\Users\\nitzan\Desktop\\Structure.txt")
fillMissingValuesAndDiscretization()