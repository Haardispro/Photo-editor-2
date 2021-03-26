#this is just an experiment file 
#this is not the final version of the photo editing app
from PIL import Image, ImageFilter
from tkinter import Label, Button, PhotoImage, Tk
import os
import sys

w = Tk()
w.geometry("800x600")
w.title("Photo Editor")
#Functions
def blur():
    im = Image.open(r"C:\Users\haard\OneDrive\Desktop\Python projects\somethinguniques\joystick.png")
    im_blur = im.filter(ImageFilter.GaussianBlur(5))
    im_blur.save(r"C:\Users\haard\OneDrive\Desktop\Python projects\somethinguniques\joystick.png")
    os.execv(sys.argv[0], sys.argv)

main_image = PhotoImage(file=r"C:\Users\haard\OneDrive\Desktop\Python projects\somethinguniques\joystick.png")
photo = Label(w, image=main_image)
photo.grid(row=0, column=0, padx=260, pady=110)

blur_button = Button(w, text="Blur the image", command = blur)
blur_button.place(x=10, y=10)

w.mainloop()
