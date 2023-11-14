class IRunner:
    def getGlobalCoordinates(self) -> tuple[int, int]:
        """
        Return the coordinates in the entire map x and y.
        """
        ...

    def getCurrentMazeCoordinates(self) -> tuple[int, int]:
        """
        Return the coordinates in the entire map x and y.
        """
        ...

    def getCurrentMaze(self) -> int:
        """
        Return the current maze number.
        """
        ...

    def getCurrentMazeMap(self) -> tuple[tuple[int]]:
        """
        Return the map of the current maze.
        """
        ...

    def getGlobalMap(self) -> tuple[tuple[int]]:
        """
        Return the entire map.
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
        If the operation failed, return False.
        """
        ...

    def takePortal(self) -> bool:
        """
        Try to take a portal at the current position.
        If the operation failed, return False.
        """
        ...
    