from tkinter import *
import socket

def start_server():
    button_pressed = "1"
    client = socket.socket()
    # Define the port on which you want to connect
    port = 12345
    # connect to the server on local computer
    client.connect((' 10.193.164.190', port))
    if button_pressed == "1":
        data_bytes = button_pressed.encode()
        client.send(data_bytes)


window = Tk()
window.geometry('300x300')
client = str('Подари другу котика!')

l = Label(window, text = client, font=("Times", "15"))
l.pack(expand=True)
b = Button(window, text="жми кнопку :)", font=("Times", "12"),command=start_server)
b.pack(expand=True)
window.mainloop()
