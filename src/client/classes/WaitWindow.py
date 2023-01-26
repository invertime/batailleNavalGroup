import threading
import tkinter as tk

class WaitWindow:
    loopActive = True

    def __init__(self):
        pass

    def create(self, waitOtherPlayerToConnect):
        self.window = tk.Tk()
        self.waitOtherPlayerToConnect = waitOtherPlayerToConnect
        waiting = tk.Label(text="waiting the other player...")
        waiting.pack()
        threading.Thread(target = self.waitJob).run()
        self.window.update()

    def waitJob(self):
        # waitCondition = self.waitOtherPlayerToConnect()
        # while not waitCondition:
        #     print("waiting")
        waitCondition = self.waitOtherPlayerToConnect()
        while not waitCondition:
            pass
        self.window.destroy()