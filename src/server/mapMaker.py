#! /usr/bin/env python3
import j2l.pytactx.agent as pytactx
import random
import math
import time
from decouple import config
import threading


PLAYERID = config('PLAYERID_PYTACTX')
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
