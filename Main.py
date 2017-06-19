import Tkinter as tk
import tkFileDialog
from Tkinter import *
import os.path
import tkMessageBox
from Classifier import *

class Main(Frame):
    # window design
    def showWindow(self):
        lbl_dir = Label(self, text="Directory Path: ")
        lbl_dir.grid(row=0, column=0, pady=40)

        self.entry_dir = Entry(self)
        self.entry_dir.grid(row=0, column=2)

        browse_button = Button(self, text="Browse", command=self.browse)
        browse_button.grid(row=0, column=4, sticky=E)

        lbl_bins = Label(self, text="Discretization Bins: ")
        lbl_bins.grid(row=2, column=0)

        self.entry_bins = Entry(self)
        self.entry_bins.grid(row=2, column=2)

        build_button = Button(self, text="Build", command=self.buildModel)
        build_button.grid(row=3, column=2, sticky=E, pady=15)

        classify_button = Button(self, text="Classify", command=self.classify)
        classify_button.grid(row=3, column=0, sticky=E, pady=15)

    # constructor of main window
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.classifier = Classifier()
        self.isBuild = False
        self.dir = ""
        self.bins = None
        self.pack()
        self.showWindow()

    # show browser window and put path in needed entry
    def browse(self):
        self.dir = tkFileDialog.askdirectory()
        self.entry_dir.insert(0, self.dir)

    # check if a path to file is exist, return true or false accordingly and show error if needed
    def checkPath(self, path):
        if not os.path.exists(path):
            tkMessageBox.showinfo("Error Message", "path: " + path + " doesn't exist")
            return False
        if os.stat(path).st_size < 3:
            tkMessageBox.showinfo("Error Message", "file in path: " + path + " is empty")
            return False
        return True

    # call the pre processing functions in the classifier, and chanfe current boolean to true
    def buildModel(self):
        if self.entry_bins.get().isdigit():
            self.bins = self.entry_bins.get()
            path_train = self.dir + "\\train.csv"
            path_structure = self.dir + "\\Structure.txt"
            if self.checkPath(path_train):
                if self.checkPath(path_structure):
                    Classifier.buildModel(self.classifier, path_structure, path_train, self.bins)
                    self.isBuild = True
                    tkMessageBox.showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
        else:
            tkMessageBox.showinfo("Naive Bayes Classifier", "Please enter a valid value for discretization bins!")

    # write the results to output file, receive a list
    def writeToFile(self, targets):
        path_output = self.dir + "\\output.txt"
        with open(path_output, "a") as f:
            for i, v in enumerate(targets):
                f.write(str(i+1) + " " + v + "\n")

    # check if the file exist, and check pre processing happend already before writing results and finishing
    def classify(self):
        path_test = self.dir + "\\test.csv"
        if self.checkPath(path_test):
            if not self.isBuild:
                tkMessageBox.showinfo("Naive Bayes Classifier", "You must Build before you can Classify!")
            else:
                if self.checkPath(path_test):
                    targets = Classifier.classify(self.classifier, path_test)
                    self.writeToFile(targets)
                    root.withdraw()
                    tkMessageBox.showinfo("Naive Bayes Classifier", "Classifying finished!")
                    os._exit(0)

root = tk.Tk()
root.title('Naive Bayes Classifier')
root.geometry("400x200")
app = Main(master=root)
app.mainloop()
