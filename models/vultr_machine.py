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
