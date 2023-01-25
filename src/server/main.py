from classes.Server import Server
from classes.Client import Client
import threading
import sys

port = 6969

server = Server(port)

server.connect()

clientsThreads = []
clients = []

connectedClient = 0

while True:
    if connectedClient < 2:
        conn, addr = server.accept()
        connectedClient += 1
        print(connectedClient)
        client = Client(conn, addr, [])
        clients.append(client)
        serverThread = threading.Thread(target=Server.connectionHandler, args=(conn, addr, client, clients))
        clientsThreads.append(serverThread)
        serverThread.start()
    else:
        conn, addr = server.accept()
        serverThread = threading.Thread(targets=Server.kickHandler, args=(conn,addr))
        serverThread.start()