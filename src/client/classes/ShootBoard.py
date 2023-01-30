import tkinter as tk
import socket
import threading
from classes.Boat import Boat
from classes.Vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSexMechanicV2, MainGameMechanic

class ShootBoard:
    canvas: tk.Canvas = None
    game: gameSexMechanicV2 = None
    hitTiles: list[Vector2d] = []
    waterTiles: list[Vector2d] = []
    oldPreview: Vector2d
    tiles: list[list[int]]
 
    def __init__(self, canvas, game, bSize, cSize):
        self.canvas = canvas
        self.game = game
        self.boardSize: int = bSize
        self.caseSize: int = cSize
        self.tiles = []
        self.colors: list[str] = ["white","black"]

    def canvasToBoard(self, pos: tuple[int, int]) -> tuple[int, int]:
        return pos[0] //self.caseSize, pos[1] //self.caseSize

    def preview(self, event):
        self.drawBoard()

        x, y = self.canvasToBoard((event.x, event.y))
        if not Vector2d(x, y) in (self.hitTiles + self.waterTiles) and x < self.boardSize and y < self.boardSize:
            self.canvas.itemconfig(self.tiles[y][x], fill="green")

        self.oldPreview = Vector2d(event.x // self.caseSize, event.y // self.caseSize)

    def create(self, isFirst):
        if (isFirst):
            self.enableControls()
        else:
            threading.Thread(target=self.waitThenReturnControls).start()

        self.drawBoard()

    def clickToShoot(self, event):
        caseX, caseY = self.canvasToBoard((event.x, event.y))

        v = Vector2d(caseX, caseY)
        if not v in (self.hitTiles + self.waterTiles):
            if self.game.TryShootAt(v)[0]:
                self.hitTiles.append(v)
            else:
                self.waterTiles.append(v)

        self.drawBoard()

        self.disableControls()
        threading.Thread(target=self.waitThenReturnControls).start()

    def waitThenReturnControls(self):
        self.game.waitForTurn()
        self.enableControls()

    def _pass(self, e):
        pass

    def enableControls(self):
        self.canvas.bind("<Button-1>", self.clickToShoot)
        self.canvas.bind("<Motion>", self.preview)

    def disableControls(self):
        self.canvas.bind("<Button-1>", self._pass)
        self.canvas.bind("<Motion>", self._pass)

    def drawBoard(self):
        for lign in range(self.boardSize):
            for row in range(self.boardSize):
                color = "red" if Vector2d(row, lign) in self.hitTiles else "blue" if Vector2d(row, lign) in self.waterTiles else self.colors[(lign%2+row%2)%2]
                self.canvas.itemconfig(self.tiles[lign][row], fill=color)
                    
    def initBoard(self):
        for lign in range(self.boardSize):
            self.tiles.append([])
            for row in range(self.boardSize):
                x=row*self.caseSize
                y=lign*self.caseSize
                self.tiles[lign].append(self.canvas.create_rectangle(x,y,x+self.caseSize,y+self.caseSize, fill="grey"))
