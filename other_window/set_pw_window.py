from tkinter import messagebox
from tkinter import *
import time



def create_set_pw_window(sock, set_pw_window):
    set_pw_window.title("set_pw_window")
    set_pw_window.geometry("400x300+750+400")

    for i in range(4):
        set_pw_window.rowconfigure(i, weight=1)
    for i in range(3):
        set_pw_window.columnconfigure(i, weight=1)
    
    
    
    def exit():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            set_pw_window.destroy()
    
    
    
    def btn2Fun():
        password = in1.get()
        newpassword = in2.get()
        if len(password)!=0 and len(newpassword)!=0:
            sock.send("00008".encode("utf-8"))
            time.sleep(0.2)
            data = (password, newpassword)
            sock.send(str(data).encode("utf-8"))
            check_result = sock.recv(1024).decode("utf-8")
            print(check_result)
            if check_result == "change password":
                messagebox.showinfo("Successfully!", "You successfully change your password !!!")
                set_pw_window.destroy()
            else:
                messagebox.showwarning("Error!", "Error password !!!")
        else:
            messagebox.showerror("Error", "You don't input any name !!!")
        


    lab = Label(set_pw_window, text="Please enter the original \npassword and new password",justify="left", font="Arial 12 bold")
    lab.grid(row=0, column=0, columnspan=2, sticky=S)

    lab1 = Label(set_pw_window, text="password: ")
    lab1.grid(row=1, column=0, sticky=SE)

    lab2 = Label(set_pw_window, text="new password: ")
    lab2.grid(row=2, column=0, sticky=E)

    in1 = Entry(set_pw_window, width=15)
    in1.grid(row=1, column=1, sticky=SW)

    in2 = Entry(set_pw_window, width=15, show="*")
    in2.grid(row=2, column=1, sticky=W)

    fr1 = Frame(set_pw_window)
    fr1.grid(row=3, column=0, columnspan=3, sticky=N+S+W+E)

    btn1 = Button(fr1, text="return", height=2, bg="#ffffff", command=exit)
    btn1.pack(side="right", padx=20)

    btn2 = Button(fr1, text="set\npassword", bg="#ffffff", command=btn2Fun)
    btn2.pack(side="right", padx=20)



