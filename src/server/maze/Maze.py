class Maze:
    def __init__(self, row:int, column:int, wall, floor):
        self.__column = column
        self.__row = row
        self.__grid = [[wall for _ in range(column)] for _ in range(row)]
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
