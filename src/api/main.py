#! /usr/bin/env python3
import j2l.pytactx.agent as pytactx
import os
import time
from decouple import config
from runner.PytactxRunner import PytactxRunner
import random

PLAYER_ID = config('PLAYER_ID_PYTACTX_GUEST')

agent = PytactxRunner(PLAYER_ID)

time.sleep(5)

agent.update()

while 1:
    current_tile = agent.getCurrentTile()
    direction = random.randint(0,3)
    
    if(current_tile == 2):
        agent.takeCoin()
    elif(current_tile > 2):
        agent.takePortal()

    
    agent.update()

    
    if direction == 0:
        agent.moveUp()
    elif direction == 1:
        agent.moveDown()
    elif direction == 2:
        agent.moveLeft()
    else:
        agent.moveRight()
    
    agent.update()
