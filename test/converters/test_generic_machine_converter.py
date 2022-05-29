import unittest

from models.vultr_machine import VultrMachine
from models.generic_machine import GenericMachine
from models.hostgator_machine import HostgatorMachine
from converters.generic_machine_converter import GenericMachineConverter

class TestGenericMachineConverter(unittest.TestCase):
    def test_convert_vultr_machine(vultr_machine):
        vultr_machine = VultrMachine(
            '$395',
            '100 SSD',
            '48 cores',
            '16 GB RAM',
            'Unmetered bandwidth',
            'Unlimited network'
        )

        expected = GenericMachine(
            vultr_machine.cpu,
            vultr_machine.memory,
            vultr_machine.storage,
            vultr_machine.bandwidth,
            vultr_machine.price
        )

        assert GenericMachineConverter.convert(vultr_machine) == expected
        
    def test_convert_hostgator_machine(hostgator_machine):
        hostgator_machine = HostgatorMachine(
            '16GB RAM',
            '24 cores',
            '200 SSD',
            'Unmetered bandwidth',
            '$100'
        )

        expected = GenericMachine(
            hostgator_machine.cpu,
            hostgator_machine.memory,
            hostgator_machine.storage,
            hostgator_machine.bandwidth,
            hostgator_machine.price
        )

        assert GenericMachineConverter.convert(hostgator_machine) == expected
