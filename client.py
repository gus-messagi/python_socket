import socket, pickle, json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 1235

client_socket.connect((HOST, PORT))

user_file = {
    "name": "name",
    "type": "type",
    "fields": {
        "field1": "field1",
        "field2": "field2"
    }
}

while True:
    _data = {}
    if user_file != _data:
        message = [pickle.dumps(user_file), pickle.dumps("filename")]
        _message = pickle.dumps(message)
        client_socket.sendall(_message)
        data = client_socket.recv(1024)
        _data = json.dumps(pickle.loads(data))

