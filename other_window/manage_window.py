from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import time



def create_manage_window(sock, manage_window):
    manage_window.title("set_pw_window")
    manage_window.geometry("900x600+700+300")
    
    
    
    def exit():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            manage_window.destroy()
    
    
    
    def btn1Fun():
        content1.config(state="normal")
        content1.delete(1.0, END)
        content1.config(state="disabled")
        sock.send("00009".encode("utf-8"))
        user_name_list = eval(sock.recv(1024).decode("utf-8"))
        for name in user_name_list:
            content1.config(state="normal")
            content1.insert(INSERT, name+"\n")
            content1.config(state="disabled")
    
    
    
    def btn2Fun():
        user_name = in1.get()
        if len(user_name) != 0:
            content1.config(state="normal")
            content1.delete(1.0, END)
            content1.config(state="disabled")
            sock.send("00010".encode("utf-8"))
            time.sleep(0.2)
            sock.send(user_name.encode("utf-8"))
            data = sock.recv(1024).decode("utf-8")
            if data[0] == "(":
                data = eval(data)      
                content1.config(state="normal")
                content1.insert(INSERT, "account: "+data[0]+"\n")
                content1.insert(INSERT, "sorce: "+str(data[1][0])+"\n")
                content1.insert(INSERT, "grade: "+str(data[1][1])+"\n")
                content1.config(state="disabled")
            else:
                messagebox.showerror("Error","Error, the name is not in db !!")
        else:
            messagebox.showerror("Error", "You don't input anything !!!")
    
    
    
    def btn3Fun():
        user_name2 = in4.get()
        choose = com1.get()
        new_content = in2.get()
        if len(user_name2)!=0 and len(new_content)!=0:
            content1.config(state="normal")
            content1.delete(1.0, END)
            content1.config(state="disabled")
            sock.send("00011".encode("utf-8"))
            set_data = (user_name2, choose, new_content)
            sock.send(str(set_data).encode("utf-8"))
            chect_set2 = sock.recv(1024).decode("utf-8")
            if chect_set2 == "change successfully":
                content1.config(state="normal")
                content1.insert(INSERT, chect_set2+"\n")
                content1.config(state="disabled")
            elif chect_set2 == "input error":
                messagebox.showerror("Error!", "Input error !!!")
            elif chect_set2 == "name not in db":
                messagebox.showerror("Error", "The name is not in db !!!")
        else:
            messagebox.showerror("Error", "You don't input any name !!!")
    
    
    
    def btn4Fun():
        user_name3 = in3.get()
        if len(user_name3) != 0:
            content1.config(state="normal")
            content1.delete(1.0, END)
            content1.config(state="disabled")
            sock.send("00012".encode("utf-8"))
            time.sleep(0.2)
            sock.send(user_name3.encode("utf-8"))
            check_del = sock.recv(1024).decode("utf-8")
            if check_del == "delete successfully":
                content1.config(state="normal")
                content1.insert(INSERT, check_del+"\n")
                content1.config(state="disabled")
            elif check_del == "name3 not in db":
                messagebox.showerror("Error", "The name is not in db !!!")
        else:
            messagebox.showerror("Error", "You don't input any name !!!")
            
            
            


    for i in range(4):
        manage_window.rowconfigure(i, weight=1)
    for j in range(3):
        manage_window.columnconfigure(j, weight=1)



    f1 = Frame(manage_window, bg="#ffffdd")
    f1.grid(row=0, column=0, sticky=N+S+W, rowspan=4)



    lab2 = Label(f1, text="管理帳號", bg="#ffffdd", font="Arial 19 bold")
    lab2.pack(pady=15)



    f2 = Frame(f1)
    f2.pack(padx=10, pady=15)

    btn1 = Button(f2, text="印出帳號資料表", bg="#ffffff", font="Arial 14 bold", command=btn1Fun)
    btn1.pack(side="left")



    f3 = Frame(f1)
    f3.pack(padx=10, pady=35)

    in1 = Entry(f3, width=15, font="Arial 19 bold")
    in1.pack(side="left")

    btn2 = Button(f3, text="查詢帳號資料", bg="#ffffff", font="Arial 14 bold", command=btn2Fun)
    btn2.pack(side="left")
    
    
    
    f6 = Frame(f1)
    f6.pack(padx=10, pady=5)
    
    in4 = Entry(f6, width=15, font="Arial 19 bold")
    in4.pack(side="left")
    
    lab1 = Label(f6, text="<-被修改帳號")
    lab1.pack(side="left")



    f4 = Frame(f1)
    f4.pack(padx=10, pady=5)

    com1 = ttk.Combobox(f4, values=["sorce", "grade"], width=6, font="Arial 14 bold")
    com1.pack(side="left")
    com1.current(0)

    in2 = Entry(f4, width=10, font="Arial 19 bold")
    in2.pack(side="left")

    btn3 = Button(f4, text="修改資料", bg="#ffffff", font="Arial 14 bold", command=btn3Fun)
    btn3.pack(side="left")



    f5 = Frame(f1)
    f5.pack(padx=10, pady=35)

    in3 = Entry(f5, width=15, font="Arial 19 bold")
    in3.pack(side="left")

    btn4 = Button(f5, text="刪除帳號", bg="#ffffff", font="Arial 14 bold", command=btn4Fun)
    btn4.pack(side="left")



    btn5 = Button(f1, text="退出介面", bg="#ffffff", font="Arial 14 bold", fg="red", command=exit)
    btn5.pack(pady=20)



    content1 = Text(manage_window, font="Arial 18 bold", bg="#ffffff", state="disabled", width=40)
    content1.grid(row=0, column=1, rowspan=4, columnspan=2, sticky=N+S)





