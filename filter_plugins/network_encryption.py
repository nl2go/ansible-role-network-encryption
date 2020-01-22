#!/usr/bin/python


class FilterModule(object):
    def filters(self):
        return {
          'network_encryption_point_to_point_connections': self.point_to_point_connections,
          'network_encryption_networks': self.networks
        }

    def get_custom_interface_name_or_default(self, hostname, hostvars, interface_variable_name = None):
        if interface_variable_name:
            return self.get_custom_interface_name(hostname, hostvars, interface_variable_name)

        return self.get_default_interface_name(hostname, hostvars)

    def get_interface_address(self, hostname, hostvars, interface_name):
        interface = hostvars.get(hostname).get('ansible_' + interface_name)
        if interface:
            return interface.get('ipv4').get('address')

        raise Exception('Interface "{}" is not found for host "{}".'.format(interface, hostname))

    def get_custom_interface_name(self, hostname, hostvars, interface_variable_name):
        interface_name = hostvars.get(hostname).get(interface_variable_name)

        if interface_name:
            return interface_name

        raise Exception('Variable "{}" is not defined for host "{}".'.format(interface_variable_name, hostname))

    def get_default_interface_name(self, hostname, hostvars):
        return hostvars.get(hostname).get('ansible_default_ipv4').get('interface')

    def point_to_point_connections(self, remote_hostnames, hostname, hostvars, interface_variable_name = None):
        host_interface_name = self.get_custom_interface_name_or_default(hostname, hostvars, interface_variable_name)
        host_interface_address = self.get_interface_address(hostname, hostvars, host_interface_name)

        connections = []

        for remote_hostname in remote_hostnames:
            if hostname == remote_hostname:
                continue

            remote_host_interface_name = self.get_custom_interface_name_or_default(remote_hostname, hostvars, interface_variable_name)
            remote_host_interface_address = self.get_interface_address(remote_hostname, hostvars, remote_host_interface_name)

            connections.append({
              'local': {
                'hostname': hostname,
                'interface': host_interface_name,
                'address': host_interface_address
              },
              'remote': {
                'hostname': remote_hostname,
                'interface': remote_host_interface_name,
                'address': remote_host_interface_address
              }
            })

        return connections

    def networks(self, networks, hostvars, variable_name='network_encryption_host_networks'):
        networks = self.list_to_dict(networks)

        for host in hostvars:
            host_config = hostvars.get(host)
            host_networks = host_config.get(variable_name)
            if host_networks:
                for host_network in host_networks:
                    network_name = host_network.get('name')
                    network = networks.get(network_name)
                    hosts = network.get('hosts')
                    if not hosts:
                        hosts = []
                        network['hosts'] = hosts
                    hosts.append(host)
        return list(networks.values())

    def list_to_dict(self, objs, attr='name'):
        obj_dict = {}
        for obj in objs:
            key = obj.get(attr)
            obj_dict[key] = obj

        return obj_dict
