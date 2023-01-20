import threading
from classes.Window import Window
from classes.Client import Client


host = "127.0.0.1"
port = 6969
boardSize = 10
caseSize = 75

client = Client(host,port)

board = Window(boardSize,caseSize,client.sendBoatLocation,client.sendKill, client.sendTest)

client.create()
board.create()

