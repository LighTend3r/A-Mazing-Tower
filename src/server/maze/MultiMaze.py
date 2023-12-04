import maze.Maze as Maze
from typing import List

class MultiMaze:
    _instance = None

    def __new__(cls, row:int, column:int, wall: int | str, floor: int | str, coin: int | str): # Singleton
        if not cls._instance:
            cls._instance = super(MultiMaze, cls).__new__(cls)
        return cls._instance

    def __init__(self, row:int, column:int, wall: int | str, floor: int | str, coin: int | str):
        self.__column: int = column
        self.__row: int = row
        self.__grid: List[List[Maze.Maze]] = [[None for _ in range(column)] for _ in range(row)]
        self.__wall: int | str = wall
        self.__floor: int | str = floor
        self.__coin: int | str = coin
        self.__nbPortal: int = 0
        self.__spawn: List[int] = [0,0]
        self.__nbCoin = 0

    def get_spawn(self) -> List[int]:
        """Récupère la position du spawn
        """
        return self.__spawn

    def set_spawn(self, x:int, y:int) -> None:
        """Modifie la position du spawn
        """
        self.__spawn = [x,y]

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

    def get_coin(self) -> int | str:
        """Récupére l'objet qui représente un coin
        """
        return self.__coin

    def get_nbCoin(self) -> int:
        """Récupére le nombre de coin
        """
        return self.__nbCoin

    def set_nbCoin(self, nbCoin:int) -> None:
        """Modifie le nombre de coin
        """
        self.__nbCoin = nbCoin

    def set_grid(self, grid: List[List[Maze.Maze]]) -> None:
        """Modifie la grille de labyrinthe
        """
        self.__grid = grid

    def get_maze(self, x:int, y:int) -> Maze.Maze:
        """Récupère un labyrinthe en position x,y
        """
        return self.__grid[x][y]

    def get_nb_portal(self) -> int:
        """Récupère le nombre de portail
        """
        return self.__nbPortal

    def get_next_portal_number(self) -> int | str:
        """Récupère le prochain numéro de portail
        """
        self.__nbPortal += 1
        if type(self.__wall) == int:
            return max(self.__wall, self.__floor, self.__coin) + self.__nbPortal


        return "P" + str(self.__nbPortal)

    def get_all_portal_name(self) -> List[str|int]:
        """Récupère tout les noms de portail
        """
        if type(self.__wall) == int:
            mini = max(self.__wall, self.__floor, self.__coin) +1
            return [i for i in range(mini, mini + self.__nbPortal)]
        return ["P" + str(i) for i in range(self.__nbPortal)]


    def get_all_row(self) -> int:
        """Récupère le nombre de ligne de la grille de labyrinthe complèter par les sous-labyrinthes
        """
        return self.get_maze(0,0).get_row() * self.get_row() + 2 + self.get_row()-1

    def get_all_column(self) -> int:
        """Récupère le nombre de colonne de la grille de labyrinthe complèter par les sous-labyrinthes
        """
        return self.get_maze(0,0).get_column() * self.get_column() + 2 + self.get_column()-1

    def get_tile(self, x:int , y:int) -> int | str:
        # TODO: On pourrait accélérer la recherche en utilisant la position du labyrinthe
        """Récupère la tuile en position x,y
        """
        return self.get_all_maze()[x][y]

    def set_tile(self, x:int , y:int, tile:int | str) -> None:
        """Modifie la tuile en position x,y
        """
        x = x - 1
        y = y - 1

        grid_x = int(x / (self.get_maze(0,0).get_row()+1))
        grid_y = int(y / (self.get_maze(0,0).get_column()+1))

        self.__grid[grid_x][grid_y].set_tile(x % (self.get_maze(0,0).get_row()+1), y % (self.get_maze(0,0).get_column()+1), tile)

    def get_other_portal(self, x:int, y:int) -> int | str:
        """Récupère le numéro de l'autre portail
        """
        portal_name = self.get_tile(x,y)
        if portal_name in self.get_all_portal_name():
            return self.__find_other_portal(x,y,portal_name)
        return None, None

    def __find_other_portal(self, x:int, y:int, portal_name:int | str) -> tuple[int, int]:
        """Récupère la position de l'autre portail
        """
        for i in range(self.get_all_row()):
            for j in range(self.get_all_column()):
                if self.get_tile(i,j) == portal_name and (i,j) != (x,y):
                    return i,j
        return None, None

    def get_all_maze(self) -> List[List[int]]:
        """Récupère la grille de labyrinthe complèter par les sous-labyrinthes
        """
        taille_petit_maze_x:int = self.get_maze(0,0).get_row()
        taille_petit_maze_y:int = self.get_maze(0,0).get_column()

        big_x:int = taille_petit_maze_x * self.get_row() + 2 + self.get_row()-1
        big_y:int = taille_petit_maze_y * self.get_column() + 2 + self.get_column()-1
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
                msg += str(j) + " "
            msg += "\n"
        return msg
