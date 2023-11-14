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

MAP_IMGS = ["","ironblock.jpg", "tresor.png", "d0.png", "d1.png", "d2.png"]
MAP_FRICTION = [0,1,0,0,0,0]

ROW = 2
COLONE = 2
TAILLE_ROW = 10
TAILLE_COLONE = 10
PROBA = 10

assert(len(MAP_IMGS) == len(MAP_FRICTION)), "MAP_IMGS and MAP_FRICTION must have the same length"

print(ARENA, USERNAME, PASS, SERVEUR)


agent = pytactx.Agent(playerId=PLAYERID,
                        arena=ARENA,
                        username=PASS,
                        password=PASS,
                        server=SERVEUR,
                        verbosity=2)

# map = agent.map

makeMaze = MakeMaze.MakeMaze()

makeMaze.setWall(1)
makeMaze.setFloor(0)
makeMaze.setCoin(2)

maze:MultiMaze.MultiMaze = makeMaze.makeMultiMaze(ROW,COLONE,TAILLE_ROW,TAILLE_COLONE,p=PROBA)
makeMaze.set_random_coin(maze, 5)

agent.ruleArena("gridColumns", maze.get_all_column())
agent.ruleArena("gridRows", maze.get_all_row())

agent.ruleArena("bgImg", "grass.jpg")

agent.ruleArena("map", maze.get_all_maze())
agent.ruleArena("mapImgs", MAP_IMGS)
agent.ruleArena("mapFriction", MAP_FRICTION)

time.sleep(5)
agent.update()
