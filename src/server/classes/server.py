import socket

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
        


def connectionHandler(conn, addr):    
    data = ""
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        if(data==b"killYourself69"):
            conn.sendall(b"killed")
            print(conn)
            print(addr)
            exit()
        elif(data==b"test"):
            conn.sendall(b"test yes")
        else:
            conn.sendall(data)

def kickHandler(conn, addr):
    print(addr, "kicked")
    conn.sendall(b"noConnect")