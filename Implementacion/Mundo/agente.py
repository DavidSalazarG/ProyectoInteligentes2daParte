from mesa import Agent

class AgenteRobot(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self) -> None:
        pass
    def destination_reached(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        print("vecinos " + str(cellmates))

        if isinstance(cellmates[0], AgenteDestino):
            print("si es instancia")
            return True

    # Se mueve a una posicion dada
    def move(self, new_position) -> None:
        self.model.grid.move_agent(self, new_position)


class AgentePared(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
class AgenteCaja(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def step(self) -> None:
        pass

    def destination_reached(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        print("vecinos " + str(cellmates))

        if isinstance(cellmates[0], AgenteDestino):
            print("si es instancia")
            return True

    # Se mueve a una posicion dada
    def move(self, new_position) -> None:
        self.model.grid.move_agent(self, new_position)
class AgenteDestino(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)

class AgenteCamino(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)

class AgenteIndicador(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)