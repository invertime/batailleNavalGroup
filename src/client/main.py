import threading
from classes.Window import Window
from classes.Client import Client
from classes.ServerConnectionWindow import ServerConnectionWindow

boardSize = 10
caseSize = 75

class Main:
    def __init__(self, boardSize, caseSize, host=None,port=None) -> None:
        self.host = host
        self.port = port
        self.boardSize = boardSize
        self.caseSize = caseSize
        self.serverSelected = False

    def serverSelecter(self,h,p):
        self.host = h
        self.port = p
        self.serverSelected = True


main = Main(boardSize, caseSize)


serverConnection = ServerConnectionWindow()

serverConnection.create(main.serverSelecter)

while not main.serverSelected:
    pass

client = Client(main.host, main.port)

board = Window(boardSize, caseSize)

client.create()
board.create(client.sendBoatLocation, client.sendMissile)
