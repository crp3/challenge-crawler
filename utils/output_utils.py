import csv
import json
from typing import List

from models.generic_machine import GenericMachine

class OutputFormatter:
    def __init__(self, generic_machines: List[GenericMachine]):
        self.generic_machines = generic_machines

    def print_machines(self):
        for machine in self.generic_machines:
            print(machine)

    def save_json(self):
        with open('machines.json', 'w', encoding='utf-8') as output_file:
            json.dump(
                [machine.__dict__ for machine in self.generic_machines],
                output_file
            )

    def save_csv(self):
        fields = self.generic_machines[-1].__dict__.keys()
        value_list = [machine.__dict__.values() for machine in self.generic_machines]

        with open('machines.csv', 'w', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)

            writer.writerow(fields)
            writer.writerows(value_list)
