from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import random
from tkcalendar import DateEntry
from datetime import datetime
import mysql.connector


#replace the password with your own and
#change the file location too


def main():
    win=Tk()
    app=main_window(win)
    win.mainloop()
    
    
    

class main_window:
    def __init__(self,root):
        self.root=root
        self.root.title("CAB BOOKING MANAGEMENT SYSTEM")
        self.root.geometry("1600x900+0+0")

        self.txtReceipt1=StringVar()
        self.txtReceipt2=StringVar()
        

        

        #Add image file
        self.img = ImageTk.PhotoImage(file=r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\cab.jpeg")

        #create canvas
        canvas=Canvas(self.root,width=500,height=500)
        canvas.pack(fill=BOTH, expand=True)

        #Display image using create_image
        canvas.create_image(0,0,image=self.img,anchor='nw')

        Login_frame=Frame(self.root,bg='black')
        Login_frame.place(x=550,y=170,height=400,width=350)

        welcome_frame=Frame(self.root,bg="black")
        welcome_frame.place(x=350,y=60,width=800,height=70)

        self.logo=ImageTk.PhotoImage(file=r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\logo.png")
        canvas_logo=Canvas(welcome_frame,width=10,height=10,bg="black")
        canvas_logo.pack(fill=BOTH, expand=True)
        canvas_logo.create_image(35,10,image=self.logo,anchor='nw')


        welcome_label=Label(welcome_frame,text="WELCOME TO OLA CAB SERVICES!!",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label.place(x=100,y=10)

        login_img=Image.open(r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\login.png")
        resized_login_img=login_img.resize((45,45),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(resized_login_img)

        lab=Label(Login_frame,image=self.img1,bg="black")
        lab.place(x=15,y=15)


        login_label=Label(Login_frame,text="LOGIN HERE",font=("comic sans MS","22","bold"),fg="red",bg="black")
        login_label.place(x=75,y=15)

        #username label
        username_label=Label(Login_frame,text="USERNAME",font=("GOUDY OLD STYLE","15"),fg="white",bg="black")
        username_label.place(x=25 ,y=90)

        #entry for getting the username from the user
        self.username_entry=Entry(Login_frame,font=("times new roman","12","bold"),bg="lightgray")
        self.username_entry.place(x=25,y=125,width=270,height=25)

        #password label
        password_label=Label(Login_frame,text="PASSWORD",font=("GOUDY OLD STYLE","15"),fg="white",bg="black")
        password_label.place(x=25 ,y=190)

        #entry for getting password from the user
        self.password_entry=Entry(Login_frame,font=("times new roman","12","bold"),bg="lightgray",show="*")
        self.password_entry.place(x=25,y=225,width=270,height=25)

        btn1=Button(Login_frame,text="FORGOT PASSWORD?",cursor="hand2",font=("calibri","10"),bg="black",fg="white",bd=0,command=self.forgot_password_window)
        btn1.place(x=35,y=340)

        btn2=Button(Login_frame,text="Login",cursor="hand2",font=("times new roman","10"),bg="grey",fg="black",bd=0,width=15,height=1,command=self.login)
        btn2.place(x=100,y=300)

        btn3=Button(Login_frame,text="NOT REGISTERED? REGISTER",cursor="hand2",font=("calibri","10"),bg="black",fg="white",bd=0,command=self.register_window)
        btn3.place(x=35,y=360)

    def register_window(self):
        self.new_window=Toplevel()
        self.app=Register(self.new_window)


# ========================================================================================================================
# =================================================LOGIN DATA=============================================================
# ========================================================================================================================
    def login(self):
        if self.username_entry.get()=='' or self.password_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required')

        else:
            
            mydb=mysql.connector.connect(host='localhost',user='root',password='pass123',database='cab_booking')
        
            mycursor=mydb.cursor()
            mycursor.execute('select * from user where username= %s and password= %s',(
                                                                                    self.username_entry.get(),
                                                                                    self.password_entry.get()
                                                                                    ))
            row=mycursor.fetchone()

            
            if row==None:
                messagebox.showerror('Error','Invalid Username And Password')
                

            else:
                
                mydb.commit()
                mydb.close()
                messagebox.showinfo('Success','WELCOME TO CAB SERVICES')
                self.from_drop()



# ========================================================================================================================
# =================================================RESET PASSWORD=============================================================
# ========================================================================================================================
    def reset_password(self):
        if self.new_password_entry.get()=='' or self.new_confirm_password_entry.get() :
            messagebox.showerror('Error','All Fields Are Required')
        elif self.new_password_entry.get()!=self.new_confirm_password_entry.get():
            messagebox.showerror('Error','Password Does Not Match')

        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='pass123',database='cab_booking')
            mycursor=mydb.cursor()
            query=('select * from user where username=%s')
            value=(self.username_entry.get())
            mydb._execute(query,value)
            row=mydb.fetchone()
            query=('update user set password=%s where username=%s')
            value=(self.new_password_entry.get(),self.username_entry.get())
            mydb.execute(query,value)
            mydb.commit()
            mydb.close()
            messagebox.showinfo('Successful','Your Password Has Been Reset,Please Login Again')

        

# ========================================================================================================================
# =================================================FORGOT PASSWORD=============================================================
# ========================================================================================================================
    def forgot_password_window(self):
        self.var_password_entry=StringVar()
        self.var_new_password_entry=StringVar()
        self.var_confirm_password_entry=StringVar()

        
        if self.username_entry.get()=='':
            messagebox.showerror('Error','Please Enter Valid Username')
        else:
            mydb=mysql.connector.connect(host='localhost',user='root',password='pass123',database='cab_booking')
            mycursor=mydb.cursor()
            query=('select * from user where username = %s')
            value=(self.username_entry.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror('Error','Invalid Username')

            else:
                mydb.close()
                self.root2=Toplevel()
                self.root2.title('Forgot Password')
                self.root2.geometry('340x450+610+170')

                self.root2['bg']='black'
                l=Label(self.root2,text='Forgot Password',font=("comic sans MS","22","bold"),fg="red",bg='black')
                l.place(x=0,y=10,relwidth=1)
                self.new_password_label=Label(self.root2,text='NEW PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=80)
                self.new_password_entry=Entry(self.root2,font=("times new roman","12","bold"),bg="lightgray",textvariable=self.var_new_password_entry,show="*")
                self.new_password_entry.place(x=25,y=110,width=300,height=25)
                self.new_confirm_password_label=Label(self.root2,text='CONFIRM PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=140)
                self.new_confirm_password_entry=Entry(self.root2,font=("times new roman","12","bold"),bg="lightgray",textvariable=self.var_confirm_password_entry,show="*")
                self.new_confirm_password_entry.place(x=25,y=170,width=300,height=25)
                self.submit_button=Button(self.root2,text="SUBMIT",cursor="hand2",font=("times new roman","10"),bg="grey",fg="black",bd=0,width=15,height=2,command=self.reset_password).place(x=100,y=250)


# ========================================================================================================================
# =================================================FROM DROP=============================================================
# ========================================================================================================================    

    def from_drop(self):

        self.root=Toplevel(self.root)
        self.root.title("Search Cabs")
        self.root.geometry("1600x900+0+0")

 
        self.var_from_entry=StringVar()
        self.var_drop_entry=StringVar()
        self.var_date_entry=IntVar()
        self.ac_check=IntVar()
        self.var_check1=IntVar()
        self.var_check2=IntVar()
        self.var_check3=IntVar()
        self.var1 = IntVar()
        self.tip_price=IntVar()
       
        
        
        
       #Add image file
        self.cabs_bg = ImageTk.PhotoImage(file=r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\cab.jpeg")

        #create canvas
        canvas=Canvas(self.root,width=500,height=500)
        canvas.pack(fill=BOTH, expand=True)

        #Display image using create_image
        canvas.create_image(0,0,image=self.cabs_bg,anchor='nw')

        self.cabs_frame=Frame(self.root,bg="khaki1")
        self.cabs_frame.place(x=500,y=0,width=925,height=485)

        self.cabs_frame1=Frame(self.root,bg="khaki1")
        self.cabs_frame1.place(x=1100,y=600,width=320,height=180)

        


        self.cab_frame=Frame(self.root,bg="khaki1")
        self.cab_frame.place(x=70,y=200,width=350,height=400)

        L1=Label(self.cab_frame,text="Your everyday travel partner",font=("ariel","15","bold"),fg="black",bg="white")
        L1.place(x=40,y=10)

        L2=Label(self.cab_frame,text="AC cabs for point to point travel",font=("calibri","12"),fg="black",bg="white")
        L2.place(x=70,y=50)

        self.L3=Label(self.cab_frame,text="PICK UP :",font=("calibri","12",'bold'),fg="black",bg="white")
        self.L3.place(x=20,y=80)

        options1=['select','mumbai','pune','nashik']
        self.L3_combo=ttk.Combobox(self.cab_frame,value=options1,textvariable=self.var_from_entry,state='readonly')
        self.L3_combo.place(x=20,y=110,width=300,height=35)
        self.L3_combo.current(0)

        self.L4=Label(self.cab_frame,text="DROP:",font=("calibri","12","bold"),fg="black",bg="white")
        self.L4.place(x=20,y=170)

        options2=['select','mumbai','pune','nashik']
        self.L4_combo=ttk.Combobox(self.cab_frame,value=options2,textvariable=self.var_drop_entry,state='readonly')
        self.L4_combo.place(x=20,y=200,width=300,height=35)
        self.L4_combo.current(0)

        self.L5=Label(self.cab_frame,text="WHEN:",font=("calibri","12","bold"),fg="black",bg="white")
        self.L5.place(x=20,y=240)
        self.cal_frame=Frame(self.root,bg="black",borderwidth=1)
        self.cal_frame.place(x=90,y=470,width=300,height=35)
        self.today=datetime.now()
        self.cal = DateEntry(self.cal_frame,mindate=self.today,width=12,height=2,disabledbackground="olivedrab2" ,bordercolor='black',date_pattern='yyyy/mm/dd',headersbackground= 'olivedrab2',bd=3,Variable=self.var_date_entry)
        self.cal.place(x=5,y=5,width=285,height=20)
        
        search_btn=Button(self.cabs_frame1,text="BOOK MY CAB",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.from_drop_data)
        search_btn.place(x=30,y=20)

        logout_btn=Button(self.cabs_frame1,text="LOG OUT",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.root.destroy)
        logout_btn.place(x=30,y=120)


        

        self.cab1=Image.open("cab1.png")
        self.cab_1=ImageTk.PhotoImage(self.cab1)
        cab_btn1=Button(self.cabs_frame,image=self.cab_1)
        cab_btn1.place(x=35,y=35)
        self.cab2=Image.open("cab2.png")
        self.cab_2=ImageTk.PhotoImage(self.cab2)
        cab_btn2=Button(self.cabs_frame,image=self.cab_2)
        cab_btn2.place(x=335,y=35)
        self.cab3=Image.open("cab3.png")
        self.cab_3=ImageTk.PhotoImage(self.cab3)
        cab_btn3=Button(self.cabs_frame,image=self.cab_3)
        cab_btn3.place(x=635,y=35)
        self.cab4=Image.open("cab4.png")
        self.cab_4=ImageTk.PhotoImage(self.cab4)
        cab_btn4=Button(self.cabs_frame,image=self.cab_4)
        cab_btn4.place(x=35,y=265)
        self.cab5=Image.open("cab5.png")
        self.cab_5=ImageTk.PhotoImage(self.cab5)
        cab_btn5=Button(self.cabs_frame,image=self.cab_5)
        cab_btn5.place(x=335,y=265)
        self.cab6=Image.open("cab6.png")
        self.cab_6=ImageTk.PhotoImage(self.cab6)
        cab_btn6=Button(self.cabs_frame,image=self.cab_6)
        cab_btn6.place(x=635,y=265)

        
        
        self.R1 = Radiobutton(self.cabs_frame, text="OLA MINI", variable=self.var1, value=1)
        self.R1.place(x=35,y=35)
        self.R2 = Radiobutton(self.cabs_frame, text="OLA PRIME SUDON", variable=self.var1, value=2)
        self.R2.place(x=335,y=35)
        self.R3 = Radiobutton(self.cabs_frame, text="OLA SUX", variable=self.var1, value=3)
        self.R3.place(x=635,y=35)
        self.R4 = Radiobutton(self.cabs_frame, text="AUTO", variable=self.var1, value=4)
        self.R4.place(x=35,y=265)
        self.R5 = Radiobutton(self.cabs_frame, text="E-AUTO", variable=self.var1, value=5)
        self.R5.place(x=335,y=265)
        self.R6 = Radiobutton(self.cabs_frame, text="OLA SUV", variable=self.var1, value=6)
        self.R6.place(x=635,y=265)

        self.fare_frame=Frame(self.root,bg="khaki1")
        self.fare_frame.place(x=500,y=600,width=550,height=180)
        self.radio_1=IntVar()
        self.radio_3=IntVar()
        self.checkbox1=Checkbutton(self.fare_frame,text="AC",variable=self.var_check1,onvalue=1,offvalue=0,bg="khaki1",fg="black",command=self.hi(),font=("times new roman","15","bold"))
        self.checkbox1.place(x=20,y=30)
        self.checkbox2=Checkbutton(self.fare_frame,text="OLA PLAY",variable=self.var_check2,onvalue=1,offvalue=0,bg="khaki1",fg="black",command=self.hi(),font=("times new roman","15","bold"))
        self.checkbox2.place(x=20,y=80)
        self.checkbox3=Checkbutton(self.fare_frame,text='EXTRA LUGGAGE',variable=self.var_check3,onvalue=1,offvalue=0,bg="khaki1",fg="black",command=self.hi(),font=("times new roman","15","bold"))
        self.checkbox3.place(x=20,y=130)
 
        self.fare_tip_label=Label(self.fare_frame,text="TIP:",font=("times new roman","15","bold"),fg="black",bg="khaki1")
        self.fare_tip_label.place(x=250,y=130)

        self.fare_tip_entry=Entry(self.fare_frame,font=("times new roman","12"),bg="white",bd=1)
        self.fare_tip_entry.place(x=300,y=130,width=200,height=40)

        
        self.fare_button1=Button(self.cabs_frame1,text="GENERATE RECEIPT",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.Receiptt)
        self.fare_button1.place(x=30,y=70)


    def cabtypefun(self):

        self.radiobtn_var= self.var1.get()

        if self.radiobtn_var==1:
            self.sqlcabtype= 'Ola Mini'

        if self.radiobtn_var==2:
            self.sqlcabtype= 'Ola Prime Sudon'
        if self.radiobtn_var==3:
            self.sqlcabtype= 'Ola SUX'
        if self.radiobtn_var==4:
            self.sqlcabtype= 'auto'

        if self.radiobtn_var==5:
            self.sqlcabtype= 'e-auto'

        if self.radiobtn_var==6:
            self.sqlcabtype= 'ola suv'


        return self.sqlcabtype

    def hi(self):
        self.take1=self.var_check1.get()
        self.take2=self.var_check2.get()
        self.take3=self.var_check3.get()
        
        self.fare_sum=0
        if self.take1==1:
            self.fare_sum+=100
             
        if self.take2==1:
            self.fare_sum+=150
    
        if self.take3==1:
            self.fare_sum+=200


        return str(self.fare_sum)

    def sumoffare(self):
        self.total=self.fare_sum+int(self.fare_tip_entry.get())+int(self.from_to_fare())
        return self.total



    def ac(self):
        if self.var_check1.get()==1:
            self.varcheck1="AC"
          
            return self.varcheck1
        else:
            self.varcheck1='NON AC'
            return self.varcheck1
    def olaplay(self):
        if self.var_check2.get()==1:
            self.varcheck2="OLA PLAY"
            return self.varcheck2
        else:
            self.varcheck2='NO OLA PLAY'
            return self.varcheck2
    def extra_luggage(self):
        if self.var_check3.get()==1:
            self.varcheck3="EXTRA LUGGAGE"
            return self.varcheck3
        else:
            self.varcheck3='NO EXTRA LUGGAGE'
            return self.varcheck3


    def from_to_fare(self):


        if self.L3_combo.get()=='mumbai' and self.L4_combo.get()=='pune':
            # km1=5
            
            return 250

        if self.L3_combo.get()=='mumbai' and self.L4_combo.get()=='nashik':
            # km1=7
            
            return 350

        if self.L3_combo.get()=='pune' and self.L4_combo.get()=='nashik':
            # km1=10
            
            return 500
        
        if self.L3_combo.get()=='pune' and self.L4_combo.get()=='mumbai':
            # km1=10
            
            return 500

        if self.L3_combo.get()=='nashik' and self.L4_combo.get()=='mumbai':
            # km1=7
            
            return 350

        if self.L3_combo.get()=='nashik' and self.L4_combo.get()=='pune':
            # km1=10
            
            return 500


    def Receiptt(self):
    
        self.root=Toplevel(self.root)
        self.root.title("Receipt")
        self.root.geometry("350x450")

        self.txtReceipt1=StringVar()
        self.txtReceipt2=StringVar()
        self.Receipt_Ref=StringVar()

        self.ReceiptFrame=Frame(self.root,bg='khaki1')
        self.ReceiptFrame.place(x=0,y=0,height=450,width=450)

        welcome_label1=Label(self.ReceiptFrame,text="Receipt",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label1.place(x=100,y=10)

        self.txtReceipt1 = Text(self.ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0,bg="khaki1")
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)

        self.txtReceipt2 = Text(self.ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0,bg="khaki1")
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)

        self.txtReceipt1.delete("1.0",END)
        self.txtReceipt2.delete("1.0",END)
        x=random.randint(10853,500831)
        randomRef = str(x)
        self.Receipt_Ref.set(randomRef)
        self.txtReceipt1.insert(END,"RECEIPT NUMBER:\n")
        self.txtReceipt2.insert(END, self.Receipt_Ref.get() + "\n")
        self.txtReceipt1.insert(END,"USERNAME:\n")
        self.txtReceipt2.insert(END, self.username_entry.get() + "\n")
        self.txtReceipt1.insert(END,'FROM:\n')
        self.txtReceipt2.insert(END, self.L3_combo.get() + "\n")
        self.txtReceipt1.insert(END,'TO:\n')
        self.txtReceipt2.insert(END, self.L4_combo.get() + " \n")
        self.txtReceipt1.insert(END,'DATE:\n')
        self.txtReceipt2.insert(END, self.cal.get() + "\n")
        self.txtReceipt1.insert(END,'CABTYPE:\n')
        self.txtReceipt2.insert(END, self.cabtypefun() + "\n")
        self.txtReceipt1.insert(END,'AC?:\n')
        self.txtReceipt2.insert(END, self.ac() + "\n")
        self.txtReceipt1.insert(END,'OLA PLAY?:\n')
        self.txtReceipt2.insert(END, self.olaplay() + "\n")
        self.txtReceipt1.insert(END,'EXTRA LUGGAGE?:\n')
        self.txtReceipt2.insert(END, self.extra_luggage() + "\n")
        self.txtReceipt1.insert(END,'EXTRA FARE:\n')
        self.txtReceipt2.insert(END, self.hi() + "\n")
        self.txtReceipt1.insert(END,'TIP:\n')
        self.txtReceipt2.insert(END, str(self.fare_tip_entry.get()) + "\n")
        self.txtReceipt1.insert(END,'FARE:\n')
        self.txtReceipt2.insert(END, str(self.from_to_fare()) + "\n")
        self.txtReceipt1.insert(END,'TOTAL AMOUNT:\n')
        self.txtReceipt2.insert(END, str(self.sumoffare()) + "\n")
        

# ========================================================================================================================
# =================================================FROM DROP DATA=============================================================
# ========================================================================================================================
    def from_drop_data(self):

        if self.L3_combo.get()=='' or self.L4_combo.get()=='':
            messagebox.showerror('Error','All fields are required')

        if self.L3_combo.get()=='select' or self.L4_combo.get()=='select':
            messagebox.showerror('Error','Please select your cities')

        if self.L3_combo.get()=='mumbai' and self.L4_combo.get()=='mumbai':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')

        if self.L3_combo.get()=='pune' and self.L4_combo.get()=='pune':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')
        
        if self.L3_combo.get()=='nashik' and self.L4_combo.get()=='nashik':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')

        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='pass123',database='cab_booking')
                print(mydb)

            
                mycursor=mydb.cursor()
                mycursor.execute("insert into cab(username,user_from,user_to,user_date,cabtype,fare,tip,ac,ola_play,extra_luggage,base_fare,total)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                 [self.username_entry.get(),self.L3_combo.get(),self.L4_combo.get(),self.cal.get(),self.cabtypefun(),self.hi(),
                                 self.fare_tip_entry.get(),self.ac(),self.olaplay(),self.extra_luggage(),self.from_to_fare(),self.sumoffare()]
                                  )
                mydb.commit()
                mydb.close()
                messagebox.showinfo('Success',"BOOKING SUCCESSFUL, ENJOY YOUR RIDE!!",parent=self.root)
                

            except Exception as es:
                messagebox.showerror('Error',f'Error due to: {str(es)}',parent=self.root)






class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #===================variables=============================

        self.var_email_entry=StringVar()
        self.var_username_entry=StringVar()
        self.var_password_entry=StringVar()
        self.var_new_password_entry=StringVar()
        self.var_confirm_password_entry=StringVar()
        self.var_check=IntVar()
        
        #=================bgimage=================================

        #Add image file
        self.img2 = ImageTk.PhotoImage(file=r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\cab.jpeg")

        #create canvas
        canvas2=Canvas(self.root,width=500,height=500)
        canvas2.pack(fill=BOTH, expand=True)

        #Display image using create_image
        canvas2.create_image(0,0,image=self.img2,anchor='nw')

        Login_frame2=Frame(self.root,bg='black')
        Login_frame2.place(x=550,y=170,height=400,width=350)

        Welcome_frame2=Frame(self.root,bg="black")
        Welcome_frame2.place(x=350,y=60,width=800,height=70)

        self.logo2=ImageTk.PhotoImage(file=r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\logo.png")
        canvas_logo2=Canvas(Welcome_frame2,width=10,height=10,bg="black")
        canvas_logo2.pack(fill=BOTH, expand=True)
        canvas_logo2.create_image(35,10,image=self.logo2,anchor='nw')


        welcome_label=Label(Welcome_frame2,text="WELCOME TO OLA CAB SERVICES!!",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label.place(x=100,y=10)

        login_img2=Image.open(r"C:\Users\Sushil\OneDrive\Desktop\sid\python files\cab\logo.png")
        resized_login_img=login_img2.resize((45,45),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(resized_login_img)

        self.Login_frame2=Frame(self.root,bg='black')
        self.Login_frame2.place(x=510,y=170,height=450,width=400)
        reg_btn=Label(self.Login_frame2,text="REGISTER",font=("comic sans MS","22","bold"),fg="red",bg="black")
        reg_btn.place(x=65 ,y=15)

        #=====================label and entry==============================
        self.email_label=Label(self.Login_frame2,text='EMAIL',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=70)
        self.email_entry=Entry(self.Login_frame2,textvariable=self.var_email_entry,font=("times new roman","12","bold"),bg="lightgray")
        self.email_entry.place(x=25,y=100,width=300,height=25)
        self.username_label=Label(self.Login_frame2,text='USERNAME',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=140)
        self.username_entry=Entry(self.Login_frame2,textvariable=self.var_username_entry,font=("times new roman","12","bold"),bg="lightgray")
        self.username_entry.place(x=25,y=170,width=300,height=25)
        self.password_label=Label(self.Login_frame2,text='PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=210)
        self.password_entry=Entry(self.Login_frame2,textvariable=self.var_password_entry,font=("times new roman","12","bold"),bg="lightgray",show="*")
        self.password_entry.place(x=25,y=240,width=300,height=25)
        self.confirm_password_label=Label(self.Login_frame2,text='CONFIRM PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25,y=280)
        self.confirm_password_entry=Entry(self.Login_frame2,textvariable=self.var_confirm_password_entry,font=("times new roman","10","bold"),bg="lightgray",show="*")
        self.confirm_password_entry.place(x=25,y=310,width=300,height=25)
        #==========================checkbtn==============================
        self.checkbox=Checkbutton(self.Login_frame2,text='I Agree To Your Terms And Conditions ',variable=self.var_check,onvalue=1,offvalue=0,bg="black",fg="red",font=("times new roman","10","bold"))
        self.checkbox.place(x=25,y=350)
        #==========================btn=====================================
        self.register_button=Button(self.Login_frame2,command=self.register_data,text="REGISTER",cursor="hand2",font=("times new roman","10"),bg="grey",fg="black",bd=0,width=15,height=1).place(x=130,y=380)
        self.logg=Button(self.Login_frame2,text="click here to go back to login page",cursor="hand2",font=("calibri","10"),bg="black",fg="white",bd=0,command=self.login_window).place(x=90,y=410)


# ========================================================================================================================
# =================================================REGISTER DATA=============================================================
# ========================================================================================================================
    def register_data(self):
        if self.var_email_entry.get()=="" or self.var_username_entry.get()=="" or self.var_password_entry.get()=="" or self.var_confirm_password_entry.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password_entry.get()!= self.var_confirm_password_entry.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',password='jpass123',database='cab_booking')
                print(mydb)

                mycursor=mydb.cursor()
                user_verification = self.var_email_entry.get()
                sql="select * from user where emailid = %s"
                mycursor.execute(sql,[user_verification])
                row=mycursor.fetchone()
                print(row)
                if row!=None:
                    messagebox.showinfo('Error','User already exists,try using another email',parent=self.root)
                else:
                    mycursor.execute("insert into user(emailid,username,password)values(%s,%s,%s)",
                                     (self.var_email_entry.get(),
                                      self.var_username_entry.get(),
                                      self.var_password_entry.get()
                                      ))
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo('Success','REGISTRATION SUCCESSFUL',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Error due to: {str(es)}',parent=self.root)

    def login_window(self):
        self.new_window3=Toplevel(self.root)
        self.app=main_window(self.new_window3)



if __name__=="__main__":
    main()
    
