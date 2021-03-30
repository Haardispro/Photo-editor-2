from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
#root.geometry("550x300+300+150")
root.resizable(width=True, height=True)
root.title("Photo Editor")

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    #img = img.resize((600, 600), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

btn = Button(root, text='open image', command=open_img)
btn.pack()

root.mainloop()