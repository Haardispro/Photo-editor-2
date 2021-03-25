#from PIL import Image
from tkinter import *
#import tkinter as tk
from tkinter import filedialog

#Functions
def openfile():
    root.withdraw()
    filedialog.askopenfilename()
    root.deiconify()

root = Tk()
root.title("Photoeditor")
root.geometry("800x600")
root.configure(bg="white")

#Open and save
open_file = Button(root, text="Open file", command=openfile)
open_file.grid(row=0, column=0)
save_file = Button(root, text="Save File")

#Editing functions
#---changing the size of the image using thumbnail function

size = Button(root, text="Select Image size")
#Change dominant color

dom_col = Button(root, text="Change the dominant color of the image")

#Blur
#Filters
#Cropping
root.mainloop()
