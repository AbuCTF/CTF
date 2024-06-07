import socket
import json

def exchange(keys):
    host = '83.136.254.167'
    port = 47355

    command_data = {
        "keys": keys
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(json.dumps(command_data).encode('utf-8'))
        data = s.recv(1024)
        return data.decode('utf-8')

# Keys to retrieve the flag
keys = [239, 64, 24]

# Exchange keys with the server and receive the flag
flag = exchange(keys)

print("Flag:", flag)
