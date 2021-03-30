from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os




class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Photo Editor")
        master.geometry("550x300+300+150")
        master.resizable(width=True, height=True)

        self.btn = Button(master, text='open image', command=self.open_img)
        self.btn.pack()
        self.btn_blur = Button(master, text="blur image", command=self.blur_btn)
        self.btn_blur.pack()

    def openfn(self):
        filename = filedialog.askopenfilename(title='open')
        return filename
    def open_img(self):
        x = self.openfn
        img = Image.open(x)
        #img = img.resize((600, 600), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.pack()
    def blur_btn(self):

        return

root = Tk()
my_window = MainWindow(root)
root.mainloop()