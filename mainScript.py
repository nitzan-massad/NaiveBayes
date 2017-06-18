import pandas as pd
import numpy as np
#import matplotlib as plt
dictStructure  = {}



def readStructure (pathToStructureInfoFile):
    file = open(pathToStructureInfoFile,"r")
    for line in file:
     tmp = line.split(' ')
     dictStructure[tmp [1]]=tmp [2]
    #for robi in dictStructure:
     #   print robi +" " + dictStructure [robi]
    return


df = pd.read_csv("C:\Users\\nitzan\Desktop\\train.csv")

#print(df.head(10))
#print(df['month'].str.lower().value_counts())
#print(df.describe())

readStructure ("C:\Users\\nitzan\Desktop\\Structure.txt")