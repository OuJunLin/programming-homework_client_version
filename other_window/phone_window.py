from tkinter import messagebox
from tkinter import *
import re
import time



def create_phone_window(sock, phone_window):
    phone_window.title("phone_window")
    phone_window.geometry("800x600+700+300")

    for i in range(3):
        phone_window.rowconfigure(i, weight=1)
    for j in range(5):
        phone_window.columnconfigure(j, weight=1)

    content1 = Text(phone_window, font="Arial 14 bold", bg="#ffffff")
    content1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky=N+S)
    
    
    
    def exit():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            phone_window.destroy()
    
    
    
    def btn1Fun():
        content2.config(state="normal")
        content2.delete(1.0, END)
        content2.config(state="disabled")
        data = content1.get("0.0", END)
        if len(data) != 1:
            match = re.findall(r"\d{4}-\d{3}-\d{3}|\(\d{2}\)\d{8}|\(\d{2}\)\d{4}-\d{4}|\+\d{3}-\d-\d{4}-\d{4}", data)
            for phone in match:
                content2.config(state="normal")
                content2.insert(INSERT, phone+"\n")
                content2.config(state="disabled")
            sock.send("00007".encode("utf-8"))
            time.sleep(0.2)
            sock.send(str(match).encode("utf-8"))
        else:
            messagebox.showerror("Error", "You don't input anything !!!")
        




    f1 = Frame(phone_window, bg="#ffffdd")
    f1.grid(row=0, column=3, rowspan=3, columnspan=2, sticky=N+S+W+E)

    btn1 = Button(f1, text="查詢電話號碼", bg="#ffffff", font="Arial 18 bold", width=25, command=btn1Fun)
    btn1.pack(padx=50, pady=20)

    btn2 = Button(f1, text="退出頁面", bg="#ffffff", font="Arial 18 bold", fg="red", command=exit)
    btn2.pack()

    lab1 = Label(f1, text="搜尋結果:", bg="#ffffdd", font="Arial 18 bold")
    lab1.pack(pady=30)

    content2 = Text(f1, font="Arial 16 bold", bg="#ffffff", state="disabled", width=20)
    content2.pack(padx=10, pady=10)



