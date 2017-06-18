import Tkinter as tk
import tkFileDialog
from Tkinter import *

#from Classifier import *

class Main(Frame):

    def showWindow(self):
        lbl_dir = Label(self, text="Directory Path: ")
        lbl_dir.grid(row=0, column=0, pady=40)

        self.entry_dir = Entry(self)
        self.entry_dir.grid(row=0, column=2)

        browse_button = Button(self, text="Browse", command=self.browse)
        browse_button.grid(row=0, column=4, sticky=E)

        lbl_bins = Label(self, text="Number of Bins: ")
        lbl_bins.grid(row=2, column=0)

        self.entry_bins = Entry(self)
        self.entry_bins.grid(row=2, column=2)

        build_button = Button(self, text="Build", command=self.browse)
        build_button.grid(row=3, column=2, sticky=E, pady=15)

        classify_button = Button(self, text="Build", command=self.browse)
        classify_button.grid(row=3, column=0, sticky=E, pady=15)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.showWindow()

    def browse(self):
        dir= tkFileDialog.askdirectory()
        self.entry_dir.insert(0, dir)


root = tk.Tk()
root.title('Naive Bayes Classifier')
root.geometry("400x200")
app = Main(master=root)
app.mainloop()
