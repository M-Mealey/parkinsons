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
    rall = []

    def __init__(self, pInfo, prefix): 
        # creates a person object
        # takes pInfo (patient info) as argument. This is a vector with the MIT patient information that is in their file. Should be in same order.
        # prefix = name of folder that holds patient files
        # should be a 1 row np array, formatted as follows:
        # array as follows:
        # col 0    col 1    col 2    col 3    col 4    col 5    col 6        col 7    col 8
        # pID      gt       updrs108 afTap    sTap     nqScore  typingSpeed  file_1   file_2
        self.pID=pInfo[0]
        self.gt=pInfo[1]
        self.updrs108=pInfo[2]
        self.afTap=pInfo[3]
        self.sTap=pInfo[4]
        self.nqScore=pInfo[5]
        self.typingSpeed=pInfo[6]
        self.file_1 = prefix + pInfo[7]
        self.r1 = self.analyzeData(self.file_1)
        
        if len(pInfo)>8 : # the second group of people only have 1 file
            self.file_2 = prefix + pInfo[8]
            self.r2 = self.analyzeData(self.file_2)
        
        self.rall=self.r1+self.r2

        # list of predictions
        self.pred = []
        self.avg=-1

        print self.pID, " loaded"





    def analyzeData(self, file):
        result = []
        data = NqDataLoader()
        data.loadDataFile(file)
        window = []
        num_windows =int( (data.dataTimeEnd[len(data.dataTimeEnd)-1] //90)+1)
        i=0
        for w_num in range(0,num_windows):
            while i<len(data.dataTimeEnd) and data.dataTimeEnd[i]< w_num*90+90 :
                window.append( [data.dataKeys[i], data.dataHT[i], data.dataFT[i], data.dataTimeStart[i], data.dataTimeEnd[i] ])
                i=i+1
            if len(window)>=30: #make sure there's enough data
                result.append(self.analyzeWindow(window)) #create stat vector, add it to list
            window=[] #reset the list
        return result


    def analyzeWindow(self, window):
        # window is a 2d array, each row has key, HT, FT, time start, time end
        win=np.array(window)
        hts = win[:,1]
        hts = hts.astype(np.float)
        v0 = self.num_outliers(hts)/len(hts)
        v1 = (np.percentile(hts,50)-np.percentile(hts,25))/(np.percentile(hts,75)-np.percentile(hts,25))
        v2 = win[1][3].astype(np.float)-win[0][4].astype(np.float)
        if v2<0:
            v2=0
        hist =  np.histogram(hts, bins=[0, 0.125, 0.25, 0.375, 0.5])[0]
        return [v0,v1,v2,hist[0],hist[1],hist[2],hist[3]]

    def num_outliers(self, data):
        # https://gist.github.com/vishalkuo/f4aec300cf6252ed28d3
        # I will use the standard definition of an outlier, a value < q1 - 1.5IQR or > q3 + 1.5IQR
        q3 = np.percentile(data,75)
        q1 = np.percentile(data,25)
        iqr = (q3-q1)* (1.5) #iqr is actually 1.5 * the iqr
        uf = q3+iqr # upper fence
        lf = q1-iqr # lower fence
        outliers = 0
        for i in data.tolist():
            if i>uf or i<lf:
                outliers += 1
        return outliers

    def get_vecs(self):
        print self.rall
        return self.rall






