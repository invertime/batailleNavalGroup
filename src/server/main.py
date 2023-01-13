from classes.server import *
import threading
import sys

port = 6969

server = Server(port)

server.connect()

servers = []

connectedClient = 0

while True:
    if connectedClient < 2:
        conn, addr = server.accept()
        connectedClient += 1
        print(connectedClient)
        serverThread = threading.Thread(target=connectionHandler, args=(conn, addr))
        servers.append(serverThread)
        serverThread.start()
    else:
        conn, addr = server.accept()
        serverThread = threading.Thread(target=kickHandler, args=(conn,addr))
        serverThread.start()



