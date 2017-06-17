


import pandas as pd
import numpy as np
#import matplotlib as plt

df = pd.read_csv("C:\Users\nitzan\Desktop\train.csv")

print(df.head(10))
print("\n Summary of numeircal variables:")
print(df.describe())                                             # Get summary of numerical variables
print("\n Frequency Distribution of Property_Area attribute:")
print(df['Property_Area'].value_counts())                        # Frequency distribution for non-numerical attributes
print("\n Frequency Distribution of Credit_History attribute:")
print(df['Credit_History'].value_counts())



def readStructure (pathToStructureInfoFile):




    return
