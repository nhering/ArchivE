from tkinter import *
from tkinter import ttk
from tkinter import tkFileDialog
import os

class ArchivE:
    def __init__(self, master):
        self.label = ttk.Label(master, text = "Welcome to ArchivE--->")
        self.label.grid(row = 0, column = 0, columnspan = 2)

    currdir = os.getcwd()
    tkFileDialog.askdirectory(parent=root, initialdir=currdir, title="Select a source directory.")

def main():
    root = Tk()
    app = ArchivE(root)
    root.mainloop()

if __name__ == "__main__": main()