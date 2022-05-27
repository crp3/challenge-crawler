import sys
import json

from extractors.vultr_extractor import VultrExtractor
from utils.output_utils import print_machines, save_json

if __name__ == '__main__':
    vultrExtractor = VultrExtractor('https://www.vultr.com/products/bare-metal/#pricing')
    vultr_machines = vultrExtractor.extract()
    generic_machines = [vultr_machine.to_generic_machine() for vultr_machine in vultr_machines]

    if '--print' in sys.argv:
        print_machines(generic_machines)

    if '--json' in sys.argv:
        save_json(generic_machines)
