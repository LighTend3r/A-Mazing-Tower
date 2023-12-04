class IRunner:
    def getCoordinates(self) -> tuple[int, int]:
        """
        Return the coordinates in the map, x and y.
        """
        ...

    def getMap(self) -> tuple[tuple[int]]:
        """
        Return the map.
        """
        ...

    def getCurrentTile(self) -> int:
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

    def moveUp(self) -> bool:
        """
        Try to move upward if possible.
        If not return False.
        """
        ...
    
    def moveDown(self) -> bool:
        """
        Try to move downward if possible.
        If not return False.
        """
        ...
    
    def moveLeft(self) -> bool:
        """
        Try to move to the left if possible.
        If not return False.
        """
        ...
    
    def moveRight(self) -> bool:
        """
        Try to move to the right if possible.
        If not return False.
        """
        ...

    def takeCoin(self) -> bool:
        """
        Try to take a coin at the current position.
        If there is a coin return True, return False.
        """
        ...

    def takePortal(self) -> bool:
        """
        Try to take a portal at the current position.
        If there is a portal return True, return False.
        """
        ...
    