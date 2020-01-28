import unittest

from filter_plugins.network_encryption import *


class NetworkEncryptionTest(unittest.TestCase):

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
            'hosts': ['one']
        }])
