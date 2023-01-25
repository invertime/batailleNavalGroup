class Client:
    boats: list[tuple[int, int]] = None
    conn,addr = None, None
    isReady:bool = False
    id = None

    def __init__(self, conn, addr, boats: list[tuple[int, int]]) -> None:
        self.conn = conn
        self.addr = addr
        self.boats: list[tuple[int, int]] = boats

    def setReady(self):
        self.isReady = True