from socket import socket, AF_INET, SOCK_STREAM
import tkinter
from threading import Thread
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class Client:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Python Skype Clone")
        self.add_message_list()
        self.add_message_field()
        self.name = input("Enter your name: ")
        self.key = RSA.generate(1024)
        open(f'{self.name}_key.pem','wb').write(self.key.exportKey())
        self.connect()
        self.client_socket.send(bytes(self.name, "utf-8"))
        tkinter.mainloop()

    def add_message_list(self):
        frame = tkinter.Frame(self.window)
        scrollbar = tkinter.Scrollbar(frame)
        self.message_list = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.message_list.pack(side=tkinter.LEFT)
        frame.pack()

    def add_message_field(self):
        self.message_field = tkinter.Entry(self.window)
        self.message_field.pack()
        self.send_button = tkinter.Button(self.window, text="Send", command=self.send)
        self.send_button.pack()

    def connect(self):
        host = '127.0.0.1'
        port = 21568
        self.buffer_size = 1024
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((host, port))
        th = Thread(target=self.receive)
        th.start()

    def receive(self):
        while True:
            msg = self.client_socket.recv(self.buffer_size).decode("utf8")
            self.message_list.insert(tkinter.END, msg)

    def send(self):
        msg = self.message_field.get()
        self.message_field.delete(0, "end")
        encryptor = PKCS1_OAEP.new(self.key.publickey())
        encrypted_msg = encryptor.encrypt(bytes(msg, "utf8"))
        self.client_socket.send(encrypted_msg)
        if msg == "close":
            self.window.quit()


if __name__ == '__main__':
    client = Client()