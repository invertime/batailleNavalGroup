import socket


class Client:
    def __init__(self,host,port):
        self.HOST = host  # The server's hostname or IP address
        self.PORT = port  # The port used by the server

    def create(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))

    def sendBoatLocation(self,boatCase) -> bool:
        if not len(boatCase): return 
        self.sock.sendall(bytes("0" + str([boatCase]), "utf8"))
        data = self.sock.recv(1024)
        print(f"Received {data!r}")
        return data == b"0"

    def sendMissile(self, position: tuple[int,int]) -> bool:
        self.sock.sendall(bytes("1" + str([position]), "utf8"))
        data = self.sock.recv(1024)
        print(f"Received {data!r}")

        return data == b"1"

    def waitOtherPlayerToSendBoats(self):
        print("Testing if other client sent his boats...")
        self.sock.sendall(b"2")
        data = self.sock.recv(1024)

        print(f"your id: {int(data)}")

        return int(data) # return the id of this player

    def waitOtherPlayerToConnect(self):
        print("Testing if other client is up...") 
        self.sock.sendall(b"3")
        data = self.sock.recv(1024)

        return data == b"1"
    
    def wait(self):
        print("waiting for turn...")
        self.sock.sendall(b"4")
        self.sock.recv(1024)
        print("u turn !")
