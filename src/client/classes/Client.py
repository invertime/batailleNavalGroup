import socket


class Client:
    def __init__(self,host,port):
        self.HOST = host  # The server's hostname or IP address
        self.PORT = port  # The port used by the server

    def create(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))

    def sendTest(self) -> socket:
        self.sock.sendall(b"test")
        data = self.sock.recv(1024)
        return data

    def sendBoatLocation(self,boatCase) -> None:
        if not len(boatCase): return 
        self.sock.sendall(bytes(str([boatCase]), "utf8"))
        data = self.sock.recv(1024)
        print(f"Received {data!r}")

    def sendKill(self) -> None:
        print("kill yourself pls")
        self.sock.sendall(b"killYourself69")
        data = self.sock.recv(1024)
        if (data==b"killed"):
            exit()