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


    def fillMissingValuesAndDiscretization(self):
        tmp = 'NUMERIC'

        for x in self.m_dictStructure:
            if (self.m_dictStructure[x] == 'NUMERIC'):
                self.df[x].fillna(self.df[x].mean(), inplace=True)
                self.df[x] = self.binning(self.df[x])
            else:
                self.df[x].fillna(self.df.mode()[x][0], inplace=True)  # find the most comman value in month
        # print(df.apply(lambda x: sum(x.isnull()), axis=0)) # print the missing values in eche colmn


    def binning(self,col):
        labels = None
        minval = col.min()
        maxval = col.max()
        interval = (maxval - minval) * 1.0 / self.m_bins
        # print "maxval: ",maxval
        # print "minval: ",minval
        # print "interval: ",interval
        cut_points = []
        for x in range(0, self.m_bins + 1):
            cut_points.append((minval + x * interval))
        break_points = cut_points
        if not labels:
            labels = range(len(cut_points) - 1)
        colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
        return colBin

    def classifier(self):
        target = "yes"
        return target

    def classify(self, path_test):
        df_test = pd.read_csv(path_test)

        list = ['yes', 'yes', 'no']
        return list

    def buildClassifier (self):

       #for attribut in self.m_dictStructure:

     # print(df.loc[(df["education"] == "secondary") & (df["marital"] == "married"),["education", "marital"]])
      return




    def buildModel(self, path, bins):
          self.m_dictStructure = {}
          self.m_bins = bins
          self.df = pd.read_csv(path)
          self.readStructure(path)
          self.fillMissingValuesAndDiscretization()
          self.buildClassifier()


