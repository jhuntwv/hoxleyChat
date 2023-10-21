#!/usr/bin/python3

import socket 

def callServer(HOST="127.0.0.1", PORT=6666):
    occultCaller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    occultCaller.connect((HOST, PORT))
    return occultCaller

def message(message, connection):
    connection.sendall(message)
    print(str(connection.recv(1024)))

occultCaller = callServer()


