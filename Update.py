from tkinter import ttk
from tkinter import filedialog


instructions = "Step 1: Select the source directory\nStep 2: Select the destination directory\nStep 3: Press the 'Archive Now' button to perfom the archive"

srcdir="Directory not yet selected"
dstdir="Directory not yet selected"

def select_src(self):
    srcdir = filedialog.askdirectory(initialdir="/", title="Select source directory.")
    self.src_label.config(text=srcdir)

def select_dst(self):
    dstdir = filedialog.askdirectory(initialdir="/", title="Select destination directory.")
    self.dst_label.config(text=dstdir)
