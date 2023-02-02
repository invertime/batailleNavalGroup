import tkinter as tk
import time
import socket
from classes.PlaceBoard import PlaceBoard
from classes.ShootBoard import ShootBoard
from classes.Vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSex_sixenlatin_Mecanic_bytesManager, gameSexMechanicV2, MainGameMechanic
import os

class Window:

    window, boatCanvas, missileCanvas, placeBoatGame, shootGame, boatKilledCounterWrapper, boatKilledCounter = None, None, None, None, None, None, None
    tiles: list[list[int]]    

    def __init__(self, bsize, csize):
        self.boardSize = bsize
        self.caseSize = csize
        

    def create(self, sendBoatLocation, sendMissile, waitFunc, waitOtherPlayerToSendBoats):
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", lambda: os.kill(os.getpid(), 9))

        self.boatKilledCounter = tk.IntVar()
        self.boatKilledCounter.set(0)

        self.boatKilledCounterWrapper = tk.StringVar()
        self.boatKilledCounterWrapper.set("Boat killed:"+str(self.boatKilledCounter.get()))

        self.boatKilledCounter.trace('w', self.setboatKilledCounterWrapperReactivity)

        self.mainGameMechanics = MainGameMechanic()

        self.placeBoatGame = gameSex_sixenlatin_Mecanic_bytesManager()

        self.boatCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.boatCanvas.grid(row=0, column=0, columnspan=2)        
        self.placeBoard = PlaceBoard(self.boatCanvas, self.placeBoatGame, self.boardSize, self.caseSize, sendBoatLocation)
        self.placeBoard.create()
       
        SendBoatLocationButton = tk.Button(self.window, text="Send your boats location", command=lambda: self.sendFuncHandler(sendBoatLocation, waitOtherPlayerToSendBoats))
        SendBoatLocationButton.grid(row=1, column=0, columnspan=2)

        # BoatGreyAllButton = tk.Button(self.window, text="Everything grey", command=self.switchToShootHandler)
        # BoatGreyAllButton.grid(row=1,column=1)

        self.shootGame = gameSexMechanicV2(sendMissile, waitFunc)

        self.missileCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.missileCanvas.grid(row=0, column=2, columnspan=2) 

        self.shootBoard = ShootBoard(self.missileCanvas, self.shootGame, self.boardSize, self.caseSize, self.boatKilledCounter)
        self.shootBoard.initBoard()
        
        SendBoatLocationButton = tk.Button(self.window, text="dont click if ur not a dev", command=self.shootBoard.Nuke)
        SendBoatLocationButton.grid(row=1, column=2)

        boatKilledLabel = tk.Label(self.window, textvariable=self.boatKilledCounterWrapper, fg="black")
        boatKilledLabel.grid(row=1, column=3)

        self.window.mainloop()

    def sendFuncHandler(self, sendBoatLocation, waitOtherPlayer):
        if not self.placeBoard.game.sizes:
            sendBoatLocation(self.placeBoard.boats)
            id = waitOtherPlayer()
            self.switchToShootHandler(id == 0)
        else:
            self.placeBoard._pass(None)

    def switchToShootHandler(self, isFirst: bool):
        shootModeEnabled = self.mainGameMechanics.switchToShoot()
        if shootModeEnabled and self.placeBoard.everyBoatsPlaced:
            self.placeBoard.greyAll()
            self.shootBoard.create(isFirst)

    def setAlert(self, message: str, timeOnDisplay: int):
        print(message)
        self.alert.set(message)
        self.wait(timeOnDisplay)
        self.clearAlert()

    def clearAlert(self):
        self.alert.set("")

    def wait(self, waitDuration):
        time.sleep(waitDuration)

    def setboatKilledCounterWrapperReactivity(self, var, index, mode):
        self.boatKilledCounterWrapper.set("Boat killed:"+str(self.boatKilledCounter.get()))