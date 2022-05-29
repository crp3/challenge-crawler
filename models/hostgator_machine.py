from dataclasses import dataclass

from models.generic_machine import GenericMachine

@dataclass
class HostgatorMachine:
    memory: str
    cpu: str
    storage: str
    bandwidth: str
    price:str
