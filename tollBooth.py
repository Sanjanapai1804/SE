from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
import datetime as dt
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234")
from tkinter import messagebox

import reg
import login
 

root=Tk() #Creating a window
root.title("Automated Toll Booth")
background_image = PhotoImage(file="toll4.png")
bgimage_label = Label(root, image=background_image)
bgimage_label.place(relwidth=1, relheight=1)
button_font = font.Font(family='Helvitica', size=15)

def pay():
    c = mydb.cursor(buffered=True)
    c.execute("use toll")
    c.execute("SELECT Plate from users")
    nums=c.fetchall()
    lp=[]
    for i in nums:
        lp.append(i[0])
    if e1.get() not in lp:
        messagebox.showerror(' Error', 'Error: License number does not exists, Please register')
    else:
        query = "SELECT * from users where Plate = '{}'".format(e1.get())
        print(query)
        c.execute(query)
        
        records = c.fetchall()
        print(records)
        type=records[0][7]
        money = records[0][6]
        print(money)
        if type == '2-wheeler':
            if money < 20:
                messagebox.showerror(' Error', 'Insufficeint funds')
            else:
                money-=20
                l1=Label(root, text="Payment successfull",fg='red',font=("Times New Roman",22,"bold"))
                l1.place(relx=0.5, rely=0.7, anchor=CENTER)
        elif type == '4-wheeler':
            if money < 40:
                messagebox.showerror(' Error', 'Insufficeint funds')
            else:
                money-=40
                l1=Label(root, text="Payment successfull",fg='red',font=("Times New Roman",22,"bold"))
                l1.place(relx=0.5, rely=0.7, anchor=CENTER)
        elif type == 'heavy vehicle':
            if money < 60:
                messagebox.showerror(' Error', 'Insufficeint funds')
            else:
                money-=60
                l1=Label(root, text="Payment successfull",fg='red',font=("Times New Roman",22,"bold"))
                l1.place(relx=0.5, rely=0.7, anchor=CENTER)
        elif type=="":
            messagebox.showerror(' Error', 'Error: Enter valid number')
        Uquery = "UPDATE users SET Money ='{}' WHERE Plate ='{}' ".format(money,e1.get())
        c.execute(Uquery)
        e1.delete(0,END)
        
        
        msg = "Account balance :-"+str(money)
        l2=Label(root, text=msg,fg='red',font=("Times New Roman",22,"bold"))
        l2.place(relx=0.5, rely=0.8, anchor=CENTER)
        root.after(4000, lambda: l1.destroy())
        root.after(4000, lambda: l2.destroy())
        
    mydb.commit()
    
def regi():
    reg.register()

def logi():
    login.LoginPage()
   

l1=Label(root, text="SCANNED LICENSE NUMBER",fg='black',bg='white',font=("Times New Roman",22,"bold")).place(relx=0.5, rely=0.3, anchor=CENTER)

e1=Entry(root,width=30,font=("Times New Roman",18))
e1.config(highlightthickness=3, highlightbackground="black")

e1.place(relx=0.5, rely=0.4, anchor=CENTER)
bt1= Button(root,text = "Pay",relief = SOLID,height = 3, width=30,bg='#FFD343',fg='black',font=button_font,command=pay).place(relx=0.95, rely=0.7, anchor=SE)
bt1= Button(root,text = "Register",relief = SOLID,height = 3, width=30,bg='#190380',fg='#ffffff',font=button_font,command=regi).place(relx=0.3, rely=0.8, anchor=SE)
bt1= Button(root,text = "Login",relief = SOLID,height = 3, width=30,bg='#190380',fg='#ffffff',font=button_font, command=logi).place(relx=0.3, rely=0.6, anchor=SE)

root.state("zoomed")
root.mainloop()

