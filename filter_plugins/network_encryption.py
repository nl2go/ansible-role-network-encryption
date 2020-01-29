#!/usr/bin/python

from ansible_filter import network
from ansible_filter import list_to_dict


class FilterModule(object):
    def filters(self):
        return {
            'network_encryption_point_to_point_connections': network.get_point_to_point_connections,
            'network_encryption_configs': get_network_encryption_configs
        }


def get_network_encryption_configs(configs, play_hosts, hostvars, variable_name='network_encryption_host_configs'):
    configs = list_to_dict(configs)

    for config_name in configs:
        config = configs.get(config_name)
        config['hosts'] = []
        config['absent_hosts'] = []

    for host in play_hosts:
        host_config = hostvars.get(host)
        host_configs = host_config.get(variable_name)
        if host_configs:
            for host_config in host_configs:
                config_name = host_config.get('name')
                host_config_state = host_config.get('state', 'present')
                config = configs.get(config_name)

                if host_config_state == 'present':
                    hosts = config.get('hosts')
                    hosts.append(host)
                else:
                    absent_hosts = config.get('absent_hosts')
                    absent_hosts.append(host)

    return list(configs.values())
