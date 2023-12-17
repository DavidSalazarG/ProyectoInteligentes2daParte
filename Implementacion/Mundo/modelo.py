from mesa import Model
from agente import AgenteRobot, AgentePared, AgenteCamino, AgenteDestino, AgenteCaja
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from busquedas_no_informadas import bfs, dfs, uniform_cost_search
from busquedas_informadas import a_star


class ModeloSokoban(Model):
    def __init__(self):
        self.agentes = {}
        self.agentesCoordenadas = {}
        self.schedule=RandomActivation(self)
        self.grid = MultiGrid(5, 7, True)
        self.inicio = (0, 0)
        self.destino = (0, 0)
        self.solucion = []
        self.AgenteRobot1 = AgenteRobot
        self.AgenteCaja1 = AgenteCaja
        self.contador = 0
        self.flag = 0


    def step(self, step) -> None:
        #print(self.solucion)
        self.schedule.step()



        #newAgent = AgenteIndicador(f"indicador_{step}", self)
        #self.schedule.add(newAgent)
        #print(self.solucion[int(step)-1])

        #Se obtienen las coordenadas de los agentes caja y robot

        posicion_caja = tuple
        posicion_robot = tuple
        for coordenada, agente in self.agentesCoordenadas.items():

            if agente == 'C-b':
                posicion_caja = coordenada
            elif agente == 'C-a':
                posicion_robot = coordenada

        #Se mueve el robot hasta la caja con A*



        #Se verifica si el robot ya es vecino de la caja
        #print("vecinos caja: ", self.grid.get_neighbors(posicion_caja, False, False, 1))
        vecinosCaja = self.grid.get_neighbors(posicion_caja, False, False, 1)
        if self.flag == 0:
            for i in vecinosCaja:
                if i.__class__ == self.AgenteRobot1.__class__:
                    print("Destino :", self.destino)
                    self.solucion = dfs(self.obtener_lista_adyacencias(), self.AgenteCaja1.pos, self.destino)
                    print("ALTO!!!")
                    self.contador = 0
                    print("contador despues de la verificacion :", self.contador)
                    self.flag = 1
        if self.flag == 0:
            self.solucion = a_star(self.obtener_lista_adyacencias(), self.inicio, posicion_caja)
            print(self.contador)
            self.grid.move_agent(self.AgenteRobot1, self.solucion[self.contador])
            self.contador += 1

        elif self.flag == 1:
            print("solucion despues de la flag: ", self.solucion)
            self.grid.move_agent(self.AgenteCaja1, self.solucion[self.contador + 1])
            self.grid.move_agent(self.AgenteRobot1, self.solucion[self.contador])
            self.contador += 1

    def cargar_agentes(self, mapa):
        #self.agentes={}
        #self.agentesCoordenadas = {}
        #self.solucion = []
        self.schedule = RandomActivation(self)
        agentes,columnas,filas = self.recorrer_mapa(mapa)
        self.agentes = agentes
        self.grid = MultiGrid(columnas, filas, True)
        self.llenar_grilla()

    def llenar_grilla(self):

        for i in self.agentes:

            if self.agentes[i] == "R":
                newAgent=AgentePared(f"roca_{i}",self)
                self.schedule.add(newAgent)
                self.grid.place_agent(newAgent, (i[1], self.grid.height - i[0] - 1))
            if self.agentes[i] == "C-a":
                self.inicio = (i[1], self.grid.height - i[0] - 1)
                newAgent=AgenteRobot(f"robot_{i}",self)
                self.schedule.add(newAgent)
                self.AgenteRobot1 = newAgent
                self.grid.place_agent(newAgent, (i[1], self.grid.height - i[0] - 1))
                self.agentesCoordenadas[i[1], self.grid.height - i[0] - 1] = "C-a"
            if self.agentes[i] == "M":
                self.destino = (i[1], self.grid.height - i[0] - 1)
                newAgent=AgenteDestino(f"meta_{i}",self)
                self.schedule.add(newAgent)
                self.grid.place_agent(newAgent, (i[1], self.grid.height - i[0] - 1))
                self.agentesCoordenadas[i[1], self.grid.height- i[0] - 1] = "M"
            if self.agentes[i] == "C":
                newAgent=AgenteCamino(f"camino_{i}",self)
                self.schedule.add(newAgent)
                self.grid.place_agent(newAgent, (i[1], self.grid.height - i[0] - 1))
                self.agentesCoordenadas[i[1], self.grid.height - i[0] - 1] = "C"
            if self.agentes[i] == "C-b":
                newAgent=AgenteCaja(f"caja_{i}",self)
                self.schedule.add(newAgent)
                self.grid.place_agent(newAgent, (i[1], self.grid.height - i[0] - 1))
                self.AgenteCaja1 = newAgent
                self.agentesCoordenadas[i[1], self.grid.height - i[0] - 1] = "C-b"

    def recorrer_mapa(self, mapa):
        lineas = mapa.replace("\r\n", ".").split(".")
        grafo = {}
        lista = [elemento.strip().split(', ') for elemento in lineas]
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                lista[i][j] = lista[i][j].replace(" ", "")
                lista[i][j] = lista[i][j].replace(",", "")
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                grafo[(i, j)] = lista[i][j]

        return grafo, len(lista[1]), len(lista)


    def obtener_lista_adyacencias(self):
        lista_adyacencias_ponderadas = {}

        for coordenada, identificador in self.agentesCoordenadas.items():
            x, y = coordenada
            adyacentes_ponderados = {}

            # Verificar nodos adyacentes hacia izquiersa
            if (x - 1, y) in self.agentesCoordenadas:
                adyacentes_ponderados[(x - 1, y)] = 100
            # Verificar nodos adyacentes hacia arriba
            if (x, y + 1) in self.agentesCoordenadas:
                adyacentes_ponderados[(x, y + 1)] = 100
            # Verificar nodos adyacentes hacia la derecha
            if (x + 1, y) in self.agentesCoordenadas:
                adyacentes_ponderados[(x + 1, y)] = 100
            # Verificar nodos adyacentes hacia abajo
            if (x, y - 1) in self.agentesCoordenadas:
                adyacentes_ponderados[(x, y - 1)] = 100



            lista_adyacencias_ponderadas[coordenada] = adyacentes_ponderados

        return lista_adyacencias_ponderadas

    def realizar_recorrido(self,recorrido,heuristica):
        if recorrido == "1":
            self.solucion = bfs(self.obtener_lista_adyacencias(), self.inicio, self.destino)
            return
        elif recorrido == "2":
            self.solucion =  dfs(self.obtener_lista_adyacencias(), self.inicio, self.destino)
            return
        elif recorrido == "3":
            self.solucion =  uniform_cost_search(self.obtener_lista_adyacencias(), self.inicio, self.destino)
            return
        elif recorrido == "6":
            self.solucion =  a_star(self.obtener_lista_adyacencias(), self.inicio, self.destino)
            return
        else:
            return
