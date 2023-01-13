from typing import NewType
from classes.vector2d import Vector2d

class Boat :
    __cells: list[Vector2d]
    __hpLost: int

    def __init__(self, __cells: list[Vector2d]) -> None:
        self.__cells = __cells
        self.__hpLost = 0

    def __repr__(self) -> str:
        return f"{self.__cells}"

    def getCells(self):
        return self.__cells

    def TryAttack(self, cell: Vector2d) -> bool:
        if (cell in self.__cells):
            self.__hpLost += 1
            return True

        return False

    def IsDed(self) -> bool:
        return self.__hpLost == len(self.__cells)