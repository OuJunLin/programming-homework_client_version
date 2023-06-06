import socket
import time
import threading
from tkinter import *
from tkinter import messagebox
import time




def create_login_window(sock, login_window, return_window):
    login_window.title("login")
    login_window.geometry("400x250+750+400")
    for i in range(4):
        login_window.rowconfigure(i, weight=1)
    for i in range(3):
        login_window.columnconfigure(i, weight=1)



    lab = Label(login_window, text="The connection is successful,\n please enter the account and password",justify="left", font="Arial 12 bold")
    lab.grid(row=0, column=0, columnspan=2, sticky=S)

    lab1 = Label(login_window, text="account: ")
    lab1.grid(row=1, column=0, sticky=SE)

    lab2 = Label(login_window, text="password: ")
    lab2.grid(row=2, column=0, sticky=E)

    in1 = Entry(login_window, width=15)
    in1.grid(row=1, column=1, sticky=SW)

    in2 = Entry(login_window, width=15, show="*")
    in2.grid(row=2, column=1, sticky=W)

    fr1 = Frame(login_window)
    fr1.grid(row=3, column=0, columnspan=3, sticky=N+S+W+E)
    
    
    
    def send_password():
        account = in1.get()
        password = in2.get()
        user_data = (account, password)
        if len(account)!=0 and len(password)!=0:
            sock.send(str(user_data).encode("utf-8"))
            check_result = sock.recv(1024).decode("utf-8")
            if check_result == "correct password":
                print(check_result)#!!!
            elif check_result=="error password" or check_result=="no account":
                messagebox.showwarning("warning !", "Warning, if you enter the wrong password three times,\n you will be disconnected by the server !!!")
            elif check_result=="881":
                messagebox.showerror("Error !", "You have been disconnected by the server !!!")
                login_window.destroy()
        else:
            messagebox.showerror("Error !", "no input !!!")



    btn1 = Button(fr1, text="login", height=2, bg="#ffffff", command=send_password)
    btn1.pack(side="right", padx=20)

    btn2 = Button(fr1, text="create\naccount", bg="#ffffff")
    btn2.pack(side="right", padx=20)



