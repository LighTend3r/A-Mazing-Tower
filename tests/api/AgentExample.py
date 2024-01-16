import sys

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
        """
        Renvoie les portails de la carte et compte le nombre de pièces.
        """
        portals = {}
        self.__nb_coins = 0

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
        """
        Ajoute au chemin l'action et marque la case comme déjà visité.
        Si on est sur une pièce, on la stocke.
        """
        if map_already_seen[y][x]:
            return

        if maze_map[y][x] == Case.COIN.value:
            self.__closest_coin = (x, y)
            self.__path = actions + [action, "COIN"]
            return

        map_already_seen[y][x] = True
        queue.append([(x, y), actions + [action]])

    def __search_closest_coin(self):
        """
        Cherche la pièce la plus proche et la stocke dans self.__closest_coin,
        le chemin pour y accéder et stocker dans self.__path.
        """
        maze_map = self.__agent.get_map()
        (x, y) = self.__agent.get_coordinates()

        if maze_map[y][x] == Case.COIN.value:
            self.__closest_coin = (x, y)
            self.__path = ["COIN"]
            return

        if self.__closest_coin is not None and maze_map[self.__closest_coin[1]][self.__closest_coin[0]] == Case.COIN.value:
            return

        portals = self.__get_portals()

        while self.__nb_coins == 0:
            portals = self.__get_portals()
            self.__agent.update()

        maze_map = self.__agent.get_map()
        (x, y) = self.__agent.get_coordinates()
        self.__closest_coin = None
        self.__path = []
        map_already_seen = [[False] * len(maze_map[0]) for _ in range(len(maze_map))]

        queue = [[(x, y), []]]
        map_already_seen[y][x] = True

        while len(queue) != 0 and self.__closest_coin is None:
            (x, y), actions = queue.pop(0)

            if y - 1 >= 0 and maze_map[y - 1][x] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x, y - 1, queue, actions, "UP")

            if y + 1 < len(maze_map) and maze_map[y + 1][x] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x, y + 1, queue, actions, "DOWN")

            if x - 1 >= 0 and maze_map[y][x - 1] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x - 1, y, queue, actions, "LEFT")

            if x + 1 < len(maze_map[0]) and maze_map[y][x + 1] != Case.WALL.value:
                self.__add_to_queue(map_already_seen, maze_map, x + 1, y, queue, actions, "RIGHT")

            if maze_map[y][x] >= Case.PORTALS.value:
                if (x, y) == portals[maze_map[y][x]][0]:
                    new_x, new_y = portals[maze_map[y][x]][1]
                else:
                    new_x, new_y = portals[maze_map[y][x]][0]

                self.__add_to_queue(map_already_seen, maze_map, new_x, new_y, queue, actions, "TP")


    def __turn(self):
        """
        Fais l'action pour atteindre la pièce la plus proche.
        """
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
        """
        Boucle infinie qui exécute chaque tour et fais un update sur le serveur.
        """
        while True:
            (x, y) = self.__agent.get_coordinates()
            self.__turn()

            self.__agent.update()

            while (x, y) == self.__agent.get_coordinates() and self.__closest_coin is not None:
                self.__agent.update()

            self.__agent.reset_dir()


if __name__ == "__main__":
    AgentExample("test").main()
