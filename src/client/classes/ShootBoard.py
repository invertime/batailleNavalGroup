import tkinter as tk
import socket
from classes.Boat import Boat
from classes.Vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSexMechanicV2

class ShootBoard:
    canvas: tk.Canvas = None
    game: gameSexMechanicV2 = None
    hitTiles: list[Vector2d] = []
    waterTiles: list[Vector2d] = []
    oldPreview: Vector2d
    tiles: list[list[int]]
 
    def __init__(self, canvas, game, bSize, cSize, sendFunc, killFunc, sendTest):
        self.canvas = canvas
        self.game = game
        self.boardSize: int = bSize
        self.caseSize: int = cSize
        self.tiles = []
        self.colors: list[str] = ["white","black"]
        self.sendFunc: function[list[str], None] = sendFunc
        self.killFunc: function[None] = killFunc
        self.sendTest: function[socket.socket] = sendTest

    def canvasToBoard(self, pos: tuple[int, int]) -> tuple[int, int]:
        return pos[0] //self.caseSize, pos[1] //self.caseSize

    def preview(self, event):
        self.drawBoard()

        x, y = self.canvasToBoard((event.x, event.y))
        if not (x, y) in (self.hitTiles + self.waterTiles):
            self.canvas.itemconfig(self.tiles[y][x], fill="green")

        self.oldPreview = Vector2d(event.x // self.caseSize, event.y // self.caseSize)

    def create(self):
        self.canvas.bind("<Button-1>", self.clickToShoot)
        self.canvas.bind("<Motion>", self.preview)
        
        # self.missileCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        # self.missileCanvas.pack(side=tk.LEFT)
        # self.missileCanvas.create_rectangle(0,0,self.caseSize*self.boardSize,self.caseSize*self.boardSize, fill="grey")
        self.initBoard()
        self.drawBoard()

    def clickToShoot(self, event):
        caseX, caseY = self.canvasToBoard((event.x, event.y))

        if self.game.TryShootAt(Vector2d(caseX, caseY)):
            self.hitTiles.append(Vector2d(caseX, caseY))
        else:
            self.waterTiles.append(Vector2d(caseX, caseY))

        self.drawBoard()

    def drawBoard(self):
        for lign in range(self.boardSize):
            for row in range(self.boardSize):
                color = "red" if (row, lign) in self.hitTiles else "blue" if (row, lign) in self.waterTiles else self.colors[(lign%2+row%2)%2]
                self.canvas.itemconfig(self.tiles[lign][row], fill=color)
                    
    def initBoard(self):
        for lign in range(self.boardSize):
            self.tiles.append([])
            for row in range(self.boardSize):
                x=row*self.caseSize
                y=lign*self.caseSize
                self.tiles[lign].append(self.canvas.create_rectangle(x,y,x+self.caseSize,y+self.caseSize))
