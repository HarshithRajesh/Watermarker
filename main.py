import os,sys
from tkinter import *
from PIL import Image,ImageFilter
from tkinter import filedialog

windows = Tk()
windows.title("Watermarker")
windows.config(pady=50,padx=50,bg='#E06469')
def image_processor():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All file","*.*")))
    im1 = Image.open(filename)
    im2 = Image.open("OIP.jpeg")
    w,h = im1.size
    # print(im1.format, im1.size, im1.mode)
    im2.thumbnail((100,100))
    
    im1.paste(im2,(w-100,h-100))
    im1.show()

canvas = Canvas(width=250,height=250,bg="#E06469",highlightthickness=0)
canvas.grid(row=1,column=1)
title_label = Label(text = "Watermarker",fg='#AFD3E2',bg='#E06469',font=("Ariel",26,"bold"))
title_label.grid(column=1,row=1)
btn = Button(text="Select Image",command=image_processor)
btn.grid(row=2,column=1)

windows.mainloop()
