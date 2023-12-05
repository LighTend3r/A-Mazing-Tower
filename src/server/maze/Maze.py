from typing import List


class Maze:
    def __init__(self, row:int, column:int, wall: int | str, floor: int | str, coin: int | str):
        self.__column: int = column
        self.__row: int = row
        self.__grid: List[List[int|str]] = [[wall for _ in range(column)] for _ in range(row)]
        self.__wall: int | str = wall
        self.__floor: int | str = floor
        self.__coin: int | str = coin

    def get_column(self) -> int:
        """Récupère le nombre de colonne
        """
        return self.__column

    def get_row(self) -> int:
        """Récupère le nombre de ligne
        """
        return self.__row

    def get_grid(self) -> List[List[int|str]]:
        """Récupère la grille de labyrinthe
        """
        return self.__grid

    def get_wall(self) -> int|str:
        """Récupére l'objet qui représente un mur
        """
        return self.__wall

    def get_floor(self) -> int|str:
        """Récupére l'objet qui représente le sol
        """
        return self.__floor

    def get_coin(self) -> int|str:
        """Récupére l'objet qui représente un coin
        """
        return self.__coin

    def set_tile(self, x:int, y:int, tile:int|str) -> None:
        """Modifie une case de la grille
        """
        self.__grid[x][y] = tile

    def get_tile(self, x:int, y:int) -> int|str:
        """Récupère une case de la grille
        """
        return self.__grid[x][y]

    def __str__(self):
        msg = ""
        for i in self.get_grid():
            for j in i:
                msg += str(j) + " "
            msg += "\n"
        return msg
