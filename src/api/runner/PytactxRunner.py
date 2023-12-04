# Player interface
from typing import Any
import time
import j2l.pytactx.agent as pytactx

from decouple import config
import IRunner

ARENA = config('ARENA_PYTACTX')
USERNAME = config('USERNAME_PYTACTX')
PASS = config('PASS_PYTACTX')
SERVEUR = config('SERVEUR_PYTACTX')
PORT = config('PORT_PYTACTX')

NB_VERTICAL = config('NB_VERTICAL_MAZE')
NB_HORIZONTAL = config('NB_HORIZONTAL_MAZE')
HEIGHT_MAZE = config('HEIGHT_MAZE')
WIDTH_MAZE = config('WIDTH_MAZE')

WALL = 1

class PytactxRunner(IRunner):
    def __init__(self, playerId:str) -> None:
        self.__agent = pytactx.Agent(playerId, ARENA, USERNAME, PASS, SERVEUR, PORT)

    def getGlobalCoordinates(self) -> tuple[int, int]:
        return (self.__agent.x, self.__agent.y)

    def getCurrentMazeCoordinates(self) -> tuple[int, int]:
        pass

    def getCurrentMaze(self) -> int:
        x_maze = self.__agent.x // (WIDTH_MAZE + 1)
        y_maze = self.__agent.y // (HEIGHT_MAZE + 1)

        return y_maze * NB_HORIZONTAL + x_maze


    def getCurrentMazeMap(self) -> tuple[tuple[int]]:
        """
        Return the map of the current maze.
        """
        ...

    def getGlobalMap(self) -> tuple[tuple[int]]:
        return self.__agent.map

    def update(self) -> None:
        self.__agent.update()

    def moveUp(self) -> bool:
        x,y = self.getCurrentMazeCoordinates

        if(y<=0 or self.getCurrentMazeMap[y-1][x] == WALL):
            return False
        
        self.__agent.moveTowards(self.__agent.x, self.__agent.y - 1)
        return True
    
    def moveDown(self) -> bool:
        x,y = self.getCurrentMazeCoordinates

        if(y>=(HEIGHT_MAZE - 1) or self.getCurrentMazeMap[y+1][x] == WALL):
            return False
        
        self.__agent.moveTowards(self.__agent.x, self.__agent.y + 1)
        return True
    
    def moveLeft(self) -> bool:
        x,y = self.getCurrentMazeCoordinates

        if(x <= 0 or self.getCurrentMazeMap[y][x-1] == WALL):
            return False
        
        self.__agent.moveTowards(self.__agent.x - 1, self.__agent.y)
        return True
    
    def moveRight(self) -> bool:
        x,y = self.getCurrentMazeCoordinates

        if(x>=(WIDTH_MAZE - 1) or self.getCurrentMazeMap[y][x+1] == WALL):
            return False
        
        self.__agent.moveTowards(self.__agent.x + 1, self.__agent.y)
        return True

    def takeCoin(self) -> bool:
        """
        Try to take a coin at the current position.
        If the operation failed, return False.
        """
        ...

    def takePortal(self) -> bool:
        """
        Try to take a portal at the current position.
        If the operation failed, return False.
        """
        ...