import pandas as pd
import numpy as np
import tkinter as tk


path = "C:\Users\Liron\Desktop"

def classifier(record):
    target = "yes"
    return target

def classify(path):
    path_test=path + "\\test.csv"
    df_test = pd.read_csv(path_test)
    i = 1
    for record in df_test.iterrows():
        target = classifier(record)
        writetofile(path, i, target)
        print i
        i += 1

    return

def writetofile(path, i, target):
    path_output = path + "\\output.txt"
    with open(path_output, "a") as f:
        f.write(str(i) + " " + target + "\n")
    return


classify(path)


