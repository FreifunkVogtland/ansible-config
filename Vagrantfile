# -*- mode: ruby -*-
# vi: set ft=ruby :

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
      "vpns:children" => ["gk-vpns", "hetzner-vpns", "linevast-vpns"],
      "gk-firmwares" => ["build01"],
      "firmwares:children" => ["gk-firmwares"]
    }

    ansible.playbook = "site.yml"
    ansible.extra_vars = {
        ansible_python_interpreter: "/usr/bin/env python2",
        gateway_if: "ens5",
    }
    ansible.skip_tags=["icvpn", "ffmap-backup"]
  end

  config.vm.network "private_network", type: "dhcp"

  config.vm.define "vpn01" do |config|
    config.vm.box = "debian/stretch64"
  end

  config.vm.define "vpn03" do |config|
    config.vm.box = "debian/stretch64"
  end

  config.vm.define "vpn04" do |config|
    config.vm.box = "debian/stretch64"
  end

  config.vm.define "vpn05" do |config|
    config.vm.box = "debian/stretch64"
  end

  config.vm.define "vpn06" do |config|
    config.vm.box = "debian/stretch64"
  end

  config.vm.define "build01" do |config|
    config.vm.box = "debian/stretch64"
  end
end
