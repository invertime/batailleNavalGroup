from classes.vector2d import Vector2d
from classes.Boat import Boat

class gameSex_sixenlatin_Mecanic_bytesManager:
    sizes = [5, 4, 4, 3, 3, 2, 2]
    dir: Vector2d = Vector2d(0, 1)
    boats: list[Boat] = []

    def PreviewBoatLocation(self, board, pos: Vector2d, sizeIndex: int) -> list[Vector2d]:
        temp = pos
        liste = []
        dir = self.dir
        for i in range(self.sizes[sizeIndex]):
            if (temp.x >= board.boardSize or temp.y >= board.boardSize or temp.x < 0 or temp.y < 0):
                dir = Vector2d(0, 0) - dir
                temp = pos + dir
            
            liste.append(temp)
                
            temp += dir

        return liste

    def Rotate(self):
        if self.dir.y == 1:
            self.dir = Vector2d(1, 0)
        elif self.dir.x == 1:
            self.dir = Vector2d(0, -1)
        elif self.dir.y == -1:
            self.dir = Vector2d(-1, 0)
        else:
            self.dir = Vector2d(0, 1)