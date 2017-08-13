Freifunk Vogtland Gateway Configuration
=======================================

Ansible Configuration for Freifunk Vogtland Gateways

## Requirements on Ansible Host

* Ansible (v2.2+)

## Requirements on Gateway

Debian Stretch, plus:

* openssh-server
* python
* sudo

## Starting playbook

### on all servers

    ansible-playbook site.yml -u $USER

### on a specific server

    ansible-playbook site.yml -u $USER --limit vpn01

## Vagrant test

The vagrant test environment is build around vagrant-libvirt. It requires

* vagrant-libvirt
* libvirt-daemon
* libivirt-daemon-system

The setup of the boxes are automated using

    vagrant --provider=libvirt up

The virtual machine can be accessed using

    vagrant --provider=libvirt ssh
