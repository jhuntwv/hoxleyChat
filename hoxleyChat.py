#!/usr/bin/python3
'''  Hoxley Chat Alpha ! '''

import sys
import socket

def serverListener(HOST='', PORT=6666):
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((HOST, PORT))
    lsock.listen()
    lsock.setblocking(False)
    return lsock

def startSession(lsock):
    try:
        conn, source = lsock.accept()
        conn.setblocking(False)
        return conn, source
    except:
        return False 

def getInput(conn):
    try:
        return conn.recv(30)
    except:
        pass

def sendOutput(conn,message ):
    try:
        conn.sendall(message)
    except:
        pass




connections = []              #list of accept() tuples
messagePool = []         #

lsock = serverListener()        #Initialize Server


while True:                     #basic connection acceptor loop                     
    newConn = startSession(lsock)
    if newConn:
        connections.append(newConn)

    for i in connections:

        try:
            sendOutput(i[0], messagePool[-1])
        except:
            pass
        try:
            messagePool.append(getInput(i[0]))
        except:
            pass

        









