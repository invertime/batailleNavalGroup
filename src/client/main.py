import threading
import time
from classes.Window import Window
from classes.Client import Client
from classes.ServerConnectionWindow import ServerConnectionWindow
from classes.WaitWindow import WaitWindow

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

client = Client(main.host, main.port)
clientThread = client.create()

window = Window(boardSize, caseSize)
window.create(client.sendBoatLocation, client.sendMissile, client.wait, client.waitOtherPlayerToSendBoats)

waitWindow = WaitWindow()
waitWindow.create(client.waitOtherPlayerToConnect)