import j2l.pytactx.agent as pytactx
import os
import time

agent = pytactx.Agent(playerId=os.getenv('PLAYER_ID'),
						arena=os.getenv('ARENA'),
						username=os.getenv('USERNAME'),
						password=os.getenv('PASSWORD'),
						server=os.getenv('SERVER'),
						verbosity=2)

agent.ruleArena("desc", "coucou")
agent.ruleArena("bgImg", "gta5.jpg")

time.sleep(5)

agent.update()
	
