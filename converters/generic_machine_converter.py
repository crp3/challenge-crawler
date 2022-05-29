from typing import Union

from models.vultr_machine import VultrMachine
from models.generic_machine import GenericMachine
from models.hostgator_machine import HostgatorMachine

class GenericMachineConverter:
    def convert(machine: Union[VultrMachine, HostgatorMachine]) -> GenericMachine:
        return GenericMachine(
            machine.cpu,
            machine.memory,
            machine.storage,
            machine.bandwidth,
            machine.price
        )
