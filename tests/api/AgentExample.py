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

                    portals[case].append((x, y))

                if case == Case.COIN.value:
                    self.__nb_coins += 1

        return portals

    def __add_to_queue(self, map_already_seen, maze_map, x, y, queue, actions, action):
        if map_already_seen[y][x]:
            return

        actions.append(action)

        if maze_map[y][x] == Case.COIN.value:
            actions.append("COIN")
            self.__closest_coin = (x, y)
            self.__path = actions
            return

        map_already_seen[y][x] = False
        queue.append([(x, y), actions])

    def __search_closest_coin(self):
        self.__path = []
        maze_map = self.__agent.get_map()
        map_already_seen = [[False] * len(maze_map[0]) for i in range(len(maze_map))]
        portals = self.__get_portals()

        if self.__nb_coins == 0:
            return

        queue = [[self.__agent.get_coordinates(), []]]
        range_search = 0
        last_pos_last_range = queue[0][0]
        map_already_seen[queue[0][0][1]][queue[0][0][0]] = True

        while len(queue) != 0 and self.__closest_coin is None:
            (x, y), actions = queue.pop(0)

            if y - 1 >= 0 and maze_map[y - 1][x] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x, y - 1, queue, deepcopy(actions), "UP")

            if y + 1 < len(maze_map) and maze_map[y + 1][x] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x, y + 1, queue, deepcopy(actions), "DOWN")

            if x - 1 >= 0 and maze_map[y][x - 1] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x - 1, y, queue, deepcopy(actions), "LEFT")

            if x + 1 < len(maze_map[0]) and maze_map[y][x + 1] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x + 1, y, queue, deepcopy(actions), "RIGHT")

            if maze_map[y][x] >= Case.PORTALS.value:
                if (x, y) == portals[maze_map[y][x]][0]:
                    new_x, new_y = portals[maze_map[y][x]][1]
                else:
                    new_x, new_y = portals[maze_map[y][x]][0]

                self.__add_to_queue(map_already_seen, maze_map, new_x, new_y, queue, deepcopy(actions), "TP")

            if (x, y) == last_pos_last_range:
                range_search += 1
                last_pos_last_range = queue[-1][0]
                print(range_search)

        print("find")

    def __turn(self):
        while (self.__closest_coin is None or
               self.__agent.get_map()[self.__closest_coin[1]][self.__closest_coin[0]] != Case.COIN.value):
            print(self.__closest_coin)
            self.__search_closest_coin()

        next_action = self.__path.pop(0)

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
    AgentExample("test_pierre").main()
