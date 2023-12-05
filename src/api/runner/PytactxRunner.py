# Player interface
import j2l.pytactx.agent as pytactx

from decouple import config
from runner.IRunner import IRunner
from runner.Case import Case
from runner.Direction import Direction

ARENA = config('ARENA_PYTACTX')
USERNAME = config('USERNAME_PYTACTX')
PASS = config('PASS_PYTACTX')
SERVEUR = config('SERVEUR_PYTACTX')


class PytactxRunner(IRunner):
    def __init__(self, player_id: str) -> None:
        self.__agent = pytactx.Agent(player_id, ARENA, USERNAME, PASS, SERVEUR, verbosity=2)

    def get_coordinates(self) -> tuple[int, int]:
        return self.__agent.x, self.__agent.y

    def get_map(self) -> tuple[tuple[int]]:
        return self.__agent.map

    def get_current_tile(self) -> int:
        x, y = self.get_coordinates()
        return self.__agent.map[y][x]

    def update(self) -> None:
        self.__agent.update()

    def move_up(self) -> bool:
        x, y = self.get_coordinates()

        if y <= 0 or self.get_map()[y - 1][x] == Case.WALL.value:
            return False

        self.__agent.moveTowards(self.__agent.x, self.__agent.y - 1)
        return True

    def move_down(self) -> bool:
        x, y = self.get_coordinates()

        if y >= self.__agent.gridRows - 1 or self.get_map()[y + 1][x] == Case.WALL.value:
            return False

        self.__agent.moveTowards(self.__agent.x, self.__agent.y + 1)
        return True

    def move_left(self) -> bool:
        x, y = self.get_coordinates()

        if x <= 0 or self.get_map()[y][x - 1] == Case.WALL.value:
            return False

        self.__agent.moveTowards(self.__agent.x - 1, self.__agent.y)
        return True

    def move_right(self) -> bool:
        x, y = self.get_coordinates()

        if x >= (self.__agent.gridColumns - 1) or self.get_map()[y][x + 1] == Case.WALL.value:
            return False

        self.__agent.moveTowards(self.__agent.x + 1, self.__agent.y)
        return True

    def take_coin(self) -> bool:
        if self.__agent.map[self.__agent.y][self.__agent.x] == Case.COIN.value:
            self.__agent.lookAt(Direction.TAKE_COIN.value)
            return True

        self.__agent.lookAt(Direction.DEFAULT.value)
        return False

    def take_portal(self) -> bool:
        if self.__agent.map[self.__agent.y][self.__agent.x] >= Case.PORTALS.value:
            self.__agent.lookAt(Direction.TAKE_PORTAL.value)
            return True

        self.__agent.lookAt(Direction.DEFAULT.value)
        return False
