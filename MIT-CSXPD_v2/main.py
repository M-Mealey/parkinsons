import numpy as np
from nqDataLoader import NqDataLoader
import sys, os, re, datetime

fileInTest = "MIT-CS1PD/data_MIT-CS1PD/1401114972.068_001_014.csv"
dir1 = "MIT-CS1PD"
dir2 = "MIT-CS2PD"

h1 = "MIT-CS1PD/GT_DataPD_MIT-CS1PD.csv"
h2 = "MIT-CS2PD/GT_DataPD_MIT-CS2PD.csv"

data = NqDataLoader()

info1 = np.genfromtxt(h1, dtype=None, delimiter=",", skip_header=1)
print info1[1][1]

data.loadDataFile(fileInTest)
badElems = data.sanityCheck()
print badElems," elements removed by sanity check\n"
print "row 1:"
print data.dataKeys[0]
print data.dataHT[0]
print data.dataTimeStart[0]
print data.dataTimeEnd[0]
print "row 10:"
print data.dataKeys[9]
print data.dataHT[9]
print data.dataTimeStart[9]
print data.dataTimeEnd[9]
