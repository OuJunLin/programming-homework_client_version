import socket
import time
import threading
from tkinter import *
from tkinter import messagebox
import time



def create_create_account_window(sock, create_account_window):
    create_account_window.title("create account")
    create_account_window.geometry("400x250+750+400")
    for i in range(4):
        create_account_window.rowconfigure(i, weight=1)
    for i in range(3):
        create_account_window.columnconfigure(i, weight=1)



    lab = Label(create_account_window, text="please enter the\n new account and new password",justify="left", font="Arial 12 bold")
    lab.grid(row=0, column=0, columnspan=2, sticky=S)

    lab1 = Label(create_account_window, text="new account: ")
    lab1.grid(row=1, column=0, sticky=SE)

    lab2 = Label(create_account_window, text="new password: ")
    lab2.grid(row=2, column=0, sticky=E)

    in1 = Entry(create_account_window, width=15)
    in1.grid(row=1, column=1, sticky=SW)

    in2 = Entry(create_account_window, width=15, show="*")
    in2.grid(row=2, column=1, sticky=W)

    fr1 = Frame(create_account_window)
    fr1.grid(row=3, column=0, columnspan=3, sticky=N+S+W+E)
    
    
    
    def send_new_account():
        newaccount = in1.get()
        newpassword = in2.get()
        newuser_data = ("newaccount", newaccount, newpassword)
        if len(newaccount)!=0 and len(newpassword)!=0:
            sock.send(str(newuser_data).encode("utf-8"))
            check_result_nc = sock.recv(1024).decode("utf-8")
            if check_result_nc == "alreadly create new account":
                messagebox.showinfo("create !", "the new account is alreadly created!!!")
                create_account_window.destroy()
            elif check_result_nc == "same account in db":
                messagebox.showwarning("Warning !", "Warning, there is the same account in database !!!")
        else:
            messagebox.showerror("Error !", "no input !!!")



    btn1 = Button(fr1, text="return", height=2, bg="#ffffff", command=lambda:create_account_window.destroy())
    btn1.pack(side="right", padx=20)

    btn2 = Button(fr1, text="create\naccount", bg="#ffffff", command=send_new_account)
    btn2.pack(side="right", padx=20)



