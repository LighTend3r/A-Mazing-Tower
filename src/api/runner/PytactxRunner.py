# Player interface
from typing import Any
import time
import j2l.pytactx.agent as pytactx

from decouple import config
from runner.IRunner import IRunner

ARENA = config('ARENA_PYTACTX')
USERNAME = config('USERNAME_PYTACTX')
PASS = config('PASS_PYTACTX')
SERVEUR = config('SERVEUR_PYTACTX')


WALL = 1
COIN = 2

HEIGHT_MAZE=22
WIDTH_MAZE=22

dir = {
    "TAKE_COIN": 0,
    "DEFAULT": 1,
    "TAKE_PORTAL": 2
}

class PytactxRunner(IRunner):
    def __init__(self, playerId:str) -> None:
        self.__agent = pytactx.Agent(playerId, ARENA, USERNAME, PASS, SERVEUR, verbosity=2)

    def getCoordinates(self) -> tuple[int, int]:
        return (self.__agent.x, self.__agent.y)

    def getMap(self) -> tuple[tuple[int]]:
        return self.__agent.map
    
    def getCurrentTile(self) -> int:
        x,y = self.getCoordinates()
        return self.__agent.map[y][x]

    def update(self) -> None:
        self.__agent.update()

    def moveUp(self) -> bool:
        x,y = self.getCoordinates()

        if(y<=0 or self.getMap()[y-1][x] == WALL):
            return False

        self.__agent.moveTowards(self.__agent.x, self.__agent.y - 1)
        return True

    def moveDown(self) -> bool:
        x,y = self.getCoordinates()

        if(y>=(HEIGHT_MAZE - 1) or self.getMap()[y+1][x] == WALL):
            return False

        self.__agent.moveTowards(self.__agent.x, self.__agent.y + 1)
        return True

    def moveLeft(self) -> bool:
        x,y = self.getCoordinates()

        if(x <= 0 or self.getMap()[y][x-1] == WALL):
            return False

        self.__agent.moveTowards(self.__agent.x - 1, self.__agent.y)
        return True

    def moveRight(self) -> bool:
        x,y = self.getCoordinates()

        if(x>=(WIDTH_MAZE - 1) or self.getMap()[y][x+1] == WALL):
            return False

        self.__agent.moveTowards(self.__agent.x + 1, self.__agent.y)
        return True

    def takeCoin(self) -> bool:
        if(self.__agent.map[self.__agent.y][self.__agent.x] != COIN):
            self.__agent.lookAt(dir['DEFAULT'])
            return False
        
        self.__agent.lookAt(dir['TAKE_COIN'])
        return True

    def takePortal(self) -> bool:
        if(self.__agent.map[self.__agent.y][self.__agent.x] <= COIN):
            self.__agent.lookAt(dir['DEFAULT'])
            return False
        
        self.__agent.lookAt(dir['TAKE_PORTAL'])
        return True
