#! /usr/bin/env python3
import j2l.pytactx.agent as pytactx
from decouple import config
import time


from maze import *

from utils import *



### CONFIGURATION ###

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


agent:pytactx.Agent = pytactx.Agent(playerId=PLAYERID,
                        arena=ARENA,
                        username=PASS,
                        password=PASS,
                        server=SERVEUR,
                        verbosity=2)


### CREATION DE LA MAP ###

makeMaze = MakeMaze.MakeMaze()

makeMaze.setWall(1)
makeMaze.setFloor(0)
makeMaze.setCoin(2)

multiMaze:MultiMaze.MultiMaze = makeMaze.makeMultiMaze(ROW,COLONE,TAILLE_ROW,TAILLE_COLONE,p=PROBA)
makeMaze.set_random_coin(multiMaze, 5)
makeMaze.set_spawn(multiMaze)
### MISE EN PLACE DES REGLES ###

agent.ruleArena("gridColumns", multiMaze.get_all_column())
agent.ruleArena("gridRows", multiMaze.get_all_row())

agent.ruleArena("bgImg", "grass.jpg")
agent.ruleArena("map", multiMaze.get_all_maze())
agent.ruleArena("mapImgs", MAP_IMGS)
agent.ruleArena("mapFriction", MAP_FRICTION)

agent.ruleArena("profiles", ['runner', 'arbitre', 'test'])
agent.ruleArena("pIcons", ['', '', ''])
agent.ruleArena("weapons", ['none','none','none'])
agent.ruleArena("hitCollision", [0,0,0])
agent.ruleArena("collision", [False, False, False])
agent.ruleArena("range", [0,0,0]) # Permet de voir tout les joueurs

agent.ruleArena("spawnArea", {"x": [multiMaze.get_spawn()[0] for i in range(3)], "y": [multiMaze.get_spawn()[1] for i in range(3)], "r": [0,0,0]})


agent.ruleArena("teamNb", [False, False, False])

agent.ruleArena("api", "https://blog.lightender.fr/tkt/")
agent.ruleArena("help", "https://blog.lightender.fr/tkt/")



### LANCEMENT DU SERVEUR ###

time.sleep(5)
agent.update()


# TODO: Faire un patron état sur la partie (peut être)
spawn = multiMaze.get_spawn()
for agentId in agent.range.keys():
    agent.rulePlayer(agentId, "x", spawn[0])
    agent.rulePlayer(agentId, "y", spawn[1])
time.sleep(2)
agent.update()
print(multiMaze.get_all_portal_name())

while True:
    for agentId in agent.range.keys():
        if get_tile(agentId, agent, multiMaze) == multiMaze.get_coin(): # Si le joueur est sur une pièce
            print(agentId, ": Coin")
            x, y = get_coordonnee(agentId, agent)
            multiMaze.set_tile(x,y, multiMaze.get_floor())



        elif get_tile(agentId, agent, multiMaze) in multiMaze.get_all_portal_name(): # Si le joueur est sur un portail
            print(agentId, ": Portal")
            x, y = get_coordonnee(agentId, agent)
            next_x, next_y = multiMaze.get_other_portal(x,y)
            print(next_x, next_y)
            agent.rulePlayer(agentId, "x", next_y)
            agent.rulePlayer(agentId, "y", next_x)
    agent.ruleArena("map", multiMaze.get_all_maze())
    agent.update()

