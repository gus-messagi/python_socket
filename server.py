import socket, pickle, json
import threading
from threading import Thread
from user import User

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = socket.gethostname()
PORT = 1235

server_socket.bind((HOST, PORT))
server_socket.listen(5)

_users = set()
clients_lock = threading.Lock()

_data = ""


def client_thread(client_socket, ip, port, _data):

    try:
        while True:
            user_data = pickle.loads(client_socket.recv(1024))
            user_file = pickle.loads(user_data[0])
            filename = pickle.loads(user_data[1])

            user = User(client_socket)
            user.file = filename

            with clients_lock:
                _users.add(user)

            if _data != user_file:
                with open("./files/" + filename + ".json", 'w+') as file:
                    json.dump(user_file, file)
                        
                    file_to_send = pickle.dumps(user_file)
                    with clients_lock:
                        for user in _users:
                            if user.file == filename:
                                user._socket.sendall(file_to_send)
                                
                    file.close()
            _data = user_file
    finally:
        with clients_lock:
            for user in _users:
                user._socket.remove(client_socket)
                client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    ip, port = str(address[0]), str(address[1])

    try:
        Thread(target=client_thread, args=(client_socket, ip, port, _data)).start()
    except:
        print("Thread Falhou")