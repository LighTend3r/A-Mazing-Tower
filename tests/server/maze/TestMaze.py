import unittest
import sys

sys.path.append("../../src/server")
import maze.Maze as Maze

class TestMaze(unittest.TestCase):

    def test_get_column(self):
        maze = Maze(15, 10, 1, 0, 2)
        self.assertEqual(maze.get_column(), 10)

        self.assertNotEqual(maze.get_column(), 15)

    def test_get_row(self):
        maze = Maze(15, 10, 1, 0, 2)
        self.assertEqual(maze.get_row(), 15)

        self.assertNotEqual(maze.get_row(), 10)

    def test_get_tile(self):
        maze = Maze(4, 4, 1, 0, 2)
        for i in range(0, 4):
            for j in range(0, 4):
                maze.set_tile(i, j, 0)

        maze.set_tile(0, 0, 1)

        maze.set_tile(3, 0, 2)

        self.assertEqual(maze.get_tile(3, 1), 0)
        self.assertEqual(maze.get_tile(0, 0), 1)
        self.assertEqual(maze.get_tile(3, 0), 2)

        self.assertNotEqual(maze.get_tile(0, 0), 0)
        self.assertNotEqual(maze.get_tile(3, 3), 1)
        self.assertNotEqual(maze.get_tile(2, 0), 2)

    def test_set_tile(self):
        maze = Maze(4, 4, 1, 0, 2)

        for i in range(0, 4):
            for j in range(0, 4):
                maze.set_tile(i, j, 0)

        maze.set_tile(0, 0, 1)

        maze.set_tile(3, 0, 2)

        self.assertEqual(maze.get_tile(3, 1), 0)
        self.assertEqual(maze.get_tile(0, 0), 1)
        self.assertEqual(maze.get_tile(3, 0), 2)

        self.assertNotEqual(maze.get_tile(0, 0), 0)
        self.assertNotEqual(maze.get_tile(3, 3), 1)
        self.assertNotEqual(maze.get_tile(2, 0), 2)

    def test_get_grid(self):
        maze = Maze(4, 4, 1, 0, 2)

        for i in range(0, 4):
            for j in range(0, 4):
                maze.set_tile(i, j, 0)

        maze.set_tile(0, 0, 1)
        maze.set_tile(1, 1, 1)
        maze.set_tile(2, 1, 1)
        maze.set_tile(1, 3, 1)
        maze.set_tile(2, 3, 1)

        maze.set_tile(0, 2, 2)
        maze.set_tile(2, 2, 2)
        maze.set_tile(3, 0, 2)

        grid = [[1,0,2,0],
                [0,1,0,1],
                [0,1,2,1],
                [2,0,0,0]]

        self.assertEqual(maze.get_grid(), grid)

    def test_get_wall(self):
        maze = Maze(15, 10, 1, 0, 2)
        self.assertEqual(maze.get_wall(), 1)

        maze2 = Maze(15, 10, 99, 0, 2)
        self.assertEqual(maze2.get_wall(), 99)

    def test_get_floor(self):
        maze = Maze(15, 10, 1, 0, 2)
        self.assertEqual(maze.get_floor(), 0)

        maze2 = Maze(15, 10, 1, 99, 2)
        self.assertEqual(maze2.get_floor(), 99)

    def test_get_coin(self):
        maze = Maze(15, 10, 1, 0, 2)
        self.assertEqual(maze.get_coin(), 2)

        maze2 = Maze(15, 10, 1, 0, 99)
        self.assertEqual(maze2.get_coin(), 99)


if __name__ == '__main__':
    unittest.main()
