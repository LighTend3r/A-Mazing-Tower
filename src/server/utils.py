import j2l.pytactx.agent as pytactx
import maze.MultiMaze as MultiMaze

def get_coordonnee(agentID, agent:pytactx.Agent):
    x = agent.range[agentID]['x']
    y = agent.range[agentID]['y']

    return y,x

def get_tile(agentID, agent:pytactx.Agent, multiMaze: MultiMaze.MultiMaze):
    x, y = get_coordonnee(agentID, agent)
    return multiMaze.get_tile(x,y)
