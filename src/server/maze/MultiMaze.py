import maze.Maze as Maze
from typing import List

class MultiMaze:
    def __init__(self, row:int, column:int, wall, floor):
        self.__column = column
        self.__row = row
        self.__grid: List[List[Maze.Maze]] = [[None for _ in range(column)] for _ in range(row)]
        self.__wall = wall
        self.__floor = floor

    def get_column(self):
        return self.__column

    def get_row(self):
        return self.__row

    def get_grid(self):
        return self.__grid

    def get_wall(self):
        return self.__wall

    def get_floor(self):
        return self.__floor

    def set_grid(self, grid):
        self.__grid = grid

    def get_maze(self, x:int, y:int):
        return self.__grid[x][y]

    def get_all_row(self):
        return self.get_maze(0,0).get_row() * self.get_row() + 2 + self.get_row()-1

    def get_all_column(self):
        return self.get_maze(0,0).get_column() * self.get_column() + 2 + self.get_column()-1

    def get_all_maze(self):
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
        pass
