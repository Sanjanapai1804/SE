from tkinter import *

def HomePage(username):
    import tkinter as tk
    import mysql.connector
    from tkinter import messagebox
    from PIL import ImageTk,Image

    mydb = mysql.connector.connect(host="localhost",user="root",password="1234")
    c = mydb.cursor(buffered=True)
    c.execute("use toll")

    def Profile():
        def Update():
            Chosen_type= chosen_type.get()
            Chosen_plate= chosen_plate.get()
            if Chosen_type != typev:
                c.execute("UPDATE users SET Type ='{}' WHERE FullName ='{}' ".format(Chosen_type, username))
            if Chosen_plate and (Chosen_plate != plate):
                c.execute("UPDATE users SET Plate ='{}' WHERE FullName ='{}' ".format(Chosen_plate, username))
            mydb.commit()

            c.execute("Select * from users where FullName='{}'".format(username))
            details= c.fetchall()
            details= details[0]
            fullname= details[0]
            email= details[1]
            plate2= details[4]
            typev2= details[7]
            if Chosen_type!= typev or (Chosen_plate and Chosen_plate != plate):
                display = tk.Label(root, text = "{}\n\n{}\n{}\n{}".format(fullname, email, plate2, typev2), font=("Lucida Sans Unicode",18,"bold"))
                display.place(x = 480, y = 80, width = 300)
            
            
        def Home():
            HomePage(username)
            
        submitbtn.destroy()
        registerbtn.destroy()
        typel = ['2-wheeler','4-wheeler','heavy vehicle']
        
        c.execute("Select * from users where FullName='{}'".format(username))
        details= c.fetchall()
        details= details[0]
        fullname= details[0]
        email= details[1]
        plate= details[4]
        typev= details[7]
        display = tk.Label(root, text = "{}\n\n{}\n{}\n{}".format(fullname, email, plate, typev), font=("Lucida Sans Unicode",18,"bold"))
        display.place(x = 480, y = 80, width = 300)

        display = tk.Label(root, text = "Change Plate No.", font=("Lucida Sans Unicode",20,"bold"))
        display.place(x = 400, y = 300)
        chosen_plate = tk.Entry(root, font=("Lucida Sans Unicode",18,"bold"))  
        chosen_plate.place(x=700, y=300, width= 300)

        display = tk.Label(root, text = "Change Vehicle type", font=("Lucida Sans Unicode",18,"bold"))
        display.place(x = 400, y = 350)
        chosen_type= StringVar()
        chosen_type.set(typev)
        drop= OptionMenu(root, chosen_type, *typel)
        drop.place(x=700, y=350)

        subbtn = tk.Button(root, text ="Update", bg ='white', command= Update, font=("Lucida Sans Unicode",18,"bold"))
        subbtn.place(x = 480, y = 400, width = 300)
        bckbtn = tk.Button(root, text ="Back", bg ='white', command= Home)
        bckbtn.place(x = 480, y = 600, width = 300)
      
     
    def Wallet():
        submitbtn.destroy()
        registerbtn.destroy()
        
        def Home():
            HomePage(username)
            
        def Add():
            c.execute("Select Money from users where FullName='{}'".format(username))
            money= c.fetchall()
            money= money[0][0]
        
            Change= change.get()
            balance= str(int(money)+int(Change))
            
            display = tk.Label(root, text = "BALANCE\n{}".format(balance), font=("Lucida Sans Unicode",26,"bold"))
            display.place(x = 480, y = 80, width = 300, height= 80)           

            Uquery = "UPDATE users SET Money ='{}' WHERE FullName ='{}' ".format(balance, username)
            c.execute(Uquery)
            mydb.commit()
        
        def Sub():
            c.execute("Select Money from users where FullName='{}'".format(username))
            money= c.fetchall()
            money= money[0][0]
            
            Change= change.get()
            balance= str(int(money)-int(Change))
            if int(balance)<0:
                #change.delete(0,END)
                messagebox.showerror("ERROR", "Insufficient balance in wallet")
            else:
                display = tk.Label(root, text = "BALANCE\n{}".format(balance), font=("Lucida Sans Unicode",26,"bold"))
                display.place(x = 480, y = 80, width = 300, height= 80)

                Uquery = "UPDATE users SET Money ='{}' WHERE FullName ='{}' ".format(balance, username)
                c.execute(Uquery)
                mydb.commit()
        
        c.execute("Select Money from users where FullName='{}'".format(username))
        money= c.fetchall()
        money= money[0][0]

        display = tk.Label(root, text = "BALANCE\n{}".format(money), font=("Lucida Sans Unicode",26,"bold"))
        display.place(x = 480, y = 80, width = 300, height= 80)

        change = tk.Entry(root)  
        change.place(x=380, y= 200, width= 460, height= 30)

        addbtn = tk.Button(root, text ="Add money",
                          bg ='white', command = Add, font=("Lucida Sans Unicode",20,"bold"))
        addbtn.place(x = 480, y = 320, width = 300)

        change.delete(0,END)

        subbtn = tk.Button(root, text ="Deduct money",
                              bg ='white', command= Sub, font=("Lucida Sans Unicode",20,"bold"))
        subbtn.place(x = 480, y = 430, width = 300)
        change.delete(0,END)
        
        bckbtn = tk.Button(root, text ="Back", bg ='white', command= Home)
        bckbtn.place(x = 480, y = 600, width = 300)
        
        
    root = tk.Toplevel(bg= '#000000')
    #root.configure(bg='black')
    background_image = tk.PhotoImage(file="toll4.png")
    bgimage_label = tk.Label(root, image=background_image)
    bgimage_label.place(relwidth=1, relheight=1)

    
    root.state("zoomed")
    root.title("HOME PAGE")
      
     
    submitbtn = tk.Button(root, text ="View Profile",
                          bg ='white', command = Profile, font=("Lucida Sans Unicode",26,"bold"))
    submitbtn.place(x = 500, y = 300, width = 300, height= 80)

    registerbtn = tk.Button(root, text ="View Wallet",
                          bg ='white', command= Wallet, font=("Lucida Sans Unicode",26,"bold"))
    registerbtn.place(x = 500, y = 400, width = 300, height= 80)


     
    root.mainloop()
