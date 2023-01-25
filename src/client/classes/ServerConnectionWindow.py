import tkinter as tk

class ServerConnectionWindow:
    def __init__(self):
        pass

    def create(self, serverSelecter):
        window = tk.Tk()
        hostLabel = tk.Label(text="Host: ")
        hostLabel.grid(row=0, column=0)
        hostInput = tk.Entry(window)
        hostInput.grid(row=0, column=1)
        portLabel = tk.Label(text="Port: ")
        portLabel.grid(row=1, column=0)
        portInput = tk.Entry(window)
        portInput.grid(row=1, column=1)
        SelectServerButton = tk.Button(window, text="Select server", command=lambda: self.SelectServer(serverSelecter, window, hostInput.get(), portInput.get()))
        SelectServerButton.grid(row=2,column=0,columnspan=1)
        SelectLocalhostServerButton = tk.Button(window, text="Select localhost server", command=lambda: self.SelectServer(serverSelecter, window, "127.0.0.1", "6969"))
        SelectLocalhostServerButton.grid(row=2,column=1,columnspan=1)
        window.mainloop()

    def SelectServer(self,serverSelecter, window: tk, host, port):
        serverSelecter(host, int(port))
        window.destroy()