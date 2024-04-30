import random 

class Agent():
    def __init__(self, id: int) -> None:
        self.id = id
        self.energy = random.randint(20, 150)
        is_percentage: bool = bool(random.getrandbits(1))
        self.transfer_type = {}
        if is_percentage:
            self.transfer_type['percentage'] = random.randint(0, 15) / 100.0
        else:
            self.transfer_type['integer'] = random.randint(0, 25)
    
    def setEnergy(self, energy_transfer: int, receive: bool):
        if receive:
            self.energy += energy_transfer
        else:
            self.energy -= energy_transfer
    
    
    
    
    