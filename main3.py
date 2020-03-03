import numpy as np
from nqDataLoader import NqDataLoader
import sys, os, re, datetime
from person import Person
from sklearn.svm import SVR
from sklearn.preprocessing import normalize
import random

fileInTest = "MIT-CS1PD/data_MIT-CS1PD/1401114972.068_001_014.csv"
dir1 = "MIT-CS1PD/data_MIT-CS1PD/"
dir2 = "MIT-CS2PD/data_MIT-CS2PD/"

h1 = "MIT-CS1PD/GT_DataPD_MIT-CS1PD.csv"
h2 = "MIT-CS2PD/GT_DataPD_MIT-CS2PD.csv"

data = NqDataLoader()

info1 = np.genfromtxt(h1, dtype=None, delimiter=",", skip_header=1)
info2 = np.genfromtxt(h2, dtype=None, delimiter=",", skip_header=1)

######## normalize the UPDRS scores#########
# get lists for each group
updrs1 = np.genfromtxt(h1, dtype=None, delimiter=",", skip_header=1, usecols=(2))
updrs2 = np.genfromtxt(h2, dtype=None, delimiter=",", skip_header=1, usecols=(2))
#print updrs1
#print updrs2
#combine lists & normalize
updrs = updrs1.tolist() + updrs2.tolist()
updrs = np.array(updrs).reshape(1,-1)
updrs = normalize(updrs, norm='max')

# update values with normalized values in raw info array
for i in range(0,info1.shape[0]):
#    print "before: ",info1[i][2]
#    print updrs[0][i]
    info1[i][2] = updrs[0][i]
#    print "after: ",info1[i][2]

for i in range(0,info2.shape[0]):
#    print "before: ",info2[i][2]
    info2[i][2] = updrs[0][i+info1.shape[0]]
#    print "after: ",info2[i][2]



####    creating "person" object for each person    ####    
group1=[]
for i in range(0,info1.shape[0]):
    group1.append(Person(info1[i],dir1))

group2=[]
for i in range(0,info2.shape[0]):
    group2.append(Person(info2[i],dir2))






# sample size
ss = 20

random.seed(6)

vectors = []
scores = []
models=[]

#creates 200 models
for k in range(0,200):
    # gets the vectors and target values
    for i in range(0,ss):
        person = group1[random.randrange(0,len(group1))]
        scores.append(person.updrs108) #need to check if that's the target we want
        vec = random.randrange(0,len(person.rall))
#        print person.rall[vec]
        vectors.append(person.rall[vec])

    m = SVR(kernel='linear', C=0.094, epsilon=0.052,verbose=False)
    m.fit(vectors,scores)
    models.append(m)
    vectors=[]
    scores=[]

# now predict using each model, median of predictions = score for vector, avg of all vector predictions = score for person
for person in group2:
    for vec in person.rall:
        preds = []
        for m in models:
            preds.append(m.predict([vec]))
        med = np.median(preds)
        person.pred.append(med)
    person.avg = sum(person.pred)/len(person.pred)
    print person.pID,"\t",person.avg, "\t",person.updrs108


