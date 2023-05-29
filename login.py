from tkinter import *
import tkinter.font as font

def LoginPage():
    import tkinter as tk
    import mysql.connector
    from tkinter import messagebox
    
    from reg import register
    from home import HomePage

    mydb = mysql.connector.connect(host="localhost",user="root",password="1234")
    c = mydb.cursor(buffered=True)
    c.execute("use toll")

    def submit():
         
        user = Username.get()
        passw = password.get()  
        login(user, passw)
      
     
    def login(user, passw):
         
        # If password is enetered by the
        # user
        c.execute("Select FullName from Users")
        users_tup= c.fetchall()
        c.execute("Select Password from Users")
        passwords_tup= c.fetchall()

        users=[]
        passwords=[]
        for i in users_tup:
            users.append(i[0])
        for i in passwords_tup:
            passwords.append(i[0])

        '''
        count= 0
        for u in users:
            if user==u[count]:
                if passwords[count]==passw:
                    HomePage(user)
            count+=1
        '''
        flag= 1
        for i in range(len(users)):
            if users[i]==user:
                if passwords[i]==passw:
                    flag= 0
                    HomePage(user)
        if flag:
            messagebox.showerror(title="Incorrect", message="Incorrect Username/ Password")
            #LoginPage()
        
          
     
    root = tk.Tk()
    root.state("zoomed")
    root.title("LOGIN PAGE")
    canvas1=Canvas(root,width=100,height=100)
    canvas1.pack(fill = "both",expand =True)
    canvas1.configure(background='#6FABB7')
    root.geometry("600x600")
    # Defining the first row
    header = Label(root, text="LOGIN" ,fg='black',bg='#6FABB7',font=("Lucida Sans Unicode",26,"bold"))
    header.place(relx=0.5, rely=0.2, anchor=CENTER)
    lblfrstrow = tk.Label(root, text ="Username:",bg='#6FABB7',font=("bold", 20) ,width=20)
    lblfrstrow.place(x = 300, y = 220)
     
    Username = tk.Entry(root, width = 100)
    Username.place(x = 550, y = 220, width = 300,height=30)
      
    lblsecrow = tk.Label(root, text ="Password:",bg='#6FABB7',font=("bold", 20),width=20)
    lblsecrow.place(x = 300, y = 300)
     
    password = tk.Entry(root, width = 100)
    password.place(x = 550, y = 300, width = 300,height=30)
    button_font = font.Font(family='Helvitica', size=10)
    submitbtn = tk.Button(root, text ="Login",fg='#ffffff',relief = SOLID,bd=0,height = 3, width=30,bg='#190380',font=button_font,
                           command = submit)
    submitbtn.place(relx=0.7, rely=0.65, anchor=CENTER)

    registerbtn = tk.Button(root, text ="Register",fg='#ffffff',relief = SOLID,bd=0,height = 3, width=30,bg='#190380',font=button_font,
                           command= register)
    registerbtn.place(relx=0.27, rely=0.65, anchor=CENTER)


     
    root.mainloop()
LoginPage()
