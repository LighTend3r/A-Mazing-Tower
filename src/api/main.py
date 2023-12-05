import time
from decouple import config
from runner.PytactxRunner import PytactxRunner
import random

PLAYER_ID = config('PLAYER_ID_PYTACTX_GUEST')

agent = PytactxRunner(PLAYER_ID)

time.sleep(5)

agent.update()

while 1:
    current_tile = agent.get_current_tile()
    direction = random.randint(0, 3)

    if current_tile == 2:
        agent.take_coin()
    elif current_tile > 2:
        agent.take_portal()

    agent.update()

    if direction == 0:
        agent.move_up()
    elif direction == 1:
        agent.move_down()
    elif direction == 2:
        agent.move_left()
    else:
        agent.move_right()

    agent.update()
