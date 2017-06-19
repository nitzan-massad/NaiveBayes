import pandas as pd
import numpy as np
import anaconda_mode as md
#import tkinter as tk
m_dictStructure = {}
m_bins =10
df =  file
mainDic ={}

def buildModel (path, bins):

    m_bins = bins
    readStructure(path)
    fillMissingValuesAndDiscretization()
    buildClassifier()
    return

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
            df[x] =binning(df[x])
        else:
            df[x].fillna(df.mode()[x][0], inplace=True) # find the most comman value in month
    #print(df.apply(lambda x: sum(x.isnull()), axis=0)) # print the missing values in eche colmn
    return

def binning(col ):
    labels = None
    minval = col.min()
    maxval = col.max()
    interval = (maxval-minval)*1.0/m_bins
    #print "maxval: ",maxval
    #print "minval: ",minval
    #print "interval: ",interval
    cut_points =[]
    for x in range(0, m_bins+1):
        cut_points.append((minval+ x*interval))
    break_points = cut_points
    if not labels:
        labels = range(len(cut_points)-1)
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin

def buildClassifier () :

    for attribut in m_dictStructure:


        for


   # print(df.loc[(df["education"] == "secondary") & (df["marital"] == "married"),["education", "marital"]])


    return




df = pd.read_csv("C:\Users\\nitzan\Desktop\\train.csv")
buildModel("C:\Users\\nitzan\Desktop\\Structure.txt" , m_bins)
