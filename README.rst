.. SPDX-License-Identifier: CC0-1.0
.. SPDX-FileCopyrightText: 2017-2019, Sven Eckelmann <sven@narfation.org>

=======================================
Freifunk Vogtland Gateway Configuration
=======================================

Ansible Configuration for Freifunk Vogtland Gateways

Requirements on Ansible Host
============================

* Ansible (v2.7+)

Requirements on Gateway
=======================

Debian Bullseye, plus:

* openssh-server
* python3
* sudo

Starting playbook
=================

on all servers
--------------

::

  ansible-playbook site.yml -u $USER

on a specific server
--------------------

::
  ansible-playbook site.yml -u $USER --limit vpn01

Vagrant test
============

The vagrant test environment is build around vagrant-libvirt. It requires

* vagrant-libvirt
* libvirt-daemon
* libvirt-daemon-system

The setup of the boxes are automated using

::
  vagrant --provider=libvirt up

The virtual machine can be accessed using

::
  vagrant --provider=libvirt ssh
