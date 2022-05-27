import json
import csv
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

def save_csv(generic_machines: List[GenericMachine]):
    fields = generic_machines[-1].__dict__.keys()
    value_list = [machine.__dict__.values() for machine in generic_machines]

    with open('machines.csv', 'w', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)

        writer.writerow(fields)
        writer.writerows(value_list)
