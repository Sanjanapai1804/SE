from tkinter import *
import tkinter.font as font
#button_font = font.Font(family='Helvitica', size=15)
def register():
        from tkinter import messagebox
        import mysql.connector
        import re

        mydb = mysql.connector.connect(host="localhost",user="root",password="1234")
        gen = ['M','F', 'None']
        typel = ['2-wheeler','4-wheeler','heavy vehicle']



        def checkPsw(Passw):
                special_characters = '!@#$%&()-_[]{};:"./<>?'
                mes =[
                lambda Passw: any(x.isupper() for x in Passw) or 'String must have 1 upper case character.',
                lambda Passw: any(x.isdigit() for x in Passw) or 'digit',
                lambda Passw: len(Passw) >= 6 and len(Passw) <=12  or 'len',
                lambda Passw: any(map(lambda x: x in Passw, special_characters)) or 'spec',]
                result = [x for x in [i(Passw) for i in mes] if x != True]
                return result
        def checkEmail(Email):
                pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
                if re.match(pat,Email):
                        return True
                else:
                        return False
                
                
        def submitact():
                
                if(not(entry_1.get()) and not(entry_02.get())  and not (chosen_gender.get()) and not(entry_04.get()) and not(entry_05.get()) and not(entry_06.get()) and not(entry_07.get()) and not (chosen_type.get()) and not(entry_09.get()) ):
                        base.destroy()
                else:
                        FullName    = entry_1.get()
                        Email       = entry_02.get()
                        Gender      = chosen_gender.get()
                        Age         = entry_04.get()
                        Plate       = entry_05.get()
                        State       = entry_06.get()
                        Money       = entry_07.get()
                        Type        = chosen_type.get()
                        Passw       = entry_09.get()

                        res = checkPsw(Passw)
                        
                        t = checkEmail(Email)        
                        if res :
                            messagebox.showerror("Please try again", "Please ensure the Password has \n* a minimum of 6 characters and a maximum  of 12 characters \n* atleast one special character \n* one capital letter \n* one digit")
                        elif not t:
                            messagebox.showerror("Please try again", "Please Ensure email is in right format")
                        else:
                                d = (FullName,Email,Gender,Age,Plate,State,Money,Type,Passw)
                                c = mydb.cursor(buffered=True)
                                c.execute("CREATE DATABASE if not exists toll")
                                c.execute("use toll")
                                s1 = "CREATE TABLE IF NOT EXISTS Users(FullName TEXT,Email TEXT, Gender TEXT, Age INT,Plate TEXT,State TEXT,Money INT,Type TEXT,Password TEXT)"
                                c.execute(s1)

                                c.execute("Select Plate from Users")
                                plates_tup= c.fetchall()
                                plates= []

                                for i in plates_tup:
                                    plates.append(i[0])

                                if Plate in plates:
                                        messagebox.showerror("ERROR", "Liscence plate already registered")
                                else:
                                        s2 = "INSERT INTO Users(FullName,Email,Gender,Age,Plate,State,Money,Type,Password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        c.execute(s2,d)

                                        mydb.commit()
                                        
                                base.destroy()
                
        base = Tk()
        base.geometry("600x700")
        #base.state("zoomed")
        base.title("Registration Form-Toll booth") 
        canvas1=Canvas(base,width=100,height=100)
        canvas1.pack(fill = "both",expand =True)
        canvas1.configure(background='#6FABB7')
        labl_0 = Label(base, text="REGISTRATION FORM",bg='#6FABB7',width=20,font=("bold", 20))  
        labl_0.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        labl_1 = Label(base, text="Full Name",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_1.place(x=80,y=130)
          
        entry_1 = Entry(base)  
        entry_1.place(x=240,y=130)
          
        labl_2 = Label(base, text="Email",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_2.place(x=68,y=180)  
          
        entry_02 = Entry(base)  
        entry_02.place(x=240,y=180)  
          
        labl_3 = Label(base, text="Gender",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_3.place(x=70,y=230)
        chosen_gender= StringVar()
        #chosen_gender.set('F')
        drop= OptionMenu(base, chosen_gender, *gen)
        drop.place(x=235,y=230, width=100)
          
        labl_4 = Label(base, text="Age:",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_4.place(x=70,y=280)  

        entry_04 = Entry(base)  
        entry_04.place(x=240,y=280) 

        labl_5 = Label(base, text="Plate_NO:",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_5.place(x=70,y=330)

        entry_05 = Entry(base)  
        entry_05.place(x=240,y=330)


        labl_6 = Label(base, text="State:",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_6.place(x=70,y=380)

        entry_06 = Entry(base)  
        entry_06.place(x=240,y=380)

        labl_7 = Label(base, text="Money:",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_7.place(x=70,y=430)

        entry_07 = Entry(base)  
        entry_07.place(x=240,y=430)

        labl_8 = Label(base, text="Type:",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_8.place(x=70,y=480)
        chosen_type= StringVar()
        #chosen_type.set('2-wheeler')
        drop= OptionMenu(base, chosen_type, *typel)
        drop.place(x=235,y=480, width=100)


        labl_9 = Label(base, text="Password:",width=20,bg='#6FABB7',font=("bold", 10))  
        labl_9.place(x=70,y=530)

        entry_09 = Entry(base,show="*")  
        entry_09.place(x=240,y=530)
        button_font = font.Font(family='Helvitica', size=15)
        Button(base, text='Submit',width=20,bg='#190380',fg='white',bd=0,font=button_font,command = submitact).place(relx=0.9, rely=0.9, anchor=SE)  
        base.mainloop()
#register()
