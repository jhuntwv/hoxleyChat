#!/usr/bin/python3
#simple echo server

import socket

HOST = "127.0.0.1"
PORT = 6666

occultListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
occultListener.bind((HOST, PORT))
occultListener.listen()

occultSpeaker, guest = occultListener.accept()

print("connection established with" + str(guest))


masterLog = open("masterlog.txt", "w")

while True:
    data = occultSpeaker.recv(1024)
    if not data:
        break
    occultSpeaker.sendall(data)
    masterLog.write(str(data) + '\n')

occultSpeaker.close()
occultListener.close()
masterLog.close()
