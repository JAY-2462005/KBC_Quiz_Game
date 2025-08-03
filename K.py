from tkinter import *
import csv
from tkinter import messagebox
a=Tk()

def onclick(d,b,c):
    with open('USER_INFO.csv' , 'r') as f2:
        reader = csv.reader(f2)

        if [d,b] in reader:
            messagebox.showerror(message='LOGIN LIMIT EXCEEDED')
        else:
            with open('USER_INFO.csv' , 'a' , newline='') as f1:
                writer = csv.writer(f1)
                writer.writerow([d,b])

                import main



a.title("Welcome to KBC")
window_width,window_height=500,500
screen_width=a.winfo_screenwidth()
screen_height=a.winfo_screenheight()
position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)
a.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
loginImage=PhotoImage(file="center.png")
bgImage=Label(a,image=loginImage,bg="black")
bgImage.place(relheight=1,relwidth=1)
user_name_label = Label(a , text='Name :',bg="black",fg="white",font=("Arial",20,"bold"))
user_PRN_label = Label(a , text='PRN :',bg="black",fg="white",font=("Arial",20,"bold"))
user_name_label.place(x=150,y=350)
user_PRN_label.place(x=150,y=400)
user_name = Entry(a)
user_name.place(x=250,y=360)
user_PRN = Entry(a)
user_PRN.place(x=250,y=410)
user_login=Label(a,text="User Login",font=("Georgia",40,"bold"),bg="black",fg="white")
user_login.place(x=100,y=60)
user_submit =Button(a , text='Submit' , command= lambda :onclick(user_name.get() , user_PRN.get(),a.destroy()),bg="black",fg="white",
                    font=("Arial",20,"bold"),activebackground="black",activeforeground="white",bd=0)
user_submit.place(x=200,y=450)

a.mainloop()

