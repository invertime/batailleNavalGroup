import tkinter as tk
import socket
from classes.Boat import Boat
from classes.Vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSex_sixenlatin_Mecanic_bytesManager


class PlaceBoard:

    canvas: tk.Canvas = None
    oldPreview: list[Vector2d] = []
    tiles: list[list[int]] = []
 
    def __init__(self, canvas, game, bSize, cSize, sendFunc: str, killFunc, sendTest):
        self.canvas = canvas
        self.game = game
        self.boardSize: int = bSize
        self.caseSize: int = cSize
        self.tiles = []
        self.boatsCases: list[any] = []
        self.boats: list[Boat] = []
        self.colors: list[str] = ["white","black"]
        self.sendFunc: function[list[str], None] = sendFunc
        self.killFunc: function[None] = killFunc
        self.sendTest: function[socket.socket] = sendTest
    
    def clickToPlace(self, event):
        caseX, caseY = self.canvasToBoard((event.x, event.y))

        pos = Vector2d(caseX, caseY)
        boat = self.game.PreviewBoatLocation(self, pos)
        newBoat = Boat(boat)

        boatOverlapp = False

        for i in self.boats:
            for j in boat:
                if j in i.getCells():
                    boatOverlapp = True


        if (not boatOverlapp or len(self.boats) == 0):
            print(newBoat," added")
            self.boats.append(newBoat)
            self.game.removeSize(self.game.getMaxBoatSizeToPlace())
            for b in newBoat.getCells():
                self.boatsCases.append(self.canvas.create_rectangle(b.x*self.caseSize,b.y*self.caseSize,b.x*self.caseSize+self.caseSize,b.y*self.caseSize+self.caseSize,fill="red"))
            if not self.game.sizes:
                print("every boats are placed")
                self.canvas.bind("<Button-1>", self._pass)
                self.canvas.bind("<Button-2>", self._pass)
                self.canvas.bind("<Button-3>", self._pass)
                self.canvas.bind("<Motion>", self._pass)
        else:
            print("There is a boat here")

    def _pass(self, e):
        pass

    def canvasToBoard(self, pos: tuple[int, int]) -> tuple[int, int]:
        return pos[0] //self.caseSize, pos[1] //self.caseSize

    def clickToRemove(self, event):
        caseX, caseY = self.canvasToBoard((event.x, event.y))

        for b in self.boats:
            for B in b.getCells():
                if (caseX,caseY) == B.getTupple():
                    self.boats.remove(b)
                    self.game.addSize(b.getLength())
                    print(b, "deleted")
                    self.drawBoard()
                    self.preview(event)
                    return

    def clickToRotate(self, event):
        self.game.Rotate()
        self.preview(event)

    def preview(self, event):
        self.drawBoard()

        pos = Vector2d(event.x // self.caseSize, event.y // self.caseSize)
        boat = self.game.PreviewBoatLocation(self, pos)
        
        for b in boat:
            self.canvas.itemconfig(self.tiles[b.y][b.x], fill="green")

        self.oldPreview = boat

    def create(self):
        self.canvas.bind("<Button-1>", self.clickToPlace)
        self.canvas.bind("<Button-2>", self.clickToRemove)
        self.canvas.bind("<Button-3>", self.clickToRotate)
        self.canvas.bind("<Motion>", self.preview)
        self.initBoard()
        self.drawBoard()

    def drawBoard(self):
        boatTiles = []

        for b in self.boats:
            for B in b.getCells():
                boatTiles.append(B.getTupple())

        for lign in range(self.boardSize):
            for row in range(self.boardSize):
                color = "red" if (row, lign) in boatTiles else self.colors[(lign%2+row%2)%2]
                self.canvas.itemconfig(self.tiles[lign][row], fill=color)
                    
    def initBoard(self):
        for lign in range(self.boardSize):
            self.tiles.append([])
            for row in range(self.boardSize):
                x=row*self.caseSize
                y=lign*self.caseSize
                self.tiles[lign].append(self.canvas.create_rectangle(x,y,x+self.caseSize,y+self.caseSize))
