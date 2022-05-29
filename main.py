import sys

from utils.output_utils import OutputFormatter
from extractors.vultr_extractor import VultrExtractor
from extractors.hostgator_extractor import HostgatorExtractor
from converters.generic_machine_converter import GenericMachineConverter

if __name__ == '__main__':
    vultr_extractor = VultrExtractor('https://www.vultr.com/products/bare-metal/#pricing')
    hostgator_extractor = HostgatorExtractor('https://www.hostgator.com/vps-hosting')

    vultr_machines = vultr_extractor.extract()
    hostgator_machines = hostgator_extractor.extract()

    machines = vultr_machines + hostgator_machines
    generic_machines = [GenericMachineConverter.convert(machine) for machine in machines]
    output_formatter = OutputFormatter(generic_machines)

    if '--print' in sys.argv:
        output_formatter.print_machines()

    if '--save_json' in sys.argv:
        output_formatter.save_json()

    if '--save_csv' in sys.argv:
        output_formatter.save_csv()
