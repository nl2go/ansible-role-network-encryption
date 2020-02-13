import unittest

from filter_plugins.network_encryption import *


class NetworkEncryptionTest(unittest.TestCase):

    def test_init(self):
        module = FilterModule()
        filters = module.filters()

        self.assertEqual(filters.get('network_encryption_point_to_point_connections'), network.get_point_to_point_connections)
        self.assertEqual(filters.get('network_encryption_configs'), get_network_encryption_configs)

    def test_get_network_encryption_configs(self):
        configs = [{
            'name': 'default',
            'psk': 'secret'
        }]
        play_hosts = ['one']
        hostvars = {
            'one' : {
                'network_encryption_host_configs': [{
                    'name': 'default'
                }]
            }
        }

        result = get_network_encryption_configs(configs, play_hosts, hostvars)

        self.assertEqual(result, [{
            'name': 'default',
            'psk': 'secret',
            'hosts': ['one'],
            'absent_hosts': []
        }])

    def test_get_network_encryption_configs_absent(self):
        configs = [{
            'name': 'default',
            'psk': 'secret'
        }]
        play_hosts = ['one']
        hostvars = {
            'one' : {
                'network_encryption_host_configs': [{
                    'name': 'default',
                    'state': 'absent'
                }]
            }
        }

        result = get_network_encryption_configs(configs, play_hosts, hostvars)

        self.assertEqual(result, [{
            'name': 'default',
            'psk': 'secret',
            'hosts': [],
            'absent_hosts': ['one']
        }])