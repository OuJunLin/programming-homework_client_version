import socket
import time
import threading
from tkinter import *
from tkinter import messagebox
import time
from login_window import create_login_window

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

input_window = Tk()
input_window.title("input")
input_window.geometry("350x200+750+400")
for i in range(3):
    input_window.rowconfigure(i, weight=1)
for i in range(2):
    input_window.columnconfigure(i, weight=1)



lab1 = Label(input_window, text="IP: ")
lab1.grid(row=0, column=0, sticky=SE)

lab2 = Label(input_window, text="Port: ")
lab2.grid(row=1, column=0, sticky=E)

in1 = Entry(input_window, width=15)
in1.grid(row=0, column=1, sticky=SW)

in2 = Entry(input_window, width=15)
in2.grid(row=1, column=1, sticky=W)

fr1 = Frame(input_window)
fr1.grid(row=2, column=1)



def check_destory(check_window, check_window_title, pre_window):
    while True:
        try:
            time.sleep(0.1)
            check_window.title(check_window_title)
        except TclError:
            s.send("00000".encode("utf-8"))
            pre_window.destroy()
            break
            


def connect():
    global login_window1
    ip = in1.get()
    port = in2.get()
    if len(ip)!=0 and len(port)!=0:
        try:
            port = int(port)
            s.connect((ip, port))
            s.send("157sfff9345s17at86322srr564".encode("utf-8"))
            correctCode = s.recv(1024).decode("utf-8")
            if correctCode == "10000":
                print("connect!!")
                login_window = Toplevel(input_window)
                create_login_window(s, login_window, input_window)
                input_window.withdraw()
                tc = threading.Thread(target=check_destory, args=(login_window, "login", input_window), daemon=True)
                tc.start()
        except ValueError:
            messagebox.showerror("Error !", "input error !!!")
        except:
            messagebox.showerror("Error !", "Error, can not connect !!!")
            input_window.destroy()
    else:
        messagebox.showerror("Error !", "no input !!!")
        


btn1 = Button(fr1, text="sumbit", bg="#ffffff", height=2, command=connect)
btn1.pack()



input_window.mainloop()
s.close()



