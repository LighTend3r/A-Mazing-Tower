#! /usr/bin/env python3
import j2l.pytactx.agent as pytactx
import os
import time
from decouple import config
from runner.PytactxRunner import PytactxRunner
import random

ARENA = config('ARENA_PYTACTX')
PLAYER_ID = config('PLAYER_ID_PYTACTX_GUEST')
USERNAME = config('USERNAME_PYTACTX')
PASS = config('PASS_PYTACTX')
SERVEUR = config('SERVEUR_PYTACTX')

print(ARENA, PLAYER_ID, USERNAME, PASS, SERVEUR)


agent = PytactxRunner(PLAYER_ID)

time.sleep(5)

agent.update()

while 1:
    direction = random.randint(0,3)
    if direction == 0:
        agent.moveUp()
    elif direction == 1:
        agent.moveDown()
    elif direction == 2:
        agent.moveLeft()
    else:
        agent.moveRight()
    agent.update()

