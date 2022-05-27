import sys

from extractors.vultr_extractor import VultrExtractor
from utils.output_utils import OutputFormatter

if __name__ == '__main__':
    vultrExtractor = VultrExtractor('https://www.vultr.com/products/bare-metal/#pricing')
    vultr_machines = vultrExtractor.extract()
    generic_machines = [vultr_machine.to_generic_machine() for vultr_machine in vultr_machines]
    output_formatter = OutputFormatter(generic_machines)

    if '--print' in sys.argv:
        output_formatter.print_machines()

    if '--save_json' in sys.argv:
        output_formatter.save_json()

    if '--save_csv' in sys.argv:
        output_formatter.save_csv()
