import tkinter as tk
import socket
from classes.PlaceBoard import PlaceBoard
from classes.ShootBoard import ShootBoard
from classes.Vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSex_sixenlatin_Mecanic_bytesManager, gameSexMechanicV2

class Window:

    window, boatCanvas, missileCanvas, placeBoatGame, shootGame = None, None, None, None, None
    tiles: list[list[int]]

    def __init__(self, bsize, csize, sendFunc: str, killFunc, sendTest):
        self.boardSize = bsize
        self.caseSize = csize
        self.sendFunc = sendFunc
        self.killFunc = killFunc
        self.sendTest = sendTest

    def create(self):
        self.window = tk.Tk()

        self.placeBoatGame = gameSex_sixenlatin_Mecanic_bytesManager()

        self.boatCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.boatCanvas.pack(side=tk.LEFT)        
        placeBoard = PlaceBoard(self.boatCanvas, self.placeBoatGame, self.boardSize, self.caseSize, self.sendFunc, self.killFunc, self.sendTest)
        placeBoard.create()
       
        SendBoatLocationButton = tk.Button(self.window, text="Send your boats location", command=lambda: placeBoard.sendFunc(self.boats) if not placeBoard.game.sizes else self._pass("you momma"))
        SendBoatLocationButton.pack(side=tk.BOTTOM)

        self.shootGame = gameSexMechanicV2()

        self.missileCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.missileCanvas.pack(side=tk.LEFT)
        shootBoard = ShootBoard(self.missileCanvas, self.shootGame, self.boardSize, self.caseSize, self.sendFunc, self.killFunc, self.sendTest)
        shootBoard.create()

        self.window.mainloop()