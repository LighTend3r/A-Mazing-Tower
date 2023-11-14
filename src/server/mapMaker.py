#! /usr/bin/env python3
import j2l.pytactx.agent as pytactx
from decouple import config
import time


import maze.Maze as Maze
import maze.MakeMaze as MakeMaze
import maze.MultiMaze as MultiMaze




PLAYERID = config('PLAYER_ID_PYTACTX')
ARENA = config('ARENA_PYTACTX')
USERNAME = config('USERNAME_PYTACTX')
PASS = config('PASS_PYTACTX')
SERVEUR = config('SERVEUR_PYTACTX')

print(ARENA, USERNAME, PASS, SERVEUR)


agent = pytactx.Agent(playerId=PLAYERID,
                        arena=ARENA,
                        username=PASS,
                        password=PASS,
                        server=SERVEUR,
                        verbosity=2)





map = agent.map

makeMaze = MakeMaze.MakeMaze()
makeMaze.setFloor(2)
maze:MultiMaze.MultiMaze = makeMaze.makeMultiMaze(22,22,2,2,p=10)

agent.ruleArena("gridColumns", maze.get_all_column())
agent.ruleArena("gridRows", maze.get_all_row())


agent.ruleArena("map", maze.get_all_maze())
agent.ruleArena("mapImgs", ["","ironblock.jpg", "grass.jpg"])
agent.ruleArena("mapFriction", [0,1,0])

time.sleep(5)
agent.update()
