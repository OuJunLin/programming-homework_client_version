from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk



img1 = None
imgData = None
def create_main_window(sock, main_window):
    global img1
    global imgData
    user_data = eval(sock.recv(1024).decode("utf-8"))
    account = user_data[1]
    sorce = user_data[0][0]
    grade = user_data[0][1]
    
    imgFile = open('Img\\saveImg.jpg', 'wb')  
    while True:
        imgData = sock.recv(1024)
        if imgData == "transmit end".encode("utf-8"):
            break  
        imgFile.write(imgData)
    imgFile.close()
    
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
        print("ok")
        return ImageTk.PhotoImage(img)



    main_window.title("main_window")
    main_window.geometry("800x600+700+300")
    for i in range(3):
        main_window.rowconfigure(i, weight=1)
    for j in range(3):
        main_window.columnconfigure(j, weight=1)
    
    
    
    
    
    
    def logout():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            main_window.destroy()






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
    btn1 = Button(f3, text="set\npassword", bg="#ffffdd", font="Arial 8 bold")
    btn1.pack(side="left")

    lab1 = Label(f1, text="分數: {} pt        " .format(sorce), font="Arial 18 bold", width=15, fg="blue")
    lab1.pack(pady=10)

    lab1 = Label(f1, text="等級: {} 等         " .format(grade), font="Arial 18 bold", width=15, fg="red")
    lab1.pack(pady=10)

    btn2 = Button(f1, text="管理帳號", bg="#ffffdd", font="Arial 18 bold")
    btn2.pack(pady=16)
    
    btn7 = Button(f1, text="登出帳號", bg="#ffffdd", fg="red", font="Arial 18 bold", command=logout)
    btn7.pack(pady=16)



    lf1 = LabelFrame(main_window, text="影像預覽:", width=100, font="Arial 16 bold", labelanchor=NW, bd=4)
    lf1.grid(row=0, column=1, sticky=W+E)

    btn2 = Button(lf1, text="影像辨識", bg="#ffffdd", font="Arial 14 bold")
    btn2.pack(padx=10, pady=10)

    btn3 = Button(lf1, text="計算人頭", bg="#ffffdd", font="Arial 14 bold")
    btn3.pack(padx=10, pady=10)



    lf2 = LabelFrame(main_window, text="電話篩選:", width=100, font="Arial 16 bold", labelanchor=NW, bd=4)
    lf2.grid(row=1, column=1, sticky=W+E)

    btn4 = Button(lf2, text="電話篩選", bg="#ffffdd", font="Arial 14 bold")
    btn4.pack(padx=50, pady=10)



    lf3 = LabelFrame(main_window, text="通訊功能:", width=100, font="Arial 16 bold", labelanchor=NW, bd=4)
    lf3.grid(row=2, column=1, sticky=W+E)

    btn5 = Button(lf3, text="聊天室", bg="#ffffdd", font="Arial 14 bold")
    btn5.pack(padx=50, pady=10)

    btn6 = Button(lf3, text="井字遊戲", bg="#ffffdd", font="Arial 14 bold")
    btn6.pack(padx=50, pady=10)


