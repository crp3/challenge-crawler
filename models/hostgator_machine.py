from dataclasses import dataclass

from models.generic_machine import GenericMachine

@dataclass
class HostgatorMachine:
    memory: str
    cpu: str
    storage: str
    bandwidth: str
    price:str

    def to_generic_machine(self):
        return GenericMachine(
            self.cpu,
            self.memory,
            self.storage,
            self.bandwidth,
            self.price
        )
