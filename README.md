[![Travis (.org) branch](https://img.shields.io/travis/nl2go/ansible-role-network-encryption/master)](https://travis-ci.org/nl2go/ansible-role-network-encryption)
[![Codecov](https://img.shields.io/codecov/c/github/nl2go/ansible-role-network-encryption)](https://codecov.io/gh/nl2go/ansible-role-network-encryption)
[![Ansible Galaxy](https://img.shields.io/badge/role-nl2go.network_encryption-blue.svg)](https://galaxy.ansible.com/nl2go/network_encryption/)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/nl2go/ansible-role-network-encryption)](https://galaxy.ansible.com/nl2go/network_encryption)
[![Ansible Galaxy Downloads](https://img.shields.io/ansible/role/d/46005.svg?color=blue)](https://galaxy.ansible.com/nl2go/network_encryption/)

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

    network_encryption_configs:
      - name: default
        psk: secret
        
Configuration sets must be configured using `network_encryption_configs` variable. The `name` of the configuration set is mandatory and
used for identification. Pre-shared key can be specified using `psk`.

    network_encryption_host_configs:
      - name: default

Hosts can be attached to a configuration set using `network_encryption_host_configs` variable. Configuration sets are referenced by `name`.      

    network_encryption_host_configs:
      - name: default
        state: absent

A host can be detached from the configuration set using `state: absent`.        

    network_encryption_configs:
      - name: default
        interface: eth0
        psk: secret

The interface can be specified using `interface` variable. If not specified, it defaults to `ansible_default_ipv4.interface`.

    network_encryption_configs:
      - name: default
        psk: secret
        params:
            lifetime: 8h
            
General connection parameters like `lifetime` may be set within `params` section (s. [ipsec.conf](https://wiki.strongswan.org/projects/strongswan/wiki/ConnSection) for full parameter description).

    network_encryption_default_config_params:
      ike: aes256gcm16-prfsha384-modp4096,aes256gcm16-prfsha384-ecp384!
      esp: aes256gcm16-modp4096,aes256gcm16-ecp384!
      keyingtries: 0
      ikelifetime: 1h
      lifetime: 8h
      dpddelay: 30
      dpdtimeout: 120
      dpdaction: clear
      authby: secret
      keyexchange: ikev2
      type: tunnel

The `params` within `network_encryption_configs` extend/override default connection parameters present above. 

    network_encryption_config_dir: "/etc/ipsec.d/{{ role_name }}"
    
Defines the custom IPsec configuration directory for isolation purposes.

## Tags

Tags can be used to limit the role execution to a particular task module. Following tags are available:

- `network_encryption`: Covers the full role lifecycle.
- `network_encryption_variables`|`variables`: Gathers OS specific variables
- `network_encryption_install`|`install`: Installs required packages
- `network_encryption_config`|`config`: Configures required packages

## Dependencies

None.

## Example Playbook

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
