import json
from typing import List

from models.generic_machine import GenericMachine

def print_machines(generic_machines: List[GenericMachine]):
    for machine in generic_machines:
        print(machine)

def save_json(generic_machines: List[GenericMachine]):
    with open('machines.json', 'w', encoding='utf-8') as output_file:
        json.dump(
            [machine.__dict__ for machine in generic_machines],
            output_file
        )
