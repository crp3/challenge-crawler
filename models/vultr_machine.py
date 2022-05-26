from dataclasses import dataclass
from typing import List

from models.generic_machine import GenericMachine

@dataclass
class VultrMachine:
    price: str
    storage: str
    cpu: str
    memory: str
    bandwidth: str
    network: str

    def to_generic_machine(self) -> GenericMachine:
        return GenericMachine(
            self.cpu,
            self.memory,
            self.storage,
            self.bandwidth,
            self.price
        )
