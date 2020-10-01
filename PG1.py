from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from PG2 import*
from PG3 import*

root = Tk()
def destroy():
    root.destroy()

#window configuration
root.title("CRYPTOGRAPHY")
root.resizable(0,0)     
#root.geometry("1350x750")
root.configure(background='#fff700')

#logo img
logo = ImageTk.PhotoImage(Image.open("logo1.png"))
imglogo = Label(image=logo, bg="#fff700").grid( columnspan=2)

#button 1
t_to_t = Button(root, text="Text to Text Encryption ", borderwidth=0,bg='#E89A00',command=lambda:[destroy(),t_2_t()], font=("Arial",15),compound = RIGHT, padx=12, pady=12).grid(columnspan=2, padx=20, pady=12)

#button 2
t_to_img = Button(root, text="Text File Encryption ", borderwidth=0,bg='#E89A00',command=lambda:[destroy(),win_3()], font=("Arial",15),compound = RIGHT, padx=12, pady=12).grid(columnspan=2, padx=12, pady=12)
root.mainloop()
