import socket
from classes.Vector2d import Vector2d


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

    def sendMissile(self, position: tuple[int,int]) -> tuple[int, int|list[Vector2d]]:
        self.sock.sendall(bytes("1" + str([position]), "utf8"))
        data = self.sock.recv(1024)
        print(f"Received {data!r}")

        parsedData: tuple[int,int] = dataTuppleParser(data)

        print("touched: ",parsedData[0],"boat destroyed:", parsedData == 0)

        return parsedData

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


def dataTuppleParser(byteStringTupple):
    stringTuple: str = byteStringTupple.decode("utf8")
    stringTuple = stringTuple.replace(" ", "")
    tuppleBuffer = []
    finalArray = []
    tuppleStart = False
    arrayStart = False

    for i in stringTuple:
        if i == "(":
            tuppleStart = True
        elif i == ")":
            finalArray.append(tuppleBuffer[0]) if len(tuppleBuffer) == 1 else finalArray.append(tuppleBuffer)
            tuppleStart = False
        elif tuppleStart:
            if i=="[":
                arrayStart = True
                start = stringTuple.index(i)
                end = stringTuple.index("]")
                tuppleBuffer.append(dataArrayParser(stringTuple[start: end+1]))
            elif arrayStart:
                if i=="]":
                    arrayStart = False
            elif i == ",":
                if len(tuppleBuffer) == 1:
                    finalArray.append(tuppleBuffer[0])
                else:
                    finalArray.append(tuppleBuffer)
                tuppleBuffer = []
            else:
                if i.isnumeric():
                    tuppleBuffer.append(int(i))
                else:
                    tuppleBuffer.append(i)

        # if (type(i) == int or i.isnumeric()):
        #     tuppleBuffer.append(int(i))
    return (finalArray[0],finalArray[1])

def dataArrayParser(byteStringArray):

    startArray = False
    startVector2D = False
    vector2dBuffer = []
    finalArray = []

    for i in byteStringArray:
        if i == "[":
            startArray = True
        elif i == "]":
            startArray = False
        elif startArray:
            if i == "(":
                startVector2D = True
            elif i == ")":
                startVector2D = False
                finalArray.append(Vector2d(vector2dBuffer[0],vector2dBuffer[1]))
            elif startVector2D:
                if i.isnumeric():
                    vector2dBuffer.append(int(i))

    return finalArray
