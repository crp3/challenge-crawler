from dataclasses import dataclass

@dataclass
class VultrMachine:
    price: str
    storage: str
    cpu: str
    memory: str
    bandwidth: str
    network: str
