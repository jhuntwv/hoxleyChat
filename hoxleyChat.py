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
    else:
        return False 

def getInput(conn):
    try:
        return conn.recv(4096)
    else:
        pass

def sendOutput(conn, ):
    try:
        conn.sendall(




connections = []              #list of accept() tuples
messagePool = []         #

lsock = serverListener()        #Initialize Server


while True:                     #basic connection acceptor loop                     
    newConn = startSession(lsock)
    if newConn:
        connCollector.append(newConn)

    for i in connections:
        messagePool.append(getInput(i[0]))
        sendOutput(i[0], messagePool[-1])

        









