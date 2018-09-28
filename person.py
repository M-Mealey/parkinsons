import numpy as np
from nqDataLoader import NqDataLoader


class Person:
    pID=0
    gt=0
    updrs108=0
    afTap=0
    sTap=0
    nqScore=0
    typingSpeed=0
    file_1=""
    file_2=""
    # list of vectors that represent the results from each test
    r1 = []
    r2 = []

    def __init__(self, pInfo, prefix): 
        # creates a person object
        # takes pInfo (patient info) as argument. This is a vector with the MIT patient information that is in their file. Should be in same order.
        # prefix = name of folder that holds patient files
        # should be a 1 row np array, formatted as follows:
        # array as follows:
        # col 0    col 1    col 2    col 3    col 4    col 5    col 6        col 7    col 8
        # pID      gt       updrs108 afTap    sTap     nqScore  typingSpeed  file_1   file_2
        pID=pInfo[0]
        gt=pInfo[1]
        updrs108=pInfo[2]
        afTap=pInfo[3]
        sTap=pInfo[4]
        nqScore=pInfo[5]
        typingSpeed=pInfo[6]
        file_1 = prefix + pInfo[7]
        file_2 = prefix + pInfo[8]

        r1 = self.analyzeData(file_1)
        r2 = self.analyzeData(file_2)




    def analyzeData(self, file):
        data = NqDataLoader()
        data.loadDataFile(file)
        window = []
        w_num = 0
        i=0
        while data.dataTimeEnd[i]< w_num*90:
            window.append( [data.dataKeys[i], data.dataHT[i], data.dataFT[i], data.dataTimeStart[i], data.dataTimeEnd[i] ])
            i=i+1
        print window






