import tkinter as tk
import time
import socket
from classes.PlaceBoard import PlaceBoard
from classes.ShootBoard import ShootBoard
from classes.Vector2d import Vector2d
from classes.gamemachinemanagercontrollersextoyinputreceiver_itCanVibrateOfCourse import gameSex_sixenlatin_Mecanic_bytesManager, gameSexMechanicV2, MainGameMechanic

class Window:

    window, boatCanvas, missileCanvas, placeBoatGame, shootGame, alert = None, None, None, None, None, None
    tiles: list[list[int]]    

    def __init__(self, bsize, csize, sendFunc: str, killFunc, sendTest):
        self.boardSize = bsize
        self.caseSize = csize
        self.sendFunc = sendFunc
        self.killFunc = killFunc
        self.sendTest = sendTest

    def create(self):
        self.window = tk.Tk()

        self.alert = tk.StringVar()
        self.alert.set("AAAAH")

        self.mainGameMechanics = MainGameMechanic()

        self.placeBoatGame = gameSex_sixenlatin_Mecanic_bytesManager()

        self.boatCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.boatCanvas.grid(row=0, column=0, columnspan=2)        
        self.placeBoard = PlaceBoard(self.boatCanvas, self.placeBoatGame, self.boardSize, self.caseSize, self.sendFunc, self.killFunc, self.sendTest)
        self.placeBoard.create()
       
        SendBoatLocationButton = tk.Button(self.window, text="Send your boats location", command=lambda: self.placeBoard.sendFunc(self.boats) if not self.placeBoard.game.sizes else self.placeBoard._pass("you momma"))
        SendBoatLocationButton.grid(row=1, column=0)

        BoatGreyAllButton = tk.Button(self.window, text="Everything grey", command=self.switchToShootHandler)
        BoatGreyAllButton.grid(row=1,column=1)

        self.shootGame = gameSexMechanicV2()

        self.missileCanvas = tk.Canvas(self.window,width=self.caseSize*self.boardSize,height=self.caseSize*self.boardSize)
        self.missileCanvas.grid(row=0, column=2, columnspan=2) 
        self.shootBoard = ShootBoard(self.missileCanvas, self.shootGame, self.boardSize, self.caseSize, self.sendFunc, self.killFunc, self.sendTest)
        self.shootBoard.initBoard()

        testButton = tk.Button(self.window, text="Click Me!", command=lambda: self.setAlert("test", .8))
        testButton.grid(row=1, column=2)

        testLabel = tk.Label(self.window, textvariable=self.alert, fg="black")
        testLabel.grid(row=1, column=3)

        self.window.mainloop()

    def switchToShootHandler(self):
        shootModeEnabled = self.mainGameMechanics.switchToShoot()
        if shootModeEnabled:
            self.placeBoard.greyAll()
            self.shootBoard.create()

    def setAlert(self, message: str, timeOnDisplay: int):
        print(message)
        self.alert.set(message)
        self.wait(timeOnDisplay)
        self.clearAlert()

    def clearAlert(self):
        self.alert.set("")

    def wait(self, waitDuration):
        time.sleep(waitDuration)