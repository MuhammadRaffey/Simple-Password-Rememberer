from os import write
import tkinter as tk
from tkinter import *
from tkinter.constants import END
s=tk.Tk()
s.geometry("500x280")
s.title("Password Rememberer")
s.configure(bg="#00FFFF")

#icon
s.iconbitmap('iconn.ico')
i=tk.Label(s,text="Enter name of your account",bg="#FF002B",fg="#FFFB00")
i.place(x=190,y=55)
Name= tk.Entry(s,width=50,background="yellow")
Name.place(x=140,y=80)
Name.insert(0,"enter your Name")

Username=tk.Entry(s,width=50,background="yellow")
Username.place(x=140,y=100)
Username.insert(0,"enter your Username")

Password=tk.Entry(s,width=50,background="yellow")
Password.place(x=140,y=120)
Password.insert(0,"enter your Password")

if "enter your Name" in Name.get():
    def remove_shit():
        Name.delete(0,END)
    Name.after(2000,remove_shit)
if "enter your Username" in Username.get():
    def remove_shit3():
        Username.delete(0,END)
    Username.after(2000,remove_shit3)
if "enter your Password" in Password.get():
    def remove_shit2():
        Password.delete(0,END)
    Password.after(2000,remove_shit2)



class Save():
    def ss():
        
        save=open("Passwords.txt",'a')
        ray=open("Passwords.txt",'r')
        rau=ray.read()
        if "List of your Passwords is down below" in rau:
            save.write('\n'+Name.get()+" "+Username.get()+" "+Password.get())
        else:
            save.write("List of your Passwords is down below")
            save.write('\n'+Name.get()+" "+Username.get()+" "+Password.get())

    
    pasbut=tk.Button(s,text="Save",command=ss,bg="#FF002B",fg="#FFFB00")
    pasbut.place(x=240,y=185)
    
def ref():
    Name.delete(0,END)
    Username.delete(0,END)
    Password.delete(0,END)

ref_but=tk.Button(s,text="Refresh",bg="#FF002B",fg="#FFFB00",command=ref)
ref_but.place(x=230,y=215)


def exe():
    s.quit()
exit_butt=tk.Button(s,text="Exit",command=exe,bg='#FF002B',fg='#FFFB00')
exit_butt.place(x=240,y=250)
s.mainloop()

