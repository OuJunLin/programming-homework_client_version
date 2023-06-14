import threading
from tkinter import *
from tkinter import messagebox



def create_chatroom_window(sock, chatroom_window):
    sock.send("00006".encode("utf-8"))
    
    
    
    chatroom_window.title("chatroom_window")
    chatroom_window.geometry("600x500+700+300")

    for i in range(9):
        chatroom_window.rowconfigure(i, weight=1) 
    for j in range(6):
        chatroom_window.columnconfigure(j, weight=1)
        
    
    
    def exit():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            chatroom_window.destroy()
    
    
    
    def recv_msg(sock):
        while True:
            data = sock.recv(1024)
            Msg = data.decode('utf-8')
            if Msg == "00000exit":
                break
            else:
                content1.config(state="normal")
                content1.insert(INSERT, Msg+"\n")
                content1.config(state="disabled")
    tr = threading.Thread(target=recv_msg, args=(sock,))
    tr.start()
    
    
    
    def send_msg(sock):
        msg = in1.get()
        if len(msg) != 0:
            sock.send(msg.encode("utf-8"))
        else:
            messagebox.showerror("Error", "You don't input anything !!!")

        


    content1 = Text(chatroom_window, font="Arial 14 bold", state="disabled", bg="#ffffff")
    content1.grid(row=0, column=0, rowspan=7, columnspan=6, sticky=NSEW)

    in1 = Entry(chatroom_window, font="Arial 30 bold")
    in1.grid(row=7, column=0,columnspan=4, pady=10, padx=2)

    btn1 = Button(chatroom_window, text="sumbit", height=5, width=10, bg="#ffffff", font="Arial 12 bold", command=lambda: send_msg(sock))
    btn1.grid(row=7, column=4, pady=10, padx=1)

    btn2 = Button(chatroom_window, text="exit", height=5, width=10, bg="#ffffff", font="Arial 12 bold", command=exit)
    btn2.grid(row=7, column=5, pady=10, padx=1)



