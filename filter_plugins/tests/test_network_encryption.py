import unittest

from filter_plugins.network_encryption import *


class NetworkEncryptionTest(unittest.TestCase):

    def test_networks(self):
        networks = [{
            'name': 'default',
            'psk': 'secret'
        }]
        hostvars = {
            'one' : {
                'network_encryption_host_networks': [{
                    'name': 'default'
                }]
            }
        }

        result = get_networks(networks, hostvars)

        self.assertEqual(result, [{
            'name': 'default',
            'psk': 'secret',
            'hosts': ['one']
        }])
