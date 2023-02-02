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
    killedBoatsCases: list[Vector2d] = []
 
    def __init__(self, canvas, game, bSize, cSize, boatKilledCounter: tk.IntVar):
        self.canvas = canvas
        self.game = game
        self.boardSize: int = bSize
        self.caseSize: int = cSize
        self.tiles = []
        self.colors: list[str] = ["white","black"]
        self.boatKilledCounter = boatKilledCounter

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
            tryShootResponse = self.game.TryShootAt(v)
            if tryShootResponse[0]:
                self.hitTiles.append(v)
                if tryShootResponse[1] != 0:
                    print(tryShootResponse[1])
                    self.killedBoatsCases += tryShootResponse[1]
                    print(self.killedBoatsCases)
                    self.boatKilledCounter.set(self.boatKilledCounter.get() + 1)
                if tryShootResponse[0] == 2:
                    self.disableControls()
                    self.drawBoard()
                    self.drawWinBoard()
                    return
            else:
                self.waterTiles.append(v)

        self.drawBoard()

        self.disableControls()
        threading.Thread(target=self.waitThenReturnControls).start()

    def waitThenReturnControls(self):
        if not self.game.waitForTurn():
            self.enableControls()
        else:
            self.drawLoseBoard()

    def Nuke(self):
        self.disableControls()

        dontShootThere = self.hitTiles + self.waterTiles
        for x in range(10):
            for y in range(10):
                v = Vector2d(x, y)
                if not v in dontShootThere:
                    tryShootResponse = self.game.TryShootAt(v)
                    if tryShootResponse[0]:
                        self.hitTiles.append(v)
                        if tryShootResponse[1] != 0:
                            self.killedBoatsCases += tryShootResponse[1]
                            self.boatKilledCounter.set(self.boatKilledCounter.get() + 1)
                    else:
                        self.waterTiles.append(v)

                self.drawBoard()

                # wait for next turn
                if self.game.waitForTurn():
                    self.drawLoseBoard()

        self.drawWinBoard()

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
                v = Vector2d(row, lign)
                color = "brown" if v in self.killedBoatsCases else "red" if v in self.hitTiles else "blue" if v in self.waterTiles else self.colors[(lign%2+row%2)%2]
                self.canvas.itemconfig(self.tiles[lign][row], fill=color)

    def drawWinBoard(self):
        self.drawPicture([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
        ])

    def drawLoseBoard(self):
        a = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
        ]
        a.reverse()
        self.drawPicture(a)

    def drawPicture(self, drawing):
        colors = ["", "red", "cyan"]
        for lign in range(self.boardSize):
            for row in range(self.boardSize):
                color = colors[drawing[lign][row]]
                if color != "":
                    self.canvas.itemconfig(self.tiles[lign][row], fill=color)
                    
    def initBoard(self):
        for lign in range(self.boardSize):
            self.tiles.append([])
            for row in range(self.boardSize):
                x=row*self.caseSize
                y=lign*self.caseSize
                self.tiles[lign].append(self.canvas.create_rectangle(x,y,x+self.caseSize,y+self.caseSize, fill="grey"))
