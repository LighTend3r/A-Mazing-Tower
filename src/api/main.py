import j2l.pytactx.agent as pytactx
import os
import time
from decouple import config

ARENA = config('ARENA_PYTACTX')
PLAYER_ID = config('PLAYER_ID_PYTACTX_GUEST')
USERNAME = config('USERNAME_PYTACTX')
PASS = config('PASS_PYTACTX')
SERVEUR = config('SERVEUR_PYTACTX')

print(ARENA, PLAYER_ID, USERNAME, PASS, SERVEUR)


agent = pytactx.Agent(playerId=PLAYER_ID,
                        arena=ARENA,
                        username=PASS,
                        password=PASS,
                        server=SERVEUR,
                        verbosity=2)

time.sleep(5)

agent.update()

