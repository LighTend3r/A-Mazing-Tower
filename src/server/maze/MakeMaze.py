import maze.Maze as Maze
import maze.MultiMaze as MultiMaze
from typing import List
import random
import sys

sys.setrecursionlimit(1000000)

class MakeMaze:
    def __init__(self, wall = 1, floor = 0, debug:int = 0):
        self.__wall = wall
        self.__floor = floor
        self.__debug = debug

    def setFloor(self, floor):
        self.__floor = floor

    def setWall(self, wall):
        self.__wall = wall

    def makeMultiMaze(self, taille_row:int = 10, taille_column:int = 10, row:int = 1, column:int = 1, p: int = 0) -> MultiMaze:
        """Créé un labyrinthe avec des labyrinthes plus petit

        Args:
            taille_row (int, optional): La taille des lignes de chaque petit labyrinthe. Defaults to 10.
            taille_column (int, optional): La taille des colonnes de chaque petit labyrinthe. Defaults to 10.
            row (int, optional): Nombre de labyrinthe en ligne. Defaults to 1.
            column (int, optional): Nombre de labyrinthe en colonne. Defaults to 1.
            p (int, optional): Probabilité de supprimer des murs dans le labyrinthe. Defaults to 0.

        Returns:
            Maze: _description_
        """

        assert p >= 0 and p <= 100, "p doit être compris entre 0 et 100 (c'est une probabilité)"
        assert row > 0 and column > 0, "row et column doivent être supérieur à 0"
        assert taille_row > 0 and taille_column > 0, "taille_row et taille_column doivent être supérieur à 0"

        if self.__debug > 0:
            print(taille_row * row + 2 + row-1, taille_column * column + 2 + column-1)

        multiMaze = MultiMaze.MultiMaze(row, column, self.__wall, self.__floor)
        grid = multiMaze.get_grid()


        for i in range(row):
            for j in range(column):
                maze = Maze.Maze(taille_row, taille_column, self.__wall, self.__floor)
                self.__makeMaze(maze)
                if p > 0:
                    nb_wall = self.__countWall(maze)
                    nb_wall_delete = int(nb_wall * (p/100))
                    if self.__debug > 0:
                        print("On supprime", nb_wall_delete, "murs")
                    self.__deleteWall(maze, nb_wall_delete)
                grid[i][j] = maze
        multiMaze.set_grid(grid)


        return multiMaze

    def __deleteWall(self, maze: Maze, nb_wall_delete:int, plan:List[List[int]]=[[-1, -1,], [-1, -1]]):
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


    def __countWall(self, maze: Maze,plan:List[List[int]]=[[-1, -1,], [-1, -1]]):
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

    def __makeMaze(self, maze: Maze,plan:List[List[int]]=[[-1, -1,], [-1, -1]]):
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

