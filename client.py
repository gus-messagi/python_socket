import socket, pickle, json
from threading import Thread

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 1235

client_socket.connect((HOST, PORT))

filename = input("Filename: ")

while True:   
    data = {}
    user_file = input("JSON inline: ")

    if user_file != data:
        message = [pickle.dumps(user_file), pickle.dumps(filename)]
        _message = pickle.dumps(message)
        client_socket.sendall(_message)
        data = client_socket.recv(1024)
        _data = pickle.loads(data)
        
        print(_data)