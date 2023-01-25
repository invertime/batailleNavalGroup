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
        self.window.after(0, self.waitJob)
        self.window.update()

    def waitJob(self):
        waitCondition = self.waitOtherPlayerToConnect
        while not waitCondition:
            print("waiting")
        if(waitCondition):
            self.window.destroy()