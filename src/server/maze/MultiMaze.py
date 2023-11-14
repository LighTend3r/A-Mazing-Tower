import maze.Maze as Maze
from typing import List

class MultiMaze:
    def __init__(self, row:int, column:int, wall: int | str, floor: int | str, coin: int | str):
        self.__column: int = column
        self.__row: int = row
        self.__grid: List[List[Maze.Maze]] = [[None for _ in range(column)] for _ in range(row)]
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

    def get_grid(self)->List[List[Maze.Maze]]:
        """Récupère la grille de labyrinthe
        """
        return self.__grid

    def get_wall(self) -> int | str:
        """Récupére l'objet qui représente un mur
        """
        return self.__wall

    def get_floor(self) -> int | str:
        """Récupére l'objet qui représente le sol
        """
        return self.__floor

    def set_grid(self, grid: List[List[Maze.Maze]]) -> None:
        """Modifie la grille de labyrinthe
        """
        self.__grid = grid

    def get_maze(self, x:int, y:int) -> Maze.Maze:
        """Récupère un labyrinthe en position x,y
        """
        return self.__grid[x][y]

    def get_all_row(self) -> int:
        """Récupère le nombre de ligne de la grille de labyrinthe complèter par les sous-labyrinthes
        """
        return self.get_maze(0,0).get_row() * self.get_row() + 2 + self.get_row()-1

    def get_all_column(self) -> int:
        """Récupère le nombre de colonne de la grille de labyrinthe complèter par les sous-labyrinthes
        """
        return self.get_maze(0,0).get_column() * self.get_column() + 2 + self.get_column()-1

    def get_all_maze(self) -> List[List[int]]:
        """Récupère la grille de labyrinthe complèter par les sous-labyrinthes
        """
        taille_petit_maze_x = self.get_maze(0,0).get_row()
        taille_petit_maze_y = self.get_maze(0,0).get_column()

        big_x = taille_petit_maze_x * self.get_row() + 2 + self.get_row()-1
        big_y = taille_petit_maze_y * self.get_column() + 2 + self.get_column()-1
        big_grid = [[None for _ in range(big_y)] for _ in range(big_x)]

        for i in range(1,big_x, taille_petit_maze_x+1):
            for j in range(1,big_y, taille_petit_maze_y+1):
                x = int((i-1)/(taille_petit_maze_x+1))
                y = int((j-1)/(taille_petit_maze_y+1))
                grid = self.get_maze(x,y).get_grid()

                for k in range(taille_petit_maze_x):
                    for l in range(taille_petit_maze_y):
                        big_grid[i+k][j+l] = grid[k][l]
        for i in range(big_x):
            for j in range(big_y):
                if big_grid[i][j] == None:
                    big_grid[i][j] = self.__wall
        return big_grid

    def __str__(self):
        msg = ""
        for i in self.get_all_maze():
            for j in i:
                msg += str(j)
            msg += "\n"
        return msg
