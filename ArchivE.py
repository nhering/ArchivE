from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
from os import listdir
import time

# Currently set to 24 hours ago. This can be used later to accept a user defined time for validating if a file should be archived or not.
archiveTime = time.time() - 86400

mod_or_create = ""
instructions = "Step 1: Select the source directory\nStep 2: Select the destination directory\nStep 3: Select desired option for archiving\nStep 4: Press the 'Archive Now' button to perfom the archive"
srcdir = ""
dstdir = ""
results = "Please select source"

class Archive:
    def __init__(self, master):
        master.wm_title("Archive")

        #Instructions---------------------------------------------------------------------------------------------------
        ins=ttk.Frame(master)
        ins.grid(sticky=W, row=0, column=0)

        self.instruct=ttk.Label(ins, text=instructions, justify=LEFT, width = 65)
        self.instruct.grid(padx=5, pady=5, sticky=W, row=0, column=0)

        self.archive_btn=ttk.Button(ins, text="Archive\nNow", state=DISABLED, command="")
        self.archive_btn.grid(pady=5, row=0, column=1, sticky=NE)


        #Paths----------------------------------------------------------------------------------------------------------
        paths=ttk.Frame(master)
        paths.grid(padx=5, pady=5, sticky=W, row=1, column=0)

        self.src_btn=ttk.Button(paths, text="Source", command=lambda: select_src(self))
        self.src_btn.grid(pady=5, row=0, column=0)
        self.src_label = ttk.Label(paths, text=srcdir, justify=LEFT, width=64)
        self.src_label.grid(padx=5, pady=5, sticky=W, row=0, column=1, columnspan=2)

        self.dst_btn=ttk.Button(paths, text="Destination", command=lambda: select_dst(self))
        self.dst_label=ttk.Label(paths, justify=LEFT, width=64, text=dstdir)

        def select_src(self):
            global srcdir
            srcdir = filedialog.askdirectory(initialdir="/", title="Select source directory.")
            self.src_label.config(text=srcdir)
            validate_paths(self)

        def select_dst(self):
            global dstdir
            dstdir = filedialog.askdirectory(initialdir="/", title="Select destination directory.")
            self.dst_label.config(text=dstdir)

        def validate_paths(self):
            if (srcdir == ""):
                self.src_label.config(text="Please select source directory.")
            if (srcdir != ""):
                self.dst_btn.grid(pady=5, row=1, column=0)
                self.dst_label.grid(padx=5, sticky=W, row=1, column=1, columnspan=2)


            if (srcdir == "" and dstdir == ""):
                self.results.config(text="Please select source")
            elif (srcdir == "" and dstdir != ""):
                self.results.config(text="That's a nice destination folder. Now please select source")
            elif (srcdir != "" and dstdir == ""):
                self.results.config(text = "Please select destination")
            elif (srcdir == dstdir):
                self.results.config(text="Source and destination may not be the same.")
            else:
                self.results.config(text="")


        #Options--------------------------------------------------------------------------------------------------------
        options=ttk.Frame(master, width=600)
        options.grid(padx=5, pady=15, sticky=W, row=2, column=0)

        self.options_text=ttk.Label(options, text="Select desired option.")
        self.options_text.grid(pady=5, sticky=W, row=0, column=0, columnspan=3)

        self.mod_create_opt1=ttk.Radiobutton(options, text = "Archive only files that have been modified in the past 24 hours.", variable=mod_or_create, value="m")
        self.mod_create_opt1.grid(padx=2, pady=1, sticky=W, row=1, column=0)

        self.mod_create_opt2=ttk.Radiobutton(options, text = "Archive only files that have been created in the past 24 hours.", variable=mod_or_create, value="c")
        self.mod_create_opt2.grid(padx=2, pady=1, sticky=W, row=2, column=0)

        self.mod_create_opt3=ttk.Radiobutton(options, text = "Archive files that have been either modified or created in the past 24 hours.", variable=mod_or_create, value="mc")
        self.mod_create_opt3.grid(padx=2, pady=1, sticky=W, row=3, column=0)


        #Feedback-------------------------------------------------------------------------------------------------------
        self.results=ttk.Label(master, justify=LEFT, text=results)
        self.results.grid(padx=5, pady=5, sticky=W, row=4, column=0, columnspan=2)



def main():
    root = Tk()
    app = Archive(root)
    root.mainloop()

if __name__ == "__main__": main()