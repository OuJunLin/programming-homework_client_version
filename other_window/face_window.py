from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
from os import listdir
from os.path import isfile, isdir, join
import time



img1 = None
img2 = None
img_name_list = None
def create_face_window(sock, face_window):
    global img1
    global img2
    global img_name_list
    
    sock.send("00001".encode("utf-8"))
    img_data_dict = sock.recv(1024).decode("utf-8")
    img_data_dict2 = sock.recv(1024).decode("utf-8")
    img_data_dict = eval(img_data_dict + img_data_dict2)
    img_name_list = []
    for name in img_data_dict:
        img_name_list.append(name)
    
    
    
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
    
    
    
    def send_img(sock, img_path):
        imgFile = open(img_path, "rb")
        while True:
            imgData = imgFile.readline(1024)
            sock.send(imgData)
            if not imgData:
                break  
        imgFile.close()
        time.sleep(0.1)
        sock.send("transmit end".encode())
    
    
    
    def recv_img(sock, save_path):
        imgFile = open(save_path, 'wb')  
        while True:
            imgData = sock.recv(1024)
            if imgData == "transmit end".encode("utf-8"):
                break  
            imgFile.write(imgData)
        imgFile.close()
    
    
    
    def getFilePath(mypath):
        files = listdir(mypath) 
        file_list = []
        for f in files:
            fullpath = join(mypath, f)
            if isfile(fullpath):
                file_list.append(fullpath)
            elif isdir(fullpath):
                for f2 in getFilePath(fullpath):
                    file_list.append(f2)
        return file_list
    
    
    
    def img_draw_box(img, boxes):
        drawing = ImageDraw.Draw(img)
        for i in range(len(boxes)):
            shape = [(boxes[i][0], boxes[i][1]), (boxes[i][2], boxes[i][3])]
            drawing.rectangle(shape, outline="red", width=2)
    
    
    
    read_img_list = getFilePath("read_img")
    for i in range(len(read_img_list)):
        read_img_list[i] = read_img_list[i][9:]



    face_window.title("face_window")
    face_window.geometry("900x600+700+300")
    for i in range(4):
        face_window.rowconfigure(i, weight=1)
    for j in range(3):
        face_window.columnconfigure(j, weight=1)
    
    
    
    
    
    
    def logout():
        if messagebox.askquestion("exit", "Are you sure you want to leave ?") == "yes":
            face_window.destroy()
    
    
    
    def btn1Fun():
        global img2
        global img_name_list
        if len(img_name_list) != 0:
            read_path = "read_img\\" + com1.get()
            send_path = com1.get()
            sock.send("00002".encode("utf-8"))
            sock.send(send_path.encode("utf-8"))
            check_name = sock.recv(1024).decode("utf-8")
            print(check_name)
            if check_name == "img is exist":
                messagebox.showerror("Exist!", "The image file is alreadly in server!!!")
            elif check_name == "can send img":
                send_img(sock, read_path)
                face_result = eval(sock.recv(1024).decode("utf-8"))
                img2 = Image.open(read_path)
                img_draw_box(img2, face_result[0])
                img2 = get_imgTK(img2, 450)
                img_lab1.config(image=img2)
                lab3.config(text="影像資訊:\nclass='{}', file name='{}'\ntime='{}', name='{}'" .format(face_result[1], face_result[2], face_result[3], face_result[4]), font="Arial 13 bold")
                img_data_dict = sock.recv(1024).decode("utf-8")
                img_data_dict2 = sock.recv(1024).decode("utf-8")
                img_data_dict = eval(img_data_dict+img_data_dict2)
                img_name_list = []
                for name in img_data_dict:
                    img_name_list.append(name)
                com2.config(values=img_name_list)
                com3.config(values=img_name_list)
                com5.config(values=img_name_list)
    
    
    
    def btn2Fun():
        global img2
        global img_name_list  
        if len(img_name_list) != 0:
            sock.send("00003".encode("utf-8"))
            sock.send(com2.get().encode("utf-8"))
            file_name2 = sock.recv(1024).decode("utf-8")
            save_path = "Img\\save2" + file_name2[-4:]
            recv_img(sock, save_path)
            img_face_data2 = eval(sock.recv(1024).decode("utf-8"))
            img2 = Image.open("Img\\save2" + file_name2[-4:])
            img_draw_box(img2, img_face_data2[0])
            img2 = get_imgTK(img2, 450)
            img_lab1.config(image=img2)
            lab3.config(text="影像資訊:\nclass='{}', file name='{}'\ntime='{}', name='{}'" .format(img_face_data2[1], img_face_data2[2], img_face_data2[3], img_face_data2[4]), font="Arial 13 bold")
    
    
    
    def btn3Fun():
        global img_name_list
        if len(img_name_list) != 0:
            new_name = in2.get()
            if len(new_name) != 0:
                sock.send("00004".encode("utf-8"))
                time.sleep(0.1)
                sock.send(new_name.encode("utf-8"))
                time.sleep(0.1)
                sock.send(com3.get().encode("utf-8"))
                check_same = sock.recv(1024).decode("utf-8")
                if check_same == "same in db":
                    messagebox.showerror("Error", "The same name in db !!!")
                elif check_same == "config":
                    data = sock.recv(1024).decode("utf-8")
                    data2 = sock.recv(1024).decode("utf-8")
                    data = eval(data + data2)
                    img_name_list = []
                    for name in data:
                        img_name_list.append(name)
                    com2.config(values=img_name_list)
                    com2.current(0)
                    com3.config(values=img_name_list)
                    com3.current(0)
                    com5.config(values=img_name_list)
                    com5.current(0)
            else:
                messagebox.showerror("Error", "You don't input any name !!!")
    
    
    
    def btn4Fun():
        global img_name_list
        if len(img_name_list) != 0:
            sock.send("00005".encode("utf-8"))
            time.sleep(0.1)
            sock.send(com5.get().encode("utf-8"))
            data = sock.recv(1024).decode("utf-8")
            data2 = sock.recv(1024).decode("utf-8")
            data = eval(data + data2)
            img_name_list = []
            for name in data:
                img_name_list.append(name)
            com2.config(values=img_name_list)
            com2.current(0)
            com3.config(values=img_name_list)
            com3.current(0)
            com5.config(values=img_name_list)
            com5.current(0)
                   







    f1 = Frame(face_window, bg="#ffffff")
    f1.grid(row=0, column=0, sticky=N+S+W, rowspan=4)



    lab2 = Label(f1, text="人臉辨識資料庫", bg="#ffffff", font="Arial 19 bold")
    lab2.pack(pady=15)



    f2 = Frame(f1)
    f2.pack(padx=30, pady=35)

    com1 = ttk.Combobox(f2, values=read_img_list, width=15)
    com1.pack(side="left", padx=10)
    if len(read_img_list) != 0:
        com1.current(0)

    btn1 = Button(f2, text="新增影像", bg="#ffffdd", font="Arial 12 bold", command=btn1Fun)
    btn1.pack(side="left")



    f3 = Frame(f1)
    f3.pack(padx=30, pady=35)

    com2 = ttk.Combobox(f3, values=img_name_list, width=15)
    com2.pack(side="left", padx=10)
    if len(img_name_list) != 0:
        com2.current(0)

    btn2 = Button(f3, text="查詢影像", bg="#ffffdd", font="Arial 12 bold", command=btn2Fun)
    btn2.pack(side="left")



    f6 = Frame(f1)
    f6.pack(padx=30, pady=35)

    f4 = Frame(f6)
    f4.pack()

    com3 = ttk.Combobox(f4, values=img_name_list, width=13)
    com3.pack(side="left", padx=10)
    if len(img_name_list) != 0:
        com3.current(0)

    lab1 = Label(f4, text="<-被修改名稱")
    lab1.pack(side="left", padx=10)



    f5 = Frame(f6)
    f5.pack()

    in2 = Entry(f5, width=17)
    in2.pack(side="left", padx=10)

    btn3 = Button(f5, text="修改名稱", bg="#ffffdd", font="Arial 12 bold", width=10, command=btn3Fun)
    btn3.pack(side="left", padx=10)



    f7 = Frame(f1)
    f7.pack(padx=30, pady=35)

    com5 = ttk.Combobox(f7, values=img_name_list, width=15)
    com5.pack(side="left", padx=10)
    if len(img_name_list) != 0:
        com5.current(0)

    btn4 = Button(f7, text="刪除影像", bg="#ffffdd", font="Arial 12 bold", command=btn4Fun)
    btn4.pack(side="left", padx=10)



    btn5 = Button(f1, text="退出視窗", bg="#ffffdd",fg="red", font="Arial 16 bold", command=logout)
    btn5.pack(padx=30, pady=25)



    lab3 = Label(face_window, text="影像資訊:\n{}" .format("nothing"), bg="#ffffdd", font="Arial 16 bold", width=50, height=3, anchor=NW)
    lab3.grid(row=0, column=1, columnspan=2,rowspan=2, sticky=N+W+E)



    img1 = Image.open("Img\\face_wait_img.png")
    img1 = get_imgTK(img1, 450)
    img_lab1 = Label(face_window, image=img1, width=470, height=470)
    img_lab1.grid(row=2, column=1)
    
    