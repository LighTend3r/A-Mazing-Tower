import maze.Maze as Maze
import maze.MultiMaze as MultiMaze
from typing import List, Tuple
import random
import sys

sys.setrecursionlimit(1_000_000)

class MakeMaze:
    def __init__(self, wall: int | str = 1, floor: int | str = 0, coin: int | str = 2, debug:int = 0):
        self.__wall = wall
        self.__floor = floor
        self.__coin = coin
        self.__debug = debug


    def setFloor(self, floor: int | str):
        """Modifie l'objet qui représente le sol
        """

        self.__floor = floor

    def setWall(self, wall: int | str):
        """Modifie l'objet qui représente un mur
        """
        self.__wall = wall

    def setCoin(self, coin: int | str):
        """Modifie l'objet qui représente un coin
        """
        self.__coin = coin


    def makeMultiMaze(self, row:int = 1, column:int = 1, taille_row:int = 10, taille_column:int = 10, p: int = 0) -> MultiMaze:
        """Créé un labyrinthe avec des labyrinthes plus petit

        Args:
            row (int, optional): Nombre de labyrinthe en ligne. Defaults to 1.
            column (int, optional): Nombre de labyrinthe en colonne. Defaults to 1.
            taille_row (int, optional): La taille des lignes de chaque petit labyrinthe. Defaults to 10.
            taille_column (int, optional): La taille des colonnes de chaque petit labyrinthe. Defaults to 10.
            p (int, optional): Probabilité de supprimer des murs dans le labyrinthe. Defaults to 0.

        Returns:
            MultiMaze: Retourne un labyrinthe avec des labyrinthes plus petit
        """

        assert p >= 0 and p <= 100, "p doit être compris entre 0 et 100 (c'est une probabilité)"
        assert row > 0 and column > 0, "row et column doivent être supérieur à 0"
        assert taille_row > 0 and taille_column > 0, "taille_row et taille_column doivent être supérieur à 0"

        if self.__debug > 0:
            print(taille_row * row + 2 + row-1, taille_column * column + 2 + column-1)

        multiMaze = MultiMaze.MultiMaze(row, column, self.__wall, self.__floor, self.__coin)
        grid = multiMaze.get_grid()


        for i in range(row):
            for j in range(column):
                maze = Maze.Maze(taille_row, taille_column, self.__wall, self.__floor, self.__coin)
                self.__makeMaze(maze)
                if p > 0:
                    nb_wall = self.__countWall(maze)
                    nb_wall_delete = int(nb_wall * (p/100))
                    if self.__debug > 0:
                        print("On supprime", nb_wall_delete, "murs")
                    self.__deleteWall(maze, nb_wall_delete)
                grid[i][j] = maze
        self.__set_minimum_portal(multiMaze)
        multiMaze.set_grid(grid)


        return multiMaze

    def set_random_coin(self, multiMaze: MultiMaze, nb_coin: int = 1, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        """Place des pièces aléatoirement dans le labyrinthe
        """
        while nb_coin > 0:
            x = random.randint(0, multiMaze.get_row()-1)
            y = random.randint(0, multiMaze.get_column()-1)
            self.__set_random_coin_on_one_maze(multiMaze.get_maze(x,y), 1, plan)
            nb_coin -= 1

    def set_random_portal(self, multiMaze: MultiMaze, nb_portal: int = 1, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        """Place des portails aléatoirement dans le labyrinthe
        """
        assert multiMaze.get_row() > 1 or multiMaze.get_column() > 1, "Le labyrinthe doit avoir au moins 2 labyrinthes"

        while nb_portal > 0:
            x:int = random.randint(0, multiMaze.get_row()-1)
            y:int = random.randint(0, multiMaze.get_column()-1)
            x2:int = random.randint(0, multiMaze.get_row()-1)
            y2:int = random.randint(0, multiMaze.get_column()-1)
            while x == x2 and y == y2:
                x2 = random.randint(0, multiMaze.get_row()-1)
                y2 = random.randint(0, multiMaze.get_column()-1)
            self.__set_random_portal_on_one_maze(multiMaze.get_maze(x,y), 1, plan)
            nb_portal -= 1

    def __set_minimum_portal(self, multiMaze: MultiMaze, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        if multiMaze.get_row() == 1 and multiMaze.get_column() == 1:
            return
        all_link = self.__create_all_link(multiMaze.get_row(), multiMaze.get_column())
        if self.__debug > 0:
            print(all_link)
        for link in all_link:
            x1, y1 = link[0] // multiMaze.get_column(), link[0] % multiMaze.get_column()
            x2, y2 = link[1] // multiMaze.get_column(), link[1] % multiMaze.get_column()
            if self.__debug > 0:
                print(x1, y1, x2, y2)
            marker = multiMaze.get_next_portal_number()
            self.__set_random_portal_on_one_maze(multiMaze.get_maze(x1,y1), marker, plan)
            self.__set_random_portal_on_one_maze(multiMaze.get_maze(x2,y2), marker, plan)


    def __create_all_link(self, row: int, column: int) -> List[Tuple[int, int]]:
        x = random.randint(0, row-1 + column)
        y = random.randint(0, row-1 + column)
        while x == y:
            y = random.randint(0, row-1 + column)

        ensemble = set([x,y])
        ensemble_restant = set(range(row*column)) - ensemble
        link = [(x,y)]

        while len(ensemble) < row*column:
            x = random.choice(list(ensemble))
            y =  random.choice(list(ensemble_restant))

            ensemble.add(y)
            link.append((x,y))

            ensemble_restant = ensemble_restant - set([y])
        return link

    def __set_random_portal_on_one_maze(self, maze: Maze, marker: int | str, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        start_x = 0 if plan[0][0] == -1 else plan[0][0]
        start_y = 0 if plan[0][1] == -1 else plan[0][1]
        end_x = maze.get_row()-1 if plan[1][0] == -1 else plan[1][0]
        end_y = maze.get_column()-1 if plan[1][1] == -1 else plan[1][1]

        placed = False
        while not placed:
            x = random.randint(start_x, end_x-1)
            y = random.randint(start_y, end_y-1)
            if maze.get_grid()[x][y] == self.__floor:
                maze.get_grid()[x][y] = marker
                placed = True

    def __set_random_portal_on_two_maze(self, maze1: Maze, maze2: Maze, marker: int | str, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        start_x:int = 0 if plan[0][0] == -1 else plan[0][0]
        start_y:int = 0 if plan[0][1] == -1 else plan[0][1]
        end_x:int = maze1.get_row()-1 if plan[1][0] == -1 else plan[1][0]
        end_y:int = maze1.get_column()-1 if plan[1][1] == -1 else plan[1][1]


        portal1_placed: bool = False
        portal2_placed: bool = False
        while not portal1_placed:
            x:int = random.randint(start_x, end_x-1)
            y:int = random.randint(start_y, end_y-1)
            if maze1.get_grid()[x][y] == self.__floor:
                maze1.get_grid()[x][y] = marker
                portal1_placed = True

        while not portal2_placed:
            x:int = random.randint(start_x, end_x-1)
            y:int = random.randint(start_y, end_y-1)
            if maze2.get_grid()[x][y] == self.__floor:
                maze2.get_grid()[x][y] = marker
                portal2_placed = True




    def __set_random_coin_on_one_maze(self, maze: Maze, nb_coin: int, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        start_x = 0 if plan[0][0] == -1 else plan[0][0]
        start_y = 0 if plan[0][1] == -1 else plan[0][1]
        end_x = maze.get_row()-1 if plan[1][0] == -1 else plan[1][0]
        end_y = maze.get_column()-1 if plan[1][1] == -1 else plan[1][1]

        while nb_coin > 0:
            x = random.randint(start_x, end_x-1)
            y = random.randint(start_y, end_y-1)
            if maze.get_grid()[x][y] == self.__floor:
                maze.get_grid()[x][y] = self.__coin
                nb_coin -= 1

    def __deleteWall(self, maze: Maze, nb_wall_delete:int, plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        start_x = 0 if plan[0][0] == -1 else plan[0][0]
        start_y = 0 if plan[0][1] == -1 else plan[0][1]
        end_x = maze.get_row()-1 if plan[1][0] == -1 else plan[1][0]
        end_y = maze.get_column()-1 if plan[1][1] == -1 else plan[1][1]
        while nb_wall_delete > 0:
            x = random.randint(start_x, end_x-1)
            y = random.randint(start_y, end_y-1)
            if maze.get_grid()[x][y] == self.__wall:

                coo = [(1,0), (-1,0), (0,1), (0,-1)]
                possible = False
                for co in coo:
                    x_new = x + co[0]
                    y_new = y + co[1]
                    if x_new >= start_x and x_new < end_x and y_new >= start_y and y_new < end_y:
                        if maze.get_grid()[x_new][y_new] == self.__floor:
                            possible = True
                            break


                if possible:
                    maze.get_grid()[x][y] = self.__floor
                    nb_wall_delete -= 1


    def __countWall(self, maze: Maze,plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        start_x = 0 if plan[0][0] == -1 else plan[0][0]
        start_y = 0 if plan[0][1] == -1 else plan[0][1]
        end_x = maze.get_row() if plan[1][0] == -1 else plan[1][0]
        end_y = maze.get_column() if plan[1][1] == -1 else plan[1][1]

        count = 0
        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                if maze.get_grid()[i][j] == self.__wall:
                    count += 1
        return count

    def __makeMaze(self, maze: Maze,plan:List[List[int]]=[[-1, -1], [-1, -1]]):
        """Créé un labyrinthe sans boucle

        Args:
            maze (Maze): Labyrinthe à modifier
        """

        start_x = 0 if plan[0][0] == -1 else plan[0][0]
        start_y = 0 if plan[0][1] == -1 else plan[0][1]
        end_x = maze.get_row() if plan[1][0] == -1 else plan[1][0]
        end_y = maze.get_column() if plan[1][1] == -1 else plan[1][1]


        x_start = random.randint(start_x,end_x-1)
        y_start = random.randint(start_y,end_y-1)

        self.__makeMazeRecursif(maze, [[x_start, y_start]], start_x, start_y, end_x, end_y)

    def __makeMazeRecursif(self, maze: Maze, pile: List[List[int]], start_x:int = 0, start_y:int = 0, end_x:int = -1, end_y:int = -1):
        if len(pile) == 0:
            return

        grid: List[List[str]] = maze.get_grid()

        x, y = pile[-1]

        coo = [(1,0), (-1,0), (0,1), (0,-1)]
        coo_possible = []
        for co in coo:
            x_new = x + co[0]
            y_new = y + co[1]
            if x_new >= start_x and x_new < end_x and y_new >= start_y and y_new < end_y:
                correct = False
                if grid[x_new][y_new] == self.__wall:
                    correct = True
                    nb_void = 0
                    for co2 in coo:
                        x_check = x_new + co2[0]
                        y_check = y_new + co2[1]
                        if x_check >= start_x and x_check < end_x and y_check >= start_y and y_check < end_y:
                            if grid[x_check][y_check] == self.__floor:
                                nb_void += 1

                if correct and nb_void <= 1:
                    coo_possible.append([x_new, y_new])

        if len(coo_possible) > 0:
            new_random_coo = random.randint(0,len(coo_possible)-1)
            x_new, y_new = coo_possible[new_random_coo]
            grid[x_new][y_new] = self.__floor
            pile.append([x_new, y_new])
            self.__makeMazeRecursif(maze, pile, start_x, start_y, end_x, end_y)
        else:
            pile.pop()
            self.__makeMazeRecursif(maze, pile, start_x, start_y, end_x, end_y)



    def makeMaze2(self, maze: Maze):
        pass

