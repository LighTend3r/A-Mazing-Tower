import sys
from copy import deepcopy

sys.path.append("../../src/api")

from runner.PytactxRunner import PytactxRunner
from runner.Case import Case


class AgentExample:
    def __init__(self, player_id):
        self.__agent = PytactxRunner(player_id)
        self.__path = []
        self.__closest_coin = None
        self.__nb_coins = 0

    def __get_portals(self):
        portals = {}

        for y, ligne in enumerate(self.__agent.get_map()):
            for x, case in enumerate(ligne):
                if case >= Case.PORTALS.value:
                    if case not in portals:
                        portals[case] = []

                if case == Case.COIN.value:
                    self.__nb_coins += 1

        return portals

    def __add_to_queue(self, maze_map, x, y, queue, actions, action):
        if maze_map[y][x] == -1:
            return

        actions.append(action)

        if maze_map[y][x] == Case.COIN.value:
            actions.append("COIN")
            self.__closest_coin = (x, y)
            self.__path = actions
            return

        maze_map[y][x] = -1
        queue.append([(x, y), actions])

    def __search_closest_coin(self):
        self.__path = []
        maze_map = self.__agent.get_map()
        map_copy = [[0] * len(maze_map[0])] * len(maze_map)
        portals = self.__get_portals()

        if self.__nb_coins == 0:
            return

        queue = [[self.__agent.get_coordinates(), []]]
        map_copy[queue[0][0][1]][queue[0][0][0]] = -1

        while len(queue) != 0 and self.__closest_coin is None:
            (x, y), actions = queue.pop(0)

            if y - 1 >= 0 and maze_map[y - 1][x] != Case.WALL.value:
                self.__add_to_queue(map_copy, x, y - 1, queue, deepcopy(actions), "UP")

            if y + 1 < len(map_copy) and maze_map[y + 1][x] != Case.WALL.value:
                self.__add_to_queue(map_copy, x, y + 1, queue, deepcopy(actions), "DOWN")

            if x - 1 >= 0 and maze_map[y][x - 1] != Case.WALL.value:
                self.__add_to_queue(map_copy, x - 1, y, queue, deepcopy(actions), "LEFT")

            if x + 1 < len(maze_map[0]) and maze_map[y][x + 1] != Case.WALL.value:
                self.__add_to_queue(map_copy, x + 1, y, queue, deepcopy(actions), "RIGHT")

            if maze_map[y][x] >= Case.PORTALS.value:
                if (x, y) == portals[maze_map[y][x]][0]:
                    new_x, new_y = portals[maze_map[y][x]][1]
                else:
                    new_x, new_y = portals[maze_map[y][x]][0]

                self.__add_to_queue(map_copy, new_x, new_y, queue, deepcopy(actions), "TP")

    def __turn(self):
        while (self.__closest_coin is None or
               self.__agent.get_map()[self.__closest_coin[1]][self.__closest_coin[0]] != Case.COIN.value):
            self.__search_closest_coin()

        print(self.__closest_coin)
        next_action = self.__path.pop(0)
        print(next_action)

        match next_action:
            case "UP":
                self.__agent.move_up()
            case "DOWN":
                self.__agent.move_down()
            case "LEFT":
                self.__agent.move_left()
            case "RIGHT":
                self.__agent.move_right()
            case "TP":
                self.__agent.take_portal()
            case "COIN":
                self.__agent.take_coin()
                self.__closest_coin = None

    def main(self):
        while True:
            (x, y) = self.__agent.get_coordinates()
            self.__turn()

            self.__agent.update()

            while (x, y) == self.__agent.get_coordinates() and self.__closest_coin is not None:
                self.__agent.update()


if __name__ == "__main__":
    AgentExample("parcoursLargeur").main()
