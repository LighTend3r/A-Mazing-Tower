class IRunner:
    def get_coordinates(self) -> tuple[int, int]:
        """
        Return the coordinates in the map, x and y.
        """
        ...

    def get_map(self) -> tuple[tuple[int]]:
        """
        Return the map.
        """
        ...

    def get_current_tile(self) -> int:
        """
        Return the current tile value
        \n0 -> Path
        \n1 -> Wall
        \n2 -> Coin
        \nAbove -> Portals
        """
        ...

    def update(self) -> None:
        """
        Fetch the last values of player data from server
        And send buffered requests in one shot to limit bandwidth.
        To be call in the main loop at least every 10 msecs.
        """
        ...

    def move_up(self) -> bool:
        """
        Try to move upward if possible.
        If not return False.
        """
        ...

    def move_down(self) -> bool:
        """
        Try to move downward if possible.
        If not return False.
        """
        ...

    def move_left(self) -> bool:
        """
        Try to move to the left if possible.
        If not return False.
        """
        ...

    def move_right(self) -> bool:
        """
        Try to move to the right if possible.
        If not return False.
        """
        ...

    def take_coin(self) -> bool:
        """
        Try to take a coin at the current position.
        If there is a coin return True, return False.
        """
        ...

    def take_portal(self) -> bool:
        """
        Try to take a portal at the current position.
        If there is a portal return True, return False.
        """
        ...

    def reset_dir(self):
        """
        Reset the direction of the agent.
        """
        ...