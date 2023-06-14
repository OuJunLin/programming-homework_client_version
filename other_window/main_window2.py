from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from other_window.face_window import create_face_window
from other_window.chatroom_window import create_chatroom_window
from other_window.phone_window import create_phone_window
from other_window.set_pw_window import create_set_pw_window
from other_window.manage_window import create_manage_window
import time
import threading



img1 = None
imgData = None
def create_main_window(sock, main_window):
    global img1
    global imgData
    
    def recv_img():
        imgFile = open('Img\\saveImg.jpg', 'wb')  
        while True:
            imgData = sock.recv(1024)
            if imgData == "transmit end".encode("utf-8"):
                break  
            imgFile.write(imgData)
        imgFile.close()
    
    
    
    user_data = eval(sock.recv(1024).decode("utf-8"))
    account = user_data[1]
    sorce = user_data[0][0]
    grade = user_data[0][1]
    recv_img()
    

    
    def get_imgTK(img, maxlen):
        img_size = img.size
        if img_size[0] > img_size[1]:          
            scale = img_size[1]/img_size[0]  
            w = maxlen                  
            h = int(maxlen*scale)       
        else:                        
            scale = img_size[0]/img_size[1]  
            w = int(maxlen*scale)       
            h = maxlen 
        img = img.resize((w, h))
        return ImageTk.PhotoImage(img)



    def check_destory(check_window, check_window_title, pre_window):
        while True:
            try:
                time.sleep(0.1)
                check_window.title(check_window_title)
            except TclError:
                pre_window.deiconify()
                break
    
    
    
    def check_destory2(check_window, check_window_title, pre_window):
        while True:
            try:
                time.sleep(0.1)
                check_window.title(check_window_title)
            except TclError:
                sock.send("00000exit".encode("utf-8"))
                pre_window.deiconify()
                break



    main_window.title("main_window")
    main_window.geometry("800x600+700+300")
    for i in range(3):
        main_window.rowconfigure(i, weight=1)
    for j in range(3):
        main_window.columnconfigure(j, weight=1)
    
    
    
    
    
    
    def logout():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            main_window.destroy()
    
    
    
    def btn2Fun():
        face_window = Toplevel(main_window)
        create_face_window(sock, face_window)
        main_window.withdraw()
        tc = threading.Thread(target=check_destory, args=(face_window, "face_window", main_window), daemon=True)
        tc.start()
    
    
    
    def btn5Fun():
        chatroom_window = Toplevel(main_window)
        create_chatroom_window(sock, chatroom_window)
        main_window.withdraw()
        tc = threading.Thread(target=check_destory2, args=(chatroom_window, "chatroom_window", main_window), daemon=True)
        tc.start()
    
    
    
    def btn4Fun():
        phone_window = Toplevel(main_window)
        create_phone_window(sock, phone_window)
        main_window.withdraw()
        tc = threading.Thread(target=check_destory, args=(phone_window, "phone_window", main_window), daemon=True)
        tc.start()  
    
    
    
    def btn1Fun():
        set_pw_window = Toplevel(main_window)
        create_set_pw_window(sock, set_pw_window)
        main_window.withdraw()
        tc = threading.Thread(target=check_destory, args=(set_pw_window, "set_pw_window", main_window), daemon=True)
        tc.start()
    
    
    
    def btn8Fun():
        manage_window = Toplevel(main_window)
        create_manage_window(sock, manage_window)
        main_window.withdraw()
        tc = threading.Thread(target=check_destory, args=(manage_window, "manage_window", main_window), daemon=True)
        tc.start()



    f1 = Frame(main_window, bg="#ffffff")
    f1.grid(row=0, column=0, sticky=N+S+W, rowspan=3)

    img1 = Image.open("Img\\saveImg.jpg")
    img1 = get_imgTK(img1, 150)
    img_lab1 = Label(f1, image=img1, bg="#ffddff", width=155, height=155)
    img_lab1.pack(padx=50,pady=20)

    lab1 = Label(f1, text="帳號名稱: {}" .format(account), font="Arial 18 bold", width=15)
    lab1.pack(pady=10)

    f3 = Frame(f1, width=17)
    f3.pack(pady=8)
    lab2 = Label(f3, text="    密碼: ^_^    ", font="Arial 18 bold")
    lab2.pack(side="left")
    btn1 = Button(f3, text="set\npassword", bg="#ffffdd", font="Arial 8 bold", command=btn1Fun)
    btn1.pack(side="left")

    lab1 = Label(f1, text="分數: {} pt        " .format(sorce), font="Arial 18 bold", width=15, fg="blue")
    lab1.pack(pady=10)

    lab1 = Label(f1, text="等級: {} 等         " .format(grade), font="Arial 18 bold", width=15, fg="red")
    lab1.pack(pady=10)

    btn8 = Button(f1, text="管理帳號", bg="#ffffdd", font="Arial 18 bold", command=btn8Fun)
    btn8.pack(pady=16)
    if account != "manager":
        btn8.config(state="disabled")
    
    btn7 = Button(f1, text="登出帳號", bg="#ffffdd", fg="red", font="Arial 18 bold", command=logout)
    btn7.pack(pady=16)



    lf1 = LabelFrame(main_window, text="影像預覽:", width=100, font="Arial 16 bold", labelanchor=NW, bd=4)
    lf1.grid(row=0, column=1, sticky=W+E)

    btn2 = Button(lf1, text="影像辨識", bg="#ffffdd", font="Arial 14 bold", command=btn2Fun)
    btn2.pack(padx=10, pady=10)



    lf2 = LabelFrame(main_window, text="電話篩選:", width=100, font="Arial 16 bold", labelanchor=NW, bd=4)
    lf2.grid(row=1, column=1, sticky=W+E)

    btn4 = Button(lf2, text="電話篩選", bg="#ffffdd", font="Arial 14 bold", command=btn4Fun)
    btn4.pack(padx=50, pady=10)



    lf3 = LabelFrame(main_window, text="通訊功能:", width=100, font="Arial 16 bold", labelanchor=NW, bd=4)
    lf3.grid(row=2, column=1, sticky=W+E)

    btn5 = Button(lf3, text="聊天室", bg="#ffffdd", font="Arial 14 bold", command=btn5Fun)
    btn5.pack(padx=50, pady=10)




