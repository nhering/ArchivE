from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class ArchivE:

    def __init__(self, master):
        master.wm_title("Welcome to Archive")

        srcdir=""

        self.Label = ttk.Label(master, text="Step 1: Select the source directory\nStep 2: Select the destination directory\nStep 3: Press the 'Archive Now' button to perfom the archive",justify=LEFT).grid(sticky=W, row=0, column=0, columnspan=2)

        ttk.Button(master, text = "Source", command='').grid(row=1, column=0)
        selsrc=ttk.Label(master, relief=RIDGE, justify=LEFT, width=64, text="Directory not selected").grid(sticky=W, row=1, column=1)

        ttk.Button(master,text="Destination", command='').grid(row=2, column=0)
        seldst=ttk.Label(master, relief=RIDGE, justify=LEFT, width=64, text="Directory not selected").grid(sticky=W, row=2, column=1)

        ttk.Button(master,text="Archive\nNow",state='disabled',command="").grid(row=0, column=3)

    # def select_src(self):
    #     srcdir = filedialog.askdirectory(initialdir="/",title="Select source directory.")
    #     selsrc.config(text=srcdir)
    # def select_dst(self):
    #     dstdir = filedialog.askdirectory(initialdir="/",title="Select destination directory.")


def main():
    root = Tk()
    app = ArchivE(root)
    root.mainloop()

if __name__ == "__main__": main()