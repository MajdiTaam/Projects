from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class Connection:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.name = 'N/A'


class Server:
    def __init__(self):
        host = '127.0.0.1'
        port = 21568
        self.buffer_size = 1024
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.clients = {}
        self.server_socket.listen()
        self.start()

    def start(self):
        main_thread = Thread(target=self.accept_connections)
        main_thread.start()
        main_thread.join()
        self.server_socket.close()

    def accept_connections(self):
        while True:
            print('waiting for connection...')
            conn, addr = self.server_socket.accept()
            print('...connected from:', addr)
            self.clients[conn] = Connection(conn, addr)
            th = Thread(target=self.client_thread, args=(conn,))
            th.start()

    def client_thread(self, client):
        name = client.recv(self.buffer_size).decode("utf8")
        client.send(bytes(f"{name} is online.", "utf8"))
        client.send(bytes("Hi " + name + ", type close when you want to leave.", "utf8"))
        # broadcast name
        self.clients[client].name = name
        file = open(f"{name}_key.pem", 'r') # open public of the client
        public_key = RSA.import_key(file.read()) #read the public key of the client
        while True:
            decryptor = PKCS1_OAEP.new(public_key)  # use the private key of server to decrypt
            encrypted_msg = client.recv(self.buffer_size) #encrypt msg using server pyblic key
            msg = decryptor.decrypt(encrypted_msg)
            if msg == bytes("close", "utf8"):
                del self.clients[client]
                message = bytes(name, "utf8") + bytes(" went offline.", "utf8")
                self.broadcast(message)
                break
            else:
                message = bytes(name, "utf8") + bytes(": ", "utf8") + msg
                self.broadcast(message)


    def broadcast(self, msg):
        print("Online users: ")
        for client in self.clients:
            print(self.clients[client].name)
            client.send(msg)


if __name__ == '__main__':
    server = Server()