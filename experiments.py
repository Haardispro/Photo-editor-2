from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog
import os

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Photo Editor")
        master.geometry("550x300+300+150")
        master.resizable(width=True, height=True)
        master.configure(bg="#222222")

        self.btn = Button(master, text='open image', command=self.openfn, font="None 12 bold")
        self.btn.pack()
        self.btn_blur = Button(master, text="blur image", command=self.blur_btn, font="None 12 bold")
        self.btn_blur.pack()

    def openfn(self):
        filename = filedialog.askopenfilename(title='open')
        #return filename
    #def open_img(self):
        x = filename
        self.img = Image.open(x)
        #img = img.resize((600, 600), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(self.img)
        panel = Label(root, image=image1)
        panel.image = image1
        panel.pack()
    def blur_btn(self):
        blur_img = self.img.filter(ImageFilter.GaussianBlur(5))
        blur_img.show()
        

root = Tk()
my_window = MainWindow(root)
root.mainloop()