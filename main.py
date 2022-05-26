import sys
import json

from extractors.vultr_extractor import VultrExtractor

if __name__ == '__main__':
    vultrExtractor = VultrExtractor('https://www.vultr.com/products/bare-metal/#pricing')
    vultr_machines = vultrExtractor.extract()
    generic_machines = [vultr_machine.to_generic_machine() for vultr_machine in vultr_machines]

    if '--print' in sys.argv:
        for machine in generic_machines:
            print(machine)

    if '--json' in sys.argv:
        with open('machines.json', 'w', encoding='utf-8') as output_file:
            json.dump(
                [machine.__dict__ for machine in generic_machines],
                output_file
            )
