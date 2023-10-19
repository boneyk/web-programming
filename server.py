from tkinter import *
from PIL import Image, ImageTk
import socket

server = socket.socket()
print("Socket successfully created")
port = 12345
server = socket.create_server(('192.168.214.46', port))
print("socket binded to %s" % (port))
server.listen(1)
print("socket is listening")
k = 0

while True:
    user, address = server.accept()
    print(f'New connection from {address}')
    data = user.recv(1024).decode()
    if data == "1":
        root = Tk()
        root.geometry('300x300')
        images = ["C:\\Users\\nastya-pls\\Desktop\\something\\sing.png", "C:\\Users\\nastya-pls\\Desktop\\something\\sleep.png", "C:\\Users\\nastya-pls\\Desktop\\something\\computer.png", "C:\\Users\\nastya-pls\\Desktop\\something\\hungry.png"]
        # список объектов ImageTk
        image_tk_list = []
        for image in images:
            img = Image.open(image)
            img_tk = ImageTk.PhotoImage(img)
            image_tk_list.append(img_tk)
        label_list = []
        for img_tk in image_tk_list:
            label = Label(root, image=img_tk)
            label_list.append(label)
        for label in label_list:
            if k % 4 == label_list.index(label):
                label.pack()
        k=k+1
        root.mainloop()
    else:
        print(f'Connection from {address} interrupted!')
        break
