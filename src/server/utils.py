import j2l.pytactx.agent as pytactx
import maze.MultiMaze as MultiMaze

def get_coordonnee(agentID, agent:pytactx.Agent):
    x = agent.voisins[agentID].get_x()
    y = agent.voisins[agentID].get_y()

    return x,y

def get_tile(agentID, agent:pytactx.Agent, multiMaze: MultiMaze.MultiMaze):
    x, y = get_coordonnee(agentID, agent)
    return multiMaze.get_tile(x,y)
