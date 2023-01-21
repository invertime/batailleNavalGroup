import threading
from classes.Window import Window
from classes.Client import Client


host = "127.0.0.1"
port = 6969
boardSize = 10
caseSize = 75

client = Client(host, port)

board = Window(boardSize, caseSize)

client.create()
board.create(client.sendBoatLocation, client.sendMissile)
