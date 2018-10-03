import numpy as np
from nqDataLoader import NqDataLoader
import sys, os, re, datetime
from person import Person
from sklearn.svm import SVR
import random

fileInTest = "MIT-CS1PD/data_MIT-CS1PD/1401114972.068_001_014.csv"
dir1 = "MIT-CS1PD/data_MIT-CS1PD/"
dir2 = "MIT-CS2PD/data_MIT-CS2PD/"

h1 = "MIT-CS1PD/GT_DataPD_MIT-CS1PD.csv"
h2 = "MIT-CS2PD/GT_DataPD_MIT-CS2PD.csv"

data = NqDataLoader()

info1 = np.genfromtxt(h1, dtype=None, delimiter=",", skip_header=1)
info2 = np.genfromtxt(h2, dtype=None, delimiter=",", skip_header=1)

group1=[]
for i in range(0,info1.shape[0]):
    group1.append(Person(info1[i],dir1))

group2=[]
for i in range(0,info2.shape[0]):
    group2.append(Person(info2[i],dir2))

# sample size
ss = 5 

vectors = []
scores = []
models=[]

#creates 200 models
for k in range(0,200)
    # gets the vectors and target values
    for i in range(0,ss):
        person = group1[random.randrange(0,len(group1))]
        scores.append(person.updrs108) #need to check if that's the target we want
        vec = random.randrange(0,len(person.rall))
        vectors.append(person.rall[vec])

    m = SVR(C=0.094, epsilon=0.052,verbose=True)
    m.fit(vectors,scores)
    models.append(m)


