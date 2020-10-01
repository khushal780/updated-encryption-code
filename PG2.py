from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from cryptography.fernet import Fernet

def t_2_t():
    root = Tk()
    
    root.title("CRYPTOGRAPHY")
    root.resizable(0,0)     
    #root.geometry("1350x750")
    root.configure(background='#fff700')
    
    
    
    def encrypt_win():
        if(tx.get()==""):
             out_text.insert(END,"Please enter text to encrypt");
    
        else:
            def write_key():
                key = Fernet.generate_key();
                with open("key.key", "wb") as key_file:
                    key_file.write(key)
                
            def load_key():
                return open("key.key", "rb").read()
    
            write_key()
            key = load_key()
            mz=tx.get()
            message = mz.encode()
            f = Fernet(key)
            encrypted = f.encrypt(message)
            out_text.insert(END,encrypted)
            ent_text_d.insert(END,encrypted)
            decrypted=f.decrypt(encrypted)
            out_text_d.insert(END,decrypted)

            
        
    
    def reset():
        out_text.delete(1.0,END)
        out_text_d.delete(1.0,END)
        ent_text_d.delete(1.0,END)
        
    tx=StringVar();
    tx1=StringVar();
    #logo img
    '''
    logo = ImageTk.PhotoImage(Image.open("lOGO 2.png"))
    imglogo = Label(image=logo, bg="#fff700")
    imglogo.grid()
    '''
    #$$$$$$$$$$$$$$$$$$$$$$$$ Encrypt $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    #======================== Heading ===================================================
    heading_e = Label(root, text="ENCRYPT",font=("Arial Black", 25,'bold'), bg="#fff700")
    heading_e.grid(columnspan=2)
    #======================== Heading ===================================================
    
    #======================== INPUT ===================================================
    text = Label(root, text="Text :",font=("Arial", 15), bg="#fff700")
    text.grid(row=1, column=0)
    ent_text = Entry(root, bd=5,borderwidth=10,textvariable=tx,width=50,relief=RIDGE)
    ent_text.grid(row=1, column=1,ipadx=50,ipady=30,padx=20)
    #======================== INPUT ===================================================
    
    #======================== BUTTON ===================================================
    #button 1
    t_to_t = Button(root, text="Text to Text Encryption ", borderwidth=2,bg='#E89A00', font=("Arial",15),compound = RIGHT,command=encrypt_win)
    t_to_t.grid(row=2, column=0, padx=20, pady=10)
    #button 2
    t_to_2 = Button(root, text="Reset", borderwidth=2,bg='#E89A00', font=("Arial",15),compound = RIGHT,width=25,command=reset)
    t_to_2.grid(row=2, column=1)
    #======================== BUTTON ===================================================
    
    #======================== OUTPUT ===================================================
    out_text = Text( bd=5,borderwidth=10,height=12,width=60,relief=RIDGE)
    out_text.grid(row=3,column=0,columnspan=2)
    #======================== OUTPUT ===================================================
    #$$$$$$$$$$$$$$$$$$$$$$$$ Encrypt $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    seperator = ImageTk.PhotoImage(Image.open("seperator.jpg"))
    seperator_ = Label(image=seperator, bg="#fff700")
    seperator_.grid(row=0, column=2, rowspan=4)
    
    #$$$$$$$$$$$$$$$$$$$$$$$$ Decrypt $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    #======================== Heading ===================================================
    heading_d = Label(root, text="DECRYPT",font=("Arial Black", 25,'bold'), bg="#fff700")
    heading_d.grid(row=0,column=3,columnspan=2)
    #======================== Heading ===================================================
    
    #======================== INPUT ===================================================
    text_d = Label(root, text="Encrypted Text :",font=("Arial", 15), bg="#fff700")
    text_d.grid(row=1, column=3)
    ent_text_d = Text(root, bd=5,borderwidth=10,height=3,width=30,relief=RIDGE)
    ent_text_d.grid(row=1, column=4,ipadx=50,ipady=30,padx=20)
    #======================== INPUT ===================================================
    
    #======================== BUTTON ===================================================
    """#button 1
    d_to_t = Button(root, text="Text to Text Decrytion ", borderwidth=2,bg='#E89A00', font=("Arial",15),compound = RIGHT)
    d_to_t.grid(row=2, column=3, padx=20, pady=10)
    #button 2
    reset = Button(root, text="Reset", borderwidth=2,bg='#E89A00', font=("Arial",15),compound = RIGHT,width=25)
    reset.grid(row=2, column=4)"""
    #======================== BUTTON ===================================================
    
    #======================== OUTPUT ===================================================
    out_text_d = Text( bd=5,borderwidth=10,height=12,width=60,relief=RIDGE)
    out_text_d.grid(row=3,column=3,columnspan=2)
    #======================== OUTPUT ===================================================
    #$$$$$$$$$$$$$$$$$$$$$$$$ Decrypt $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    root.mainloop()

