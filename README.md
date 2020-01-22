[![Travis (.org) branch](https://img.shields.io/travis/nl2go/ansible-role-network-encryption/master)](https://travis-ci.org/nl2go/ansible-role-network-encryption)
[![Codecov](https://img.shields.io/codecov/c/github/nl2go/ansible-role-network-encryption)](https://codecov.io/gh/nl2go/ansible-role-network-encryption)
[![Ansible Galaxy](https://img.shields.io/badge/role-nl2go.network_encryption-blue.svg)](https://galaxy.ansible.com/nl2go/network_encryption/)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/nl2go/ansible-role-network-encryption)](https://galaxy.ansible.com/nl2go/network_encryption)
[![Ansible Galaxy Downloads](https://img.shields.io/ansible/role/d/45353.svg?color=blue)](https://galaxy.ansible.com/nl2go/network_encryption/)

# Ansible Role: Network Encryption

An Ansible Role that manages network encryption between inventory hosts based on [IPsec](https://de.wikipedia.org/wiki/IPsec) / [strongSwan](https://www.strongswan.org/).

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    network_encryption_charon_port: 500
 
UDP port used locally. If set to 0 a random port will be allocated (s. [strongswan.conf](https://wiki.strongswan.org/projects/strongswan/wiki/StrongswanConf)).

    network_encryption_port_nat_t: 4500
    
UDP port used locally in case of NAT-T. If set to 0 a random port will be allocated. Has to be different from charon.port, otherwise a random port will be allocated (s. [strongswan.conf](https://wiki.strongswan.org/projects/strongswan/wiki/StrongswanConf)).

    network_encryption_networks:
      - name: default
        psk: secret
        
Separate networks can be configured using `network_encryption_networks` variable. The `name` of the network is mandatory and
used for identification. Pre-shared key can be specified using `psk`.

    network_encryption_host_networks:
      - name: default

Hosts can be attached to the networks using `network_encryption_host_networks` variable. Networks are referenced by `name`.      

## Tags

Tags can be used to limit the role execution to a particular task module. Following tags are available:

- `network_encryption`: Covers the full role lifecycle.
- `network-encryption-variables`: Gathers OS specific variables
- `network-encryption-install`: Installs required packages
- `network-encryption-config`: Configures required packages

## Dependencies

None.

## Example Playbook

Since the role is managing the communication with the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html)
only, it may be run on localhost.

    - hosts: all
      roles:
         - nl2go.network_encryption
              
## Development
Use [docker-molecule](https://github.com/nl2go/docker-molecule) following the instructions to run [Molecule](https://molecule.readthedocs.io/en/stable/)
or install [Molecule](https://molecule.readthedocs.io/en/stable/) locally (not recommended, version conflicts might appear).


Use following to run tests:

    molecule test --all

## Maintainers

- [build-failure](https://github.com/build-failure)

## License

See the [LICENSE.md](LICENSE.md) file for details.

## Author Information

This role was created by in 2019 by [Newsletter2Go GmbH](https://www.newsletter2go.com/).
