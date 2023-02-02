class Client:
    boats: list[list[tuple[int,int]]] = None
    conn,addr = None, None
    pseudo: str
    isReady:bool = False
    id = None
    canShoot = False
    touchedCases: list[list[tuple[int,int]]] = []
    win = False

    def __init__(self, conn, addr, pseudo, boats: list[tuple[int, int]]) -> None:
        self.conn = conn
        self.addr = addr
        self.boats: list[tuple[int, int]] = boats
        self.pseudo = pseudo

    def setReady(self):
        self.isReady = True

    def toggleCanShoot(self):
        self.canShoot = not self.canShoot