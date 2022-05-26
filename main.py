import sys

from extractors.vultr_extractor import VultrExtractor

if __name__ == '__main__':
    vultrExtractor = VultrExtractor('https://www.vultr.com/products/bare-metal/#pricing')
    vultr_machines = vultrExtractor.extract()

    if '--print' in sys.argv:
        for machine in vultr_machines:
            print(machine.to_generic_machine())
