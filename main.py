import numpy as np
from nqDataLoader import NqDataLoader
import sys, os, re, datetime
from person import Person

fileInTest = "MIT-CS1PD/data_MIT-CS1PD/1401114972.068_001_014.csv"
dir1 = "MIT-CS1PD/data_MIT-CS1PD/"
dir2 = "MIT-CS2PD/data_MIT-CS2PD/"

h1 = "MIT-CS1PD/GT_DataPD_MIT-CS1PD.csv"
h2 = "MIT-CS2PD/GT_DataPD_MIT-CS2PD.csv"

data = NqDataLoader()

info1 = np.genfromtxt(h1, dtype=None, delimiter=",", skip_header=1)
print info1[1][1]

group1=[]
for i in range(0,info1.shape[0]):
    group1.append(Person(info1[i],dir1))





