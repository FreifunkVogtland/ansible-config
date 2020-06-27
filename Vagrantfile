# -*- mode: ruby -*-
# vi: set ft=ruby :
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2017-2020, Sven Eckelmann <sven@narfation.org>


# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.provision "shell",
    inline: "apt-get install sudo python"

  config.vm.provision "ansible" do |ansible|
    ansible.groups = {
      "gk-vpns" => ["vpn01"],
      "hetzner-vpns" => ["vpn03", "vpn04", "vpn06"],
      "linevast-vpns" => ["vpn05"],
      "vpns:children" => ["gk-vpns", "hetzner-vpns", "linevast-vpns"]
    }

    ansible.playbook = "site.yml"
    ansible.extra_vars = {
        ansible_python_interpreter: "/usr/bin/env python2",
        gateway_if: "ens5",
    }
    ansible.skip_tags=["icvpn", "ffmap-backup"]
  end

  config.vm.define "vpn01" do |machine|
    machine.vm.box = "debian/buster64"
    machine.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:00:00:01"
    end
  end

  config.vm.define "vpn03" do |machine|
    machine.vm.box = "debian/buster64"
    machine.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:00:00:03"
    end
  end

  config.vm.define "vpn04" do |machine|
    machine.vm.box = "debian/buster64"
    machine.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:00:00:04"
    end
  end

  config.vm.define "vpn05" do |machine|
    machine.vm.box = "debian/buster64"
    machine.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:00:00:05"
    end
  end

  config.vm.define "vpn06" do |machine|
    machine.vm.box = "debian/buster64"
    machine.vm.provider :libvirt do |domain|
      domain.management_network_mac = "52:54:00:00:00:06"
    end
  end
end
