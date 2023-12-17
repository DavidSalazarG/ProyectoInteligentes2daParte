from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from modelo import ModeloSokoban
from agente import AgenteRobot, AgentePared, AgenteCamino, AgenteDestino, AgenteIndicador, AgenteCaja


def agent_portrayal(agent):
    portrayal={"Shape":"circle","Filled":"true","r":0.5}
    if isinstance(agent, AgenteIndicador):
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.8
        return portrayal

    if isinstance(agent, AgenteRobot):
        return {"Shape":"Mundo/Imagenes/robot.png","Layer":0, "w": 1, "h" : 1}

    if isinstance(agent, AgentePared):
        return {"Shape":"Mundo/Imagenes/muro.png","Layer":0, "w": 1, "h" : 1}

    if isinstance(agent, AgenteCamino):
        return {"Shape": "Mundo/Imagenes/pavimentacion.png", "Layer": 0, "w": 1, "h": 1}

    if isinstance(agent, AgenteDestino):
        return {"Shape": "Mundo/Imagenes/bandera.png", "Layer": 0, "w": 1, "h": 1}

    if isinstance(agent, AgenteCaja):
        return {"Shape": "Mundo/Imagenes/paquete.png", "Layer": 0, "w": 1, "h": 1}

    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.2
        portrayal["text"] = {"text": "999", "color": "white", "scale": 1.5}


    return portrayal

def crear_canvas(columnas, filas):
    grid = CanvasGrid(agent_portrayal, columnas, filas, 500, 700)
    server.visualization_elements(grid)

num_row_width=7
num_row_height=5

grid=CanvasGrid(agent_portrayal,num_row_width,num_row_height,700,500)
server=ModularServer(ModeloSokoban,[grid],"Sokoban",{})

server.port=8521
server.launch()