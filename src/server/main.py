from classes.server import Server
from classes.Client import Client
import threading
import sys

port = 6969

server = Server(port)

server.connect()

clients = []

connectedClient = 0

while True:
    if connectedClient < 100000:
        conn, addr = server.accept()
        connectedClient += 1
        print(connectedClient)
        client = Client([])
        serverThread = threading.Thread(target=Server.connectionHandler, args=(conn, addr, client))
        clients.append(serverThread)
        serverThread.start()
    else:
        conn, addr = server.accept()
        serverThread = threading.Thread(targets=Server.kickHandler, args=(conn,addr))
        serverThread.start()