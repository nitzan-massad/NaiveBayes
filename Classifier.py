import pandas as pd
import copy
class Classifier:

# initaliz the class and all the parmaters
    def __init__(self):
        self.path = None
        self.m_dictStructure = {}
        self.mainDic = {}
        self.allInteravls = {}
        self.testStructure = {}
# read the structure of the file and cut it and arrange it into a dic for use Later
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
# fill all the missing values and send eche colmn to Discretization
    def fillMissingValuesAndDiscretization(self, df):
        for x in self.m_dictStructure:
            if (self.m_dictStructure[x] == 'NUMERIC'):
                #df[x].fillna(df[x].mean(), inplace=True)
                for classValue in self.m_dictStructure["class"]:
                    self.df.loc[(self.df["class"] == classValue), ["class"]].fillna(df[x].mean(), inplace=True)
                df[x] = self.binning(df[x], x)
            else:
                df[x].fillna(df.mode()[x][0], inplace=True)  # find the most comman value in month
    #Discretization a colmn and set the data between intervals
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
        # save all imtervals for their attricutes to use for test
        self.allInteravls[nameOfColmn]= cut_points
        if not labels:
            labels = range(len(cut_points) - 1)
        colBin = pd.cut(col, bins=cut_points, labels=labels, include_lowest=True)
        self.m_dictStructure[nameOfColmn] =labels;
        return colBin
# Discretization the test file by the values that we take from the Discretization of the train
    def discretization_test(self, df_test):
        for attr in self.m_dictStructure:
            if self.testStructure[attr] == 'NUMERIC':
                labels = None
                cut_points = self.allInteravls[attr]

                if not labels:
                    labels = range(len(cut_points) - 1)
                colBin = pd.cut(df_test[attr], bins=cut_points, labels=labels, include_lowest=True)
                df_test[attr] = colBin
        return df_test
# get a path of a csv file and classfiy eche row to the coorect class by the Knowhow we take from the train set
    def classify(self, path_test):
        numberOfCorrect = 0
        ans = []
        file = pd.read_csv(path_test)
        file = self.discretization_test(file)

        for rowNumber in range(len(file["class"])):
            result= []
            resultClassName= []
            for classValue in self.m_dictStructure["class"]:
               tmpResult = 1.0
               for attribut in self.m_dictStructure:
                   if (attribut!="class"):
                    tmpResult=float(tmpResult*float(self.mainDic[attribut][file[attribut][rowNumber]][classValue]))
               result.append(tmpResult)
               resultClassName.append(classValue)
            index = result.index(max(result))
            ans.append(resultClassName[index])
            if str(resultClassName[index]) == str(file["class"][rowNumber]):
                numberOfCorrect+=1
        print " prec :", float(float(numberOfCorrect)/float(len(file["class"])))

        return ans
# the function build the main dic that will hold all the culclaition from the trin set for naive bayes formola
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
                    self.mainDic[attribut][attributValue][classValue] = float(nc + m*p)/(n+m)

# the function that we call first, she build all the modle and all the data sets for calssficiton in the futhre
    def buildModel(self, pathStructure, pathTrain, bins):
          self.m_bins = bins
          self.df = pd.read_csv(pathTrain)
          self.readStructure(pathStructure)
          self.testStructure = copy.deepcopy(self.m_dictStructure)
          self.fillMissingValuesAndDiscretization(self.df)
          self.buildClassifier()


