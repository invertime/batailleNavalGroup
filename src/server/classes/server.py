import socket
from classes.Client import Client

class Server:
    def __init__(self, port, host=""):
        self.host = host  # Standard loopback interface address (localhost)
        self.port = port  # Port to listen on (non-privileged ports are > 1023)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None 
        self.addr = None

    def connect(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        
    def accept(self):    
        self.conn, self.addr = self.sock.accept()
        return (self.conn, self.addr)

    def connectionHandler(conn, addr, client: Client):    
        data = ""
        print(f"Connected by {addr}")
        while True:
            data: str = conn.recv(1024).decode("utf8")
            if not data:
                break

            command = int(data[0])
            parsed = data[2:-1]

            if command == 0:
                print("Boats received: " + parsed)
                client.boats = dataArrayParser(data[1:])
                conn.sendall(bytes(data, "utf8"))
            elif command == 1:
                print("user shot at ", data[1:])
                flattenBoatList = [item for sublist in client.boats for item in sublist]
                if dataTuppleParser(parsed) in flattenBoatList:
                    print("Boat touched")
                    conn.sendall(b"1")
                else:
                    print("Boat missed")
                    conn.sendall(b"0")
            else:
                conn.sendall(b"error processing data")

    def kickHandler(conn, addr):
        print(addr, "kicked")
        conn.sendall(b"noConnect")


def dataArrayParser(byteStringArray):
    byteStringArray = byteStringArray[2:-2]
    arrayStart = False
    tuppleStart = False
    tuppleBuffer = []
    tuppleArrayBuffer = []
    finalArray = []
    for i in byteStringArray:
        if(i == '['):
            arrayStart=True
        elif (i == ']'):
            arrayStart=False
            finalArray.append(tuppleArrayBuffer)
            tuppleArrayBuffer=[]
        elif(i == '('):
            tuppleStart=True
        elif(i == ')'):
            tuppleStart=False
            tuppleArrayBuffer.append((tuppleBuffer[0],tuppleBuffer[1]))
            tuppleBuffer=[]

        elif(arrayStart):
            if(tuppleStart):
                if (i.isnumeric()):
                    tuppleBuffer.append(int(i))

    return finalArray

def dataTuppleParser(byteStringTupple):
    tuppleBuffer = []
    for i in byteStringTupple:
        if (i.isnumeric()):
            tuppleBuffer.append(int(i))
    return (tuppleBuffer[0],tuppleBuffer[1])