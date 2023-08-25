import tkinter as tk
import re
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect("example.db")


top = tk.Tk()
top.geometry("300x300")

def savetext():
     entered_text = user_name.get()
     pattern=r'@gmail\.com$'
     if re.search(pattern,entered_text):
         print(entered_text)
         message_label.config(text="")
     else:
          message_label.config(text="Invalid Email Address",fg="red")
          

l1=tk.Label(top,text="username:")
l1.grid(row=0,column=0)
user_name=tk.Entry(top)
user_name.grid(row=0,column=1)

message_label=tk.Label(top,text="",fg="black")
message_label.grid(row=1,column=1)

l1=tk.Label(top,text="password:")
l1.grid(row=2,column=0)
password=tk.Entry(top,show="*")
password.grid(row=2,column=1)

redirect_page=tk.Label(top,text="Forget Password",fg="blue")
redirect_page.grid(row=3,column=1)

create_new_window=tk.Toplevel(top)
create_new_window.geometry("300x300")
create_new_window.withdraw()

def go_back(event):
     top.withdraw()
     create_new_window.deiconify()
     l1=tk.Label(create_new_window,text="Enter your email_id or phone number to search \nfor your account")
     l1.grid(row=0,column=0)
     l2=tk.Entry(create_new_window,text="Enter here")
     l2.grid(row=1,column=0)
     
     
redirect_page.bind("<Button-1>",go_back)

l3=tk.Button(top,text="login",command=savetext)
l3.grid(row=4,column=1)
top.mainloop()



