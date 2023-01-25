import socket


class Client:
    def __init__(self,host,port):
        self.HOST = host  # The server's hostname or IP address
        self.PORT = port  # The port used by the server

    def create(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))

    def sendBoatLocation(self,boatCase) -> None:
        if not len(boatCase): return 
        self.sock.sendall(bytes("0" + str([boatCase]), "utf8"))
        data = self.sock.recv(1024)
        print(f"Received {data!r}")
        return 1

    def sendMissile(self, position: tuple[int,int]) -> bool:
        self.sock.sendall(bytes("1" + str([position]), "utf8"))
        data = self.sock.recv(1024)
        print(f"Received {data!r}")

        return data == b"1"

    def waitOtherPlayerToSendBoats(self):
        print("Testing if other client sent his boats...")
        self.sock.sendall(b"2")
        data = self.sock.recv(1024)
        if data == b"1":
            print(f"Player sent his boats")

        return data == b"1"

    def waitOtherPlayerToConnect(self):
        print("Testing if other client is up...") 
        self.sock.sendall(b"3")
        data = self.sock.recv(1024)
        if data == b"1":
            print("Other client is up!") 

        return data == b"1"
    
