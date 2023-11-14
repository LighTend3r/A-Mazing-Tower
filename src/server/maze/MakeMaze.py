import maze.Maze as Maze
from typing import List
import random
import sys

sys.setrecursionlimit(1000000)

class MakeMaze:
    def __init__(self, wall = 1, floor = 0):
        self.__wall = wall
        self.__floor = floor

    def setFloor(self, floor):
        self.__floor = floor

    def setWall(self, wall):
        self.__wall = wall

    def makeMultiMaze(self, taille_row:int = 10, taille_column:int = 10, row:int = 1, column:int = 1) -> Maze:
        print(taille_row * row + 2 + row-1, taille_column * column + 2 + column-1)
        maze = Maze.Maze(taille_row * row + 2 + row-1, taille_column * column + 2 + column-1, self.__wall, self.__floor)
        for i in range(1,maze.get_row(), taille_row+1):
            for j in range(1,maze.get_column(), taille_column+1):
                self.__makeMaze(maze, [[i, j], [i+taille_row, j+taille_row]])

        return maze


    def __makeMaze(self, maze: Maze,plan:List[List[int]]=[[-1, -1,], [-1, -1]]):
        """Créé un labyrinthe sans boucle

        Args:
            maze (Maze): Labyrinthe à modifier
            void (str, optional): String à mettre en tant que block vide. Defaults to ' '.
        """

        start_x = 0 if plan[0][0] == -1 else plan[0][0]
        start_y = 0 if plan[0][1] == -1 else plan[0][1]
        end_x = maze.get_row()-1 if plan[1][0] == -1 else plan[1][0]
        end_y = maze.get_column()-1 if plan[1][1] == -1 else plan[1][1]


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

