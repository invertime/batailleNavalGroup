import tkinter as tk
import socket
from classes.Boat import Boat
from classes.vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSex_sixenlatin_Mecanic_bytesManager


class Board:

    window, boatCanvas, missileCanvas, game = None, None, None, None
    sizeIndex: int = 0
    tiles: list[list[int]]
 
    def __init__(self, bSize, cSize, sendFunc: str, killFunc, sendTest):
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
        px = event.x
        py = event.y
        caseX = px//self.caseSize
        caseY = py//self.caseSize
        pos = Vector2d(caseX, caseY)
        boat = self.game.PreviewBoatLocation(self, pos, self.sizeIndex)
        newBoat = Boat(boat)
        if (set(boat).intersection(set(self.boats)) == []):
            print(newBoat," added")
            self.boats.append(newBoat)
            for b in newBoat.getCells():
                self.boatsCases.append(self.boatCanvas.create_rectangle(b.x*self.caseSize,b.y*self.caseSize,b.x*self.caseSize+self.caseSize,b.y*self.caseSize+self.caseSize,fill="red"))
            self.sizeIndex += 1
            if self.sizeIndex == len(self.game.sizes):
                self.boatCanvas.bind("<Button-1>", self._pass)
                self.boatCanvas.bind("<Button-3>", self._pass)
                self.boatCanvas.bind("<Motion>", self._pass)
            
        # case = chr(65+caseX)+str(caseY+1)
        # if (case not in self.boatCase):
        #     print(case,"added")
        #     self.boatCase.append(case)

    def _pass(self, e):
        pass

    def clickToRemove(self, event):
        px = event.x
        py = event.y
        caseX = px//self.caseSize
        caseY = py//self.caseSize
        for b in self.boatsCases:
            print(b)
            
        # self.boatCanvas.create_rectangle(caseX*self.caseSize, caseY*self.caseSize, caseX*self.caseSize+self.caseSize, caseY*self.caseSize+self.caseSize,fill=self.colors[(caseX%2+caseY%2)%2])
        # case = chr(65+caseX)+str(caseY+1)
        # print(case,"removed")
        # self.boatCase.remove(case)

    def clickToRotate(self, event):
        self.game.Rotate()
        self.preview(event)

    def preview(self, event):
        self.drawBoard()

        pos = Vector2d(event.x // self.caseSize, event.y // self.caseSize)
        boat = self.game.PreviewBoatLocation(self, pos, self.sizeIndex)

        for b in boat:
            self.boatCanvas.create_rectangle(b.x * self.caseSize, b.y * self.caseSize, (b.x + 1) * self.caseSize, (b.y + 1) * self.caseSize, fill="green")

    def create(self):
        self.window = tk.Tk()
        self.boatCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.boatCanvas.pack(side=tk.LEFT)
        self.game = gameSex_sixenlatin_Mecanic_bytesManager()
        self.drawBoard()
        self.boatCanvas.bind("<Button-1>", self.clickToPlace)
        self.boatCanvas.bind("<Button-2>", self.clickToRemove)
        self.boatCanvas.bind("<Button-3>", self.clickToRotate)
        self.boatCanvas.bind("<Motion>", self.preview)
        SendBoatLocationButton = tk.Button(self.window, text="Send your boats location", command= lambda: self.sendFunc(self.boatCase))
        SendBoatLocationButton.pack(side=tk.BOTTOM)
        self.missileCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.missileCanvas.pack(side=tk.LEFT)
        self.missileCanvas.create_rectangle(0,0,self.caseSize*self.boardSize,self.caseSize*self.boardSize, fill="grey")
        self.window.mainloop()

    def drawBoard(self):
        boatTiles = [[B.getTupple() for B in b.getCells()] for b in self.boats]
        for lign in range(self.boardSize):
            self.tiles.append([])
            for row in range(self.boardSize):
                x=row*self.caseSize
                y=lign*self.caseSize
                color = "red" if (row, lign) in boatTiles else self.colors[(lign%2+row%2)%2]
                self.tiles[lign].append(self.boatCanvas.create_rectangle(x,y,x+self.caseSize,y+self.caseSize,fill=color))
                    
    def initBoard(self):
        boatTiles = [[B.getTupple() for B in b.getCells()] for b in self.boats]
        for lign in range(self.boardSize):
            self.tiles.append([])
            for row in range(self.boardSize):
                x=row*self.caseSize
                y=lign*self.caseSize
                color = "red" if (row, lign) in boatTiles else self.colors[(lign%2+row%2)%2]
                self.tiles[lign].append(self.boatCanvas.create_rectangle(x,y,x+self.caseSize,y+self.caseSize,fill=color))
