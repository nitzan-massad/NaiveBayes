import pandas as pd
import numpy as np
#import matplotlib as plt
dict  = {}



def readStructure (pathToStructureInfoFile):
    file = open(pathToStructureInfoFile,"r")
    for line in file:
     tmp = line.split(' ')
     dict[tmp [1]]=tmp [2]
    for robi in dict:
        print robi +" "+ dict [robi]
    return


df = pd.read_csv("C:\Users\\nitzan\Desktop\\train.csv")

#print(df.head(10))
#print(df['month'].str.lower().value_counts())
#print(df.describe())

readStructure ("C:\Users\\nitzan\Desktop\\Structure.txt")