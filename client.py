#!/usr/bin/python3

import socket 

def callServer(HOST="127.0.0.1", PORT=6666):
    occultCaller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    occultCaller.connect((HOST, PORT))
    return occultCaller

def sendMessage(message, connection):
    connection.sendall(bytes(message, 'utf-8'))
    print(str(connection.recv(1024)))

def draftMessage(): 
    print("\n:")
    return (input())

print("press enter to initate connection")
input()
occultCaller = callServer()

print("Begin messaging when ready.") 

while True:
    sendMessage(draftMessage(), occultCaller)

