

class Client:
    boats: list[tuple[int, int]]

    def __init__(self, boats: list[tuple[int, int]]) -> None:
        self.boats: list[tuple[int, int]] = boats