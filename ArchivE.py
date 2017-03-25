from tkinter import *
from tkinter import ttk
import Update
from tkinter import filedialog


class Archive:
    def __init__(self, master):
        master.wm_title("Archive")

        self.instruct=ttk.Label(master, text=Update.instructions, justify=LEFT)
        self.instruct.grid(sticky=W, row=0, column=0, columnspan=2)

        ttk.Button(master,text="Archive\nNow",state='disabled',command="").grid(row=0, column=2, sticky=E)

        ttk.Button(master, text="Source", command=lambda: Update.select_src(self)).grid(row=1, column=0)
        self.src_label = ttk.Label(master, text=Update.srcdir, relief=RIDGE, justify=LEFT, width=64)
        self.src_label.grid(sticky=W, row=1, column=1, columnspan=2)

        ttk.Button(master,text="Destination", command=lambda: Update.select_dst(self)).grid(row=2, column=0)
        self.dst_label=ttk.Label(master, relief=RIDGE, justify=LEFT, width=64, text=Update.dstdir)
        self.dst_label.grid(sticky=W, row=2, column=1, columnspan=2)


def main():
    root = Tk()
    app = Archive(root)
    root.mainloop()

if __name__ == "__main__": main()