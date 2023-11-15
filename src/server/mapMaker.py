#! /usr/bin/env python3
import j2l.pytactx.agent as pytactx
from decouple import config
import time


import maze.Maze as Maze
import maze.MakeMaze as MakeMaze
import maze.MultiMaze as MultiMaze



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

### MISE EN PLACE DES REGLES ###

agent.ruleArena("gridColumns", multiMaze.get_all_column())
agent.ruleArena("gridRows", multiMaze.get_all_row())

agent.ruleArena("bgImg", "grass.jpg")

agent.ruleArena("map", multiMaze.get_all_maze())
agent.ruleArena("mapImgs", MAP_IMGS)
agent.ruleArena("mapFriction", MAP_FRICTION)

agent.ruleArena("profiles", ['runner'])
agent.ruleArena("pIcons", [''])
agent.ruleArena("weapons", ['none'])
agent.ruleArena("hitCollision", [0])
agent.ruleArena("collision", [False])
agent.ruleArena("range", 0) # Permet de voir tout les joueurs


agent.ruleArena("teamNb", [False])

agent.ruleArena("api", "https://blog.lightender.fr/tkt/")
agent.ruleArena("help", "https://blog.lightender.fr/tkt/")


### LANCEMENT DU SERVEUR ###

time.sleep(5)
agent.update()


# TODO: Faire un patron état sur la partie

for agentId in agent.voisins.keys():
    print(agentId)

def get_tile(agentID, agent:pytactx.Agent, multiMaze: MultiMaze.MultiMaze):
    x = agent.voisins[agentID].get_x()
    y = agent.voisins[agentID].get_y()


    return multiMaze.get_tile(x,y)


while True:
    for agentId in agent.voisins.keys():
        if get_tile(agentId, agent, multiMaze) == multiMaze.get_coin():
            agent.sendMsg(agentId, "Tu as gagné !")
            agent.stop()
            break
        elif get_tile(agentId, agent, multiMaze) in multiMaze.get_all_portal_name():
            agent.sendMsg(agentId, "Tu as perdu !")
            agent.stop()
            break
    agent.update()
    
