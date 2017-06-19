import pandas as pd

class Classifier:

    def __init__(self):
        self.path = None

    def readStructure(self, pathToStructureInfoFile):
        file = open(pathToStructureInfoFile, "r")
        for line in file:
            tmp = line.split(' ')
            if tmp[2][len(tmp[2]) - 1]=='\n':
                tmp[2] = tmp[2][:-1]
            if (tmp[2] != 'NUMERIC'):
                tmp[2] = tmp[2][:-1]
                tmp[2] = tmp[2][1:]
                tmp[2] = tmp[2].split(',')

            self.m_dictStructure[tmp[1]] = tmp[2]

    def fillMissingValuesAndDiscretization(self , df):
        for x in self.m_dictStructure:
            if (self.m_dictStructure[x] == 'NUMERIC'):
                df[x].fillna(df[x].mean(), inplace=True)
                df[x] = self.binning(df[x], x)
            else:
                df[x].fillna(df.mode()[x][0], inplace=True)  # find the most comman value in month

    def binning(self,col ,nameOfColmn):
        labels = None
        minval = col.min()
        maxval = col.max()
        binslocal = int(self.m_bins)
        interval = (maxval - minval) * 1.0 / binslocal
        # print "maxval: ",maxval
        # print "minval: ",minval
        # print "interval: ",interval
        cut_points = []
        for x in range(0, binslocal + 1):
            cut_points.append(float("{0:.2f}".format(minval + x * interval)))

        if not labels:
            labels = range(len(cut_points) - 1)
        colBin = pd.cut(col, bins=cut_points, labels=labels, include_lowest=True)
        self.m_dictStructure[nameOfColmn] =labels ;
        return colBin

    def classify(self, path_test):
        ans = []
        attributName= []
        file = open(path_test, "r")
        # file descrtziantion !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        firstLoop = 0 ;
        for row in file:
            if row[len(row) - 1] == '\n':
                row = row[:-1]
            if firstLoop==0:
                attributName =row.split(',')
                firstLoop=1
                continue
            attribut = row.split(',')
            results=[]
            for classValue in self.m_dictStructure["class"]:
                i = 0
                tmpResult = 1
                for attributValue in attribut:
                    tmpResult= tmpResult * self.mainDic[attributName[i]][attributValue][classValue]
                    i += 1
                    results.append(tmpResult)
            ans.append(max(results))

        return ans

    def buildClassifier (self):
        m= 2.0
        for attribut in self.m_dictStructure:
            self.mainDic[attribut] = {}
            for attributValue in self.m_dictStructure[attribut]:
                self.mainDic[attribut][attributValue] = {}
                for classValue in self.m_dictStructure["class"]:
                    nc =self.df.loc[(self.df[attribut] == attributValue) & (self.df["class"] == classValue),[attribut]].count()
                    p= 1.0/len(self.m_dictStructure[attribut])
                    n = self.df.loc[(self.df["class"] == classValue),["class"]].count ()
                    self.mainDic[attribut][attributValue][classValue] = (nc + m*p)/(n+m)

    def buildModel(self, pathStructure, pathTrain, bins):
          self.m_dictStructure = {}
          self.mainDic = {}
          self.m_bins = bins
          self.df = pd.read_csv(pathTrain)
          self.readStructure(pathStructure)
          self.fillMissingValuesAndDiscretization(self.df)
          self.buildClassifier()


