import shutil
import os
from os import listdir
import time
from tkinter import *
from tkinter import ttk



srcdir = ""
dstdir = ""

# Currently set to 24 hours ago. This can be used later to accept a user defined time for validating if a file should be archived or not.
archiveTime = time.time() - 86400

# prompt for create and/or modified date as the criteria for coping the file
criteria = ""
while (criteria != "c") and (criteria != "m"):
    criteria = input(
        "\nWould you like to copy files that have been CREATED in the last 24 hours?\nOr would you like to copy files that have been MODIFIED in the last 24 hours?\nEnter 'c' or 'm'.")

filesInFolder = listdir(srcdir)

def file_copier(filesInFolder, criteria):
    filesCopied = []
    filesNotCopied = []
    if (criteria == "m"):
        for i in filesInFolder:
            fileCreateTime = os.path.getmtime(srcdir + "\\" + i)
            if (fileCreateTime > archiveTime):
                shutil.copyfile((srcdir + "\\" + i), (dstdir + "\\" + i))
                filesCopied.append(i)
            else:
                filesNotCopied.append(i)
    elif (criteria == "c"):
        for i in filesInFolder:
            fileCreateTime = os.path.getctime(srcdir + "\\" + i)
            if (fileCreateTime > archiveTime):
                shutil.copyfile((srcdir + "\\" + i), (dstdir + "\\" + i))
                filesCopied.append(i)
            else:
                filesNotCopied.append(i)
    else:
        print("Error in criteria. Exiting")
        exit
    print(str(len(filesCopied)) + " Files have been copied: ")
    print(filesCopied)
    print("\n" + str(len(filesNotCopied)) + " Files have not been copied: ")
    print(filesNotCopied)

file_copier(filesInFolder, criteria)
