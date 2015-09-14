# -*- mode: ruby -*-
# vi: set ft=ruby :

#vagrant --custom-option="ansible-limit:all" provision


require 'json'
require 'yaml'
require 'getoptlong'
require_relative 'ruby/vagrant_helper'
require_relative 'ruby/ansible_helper'
require_relative 'ruby/custom_args'

customArgs = CustomArgs.new
puts "#{customArgs}"

# VAGRANT configuration
Vagrant.configure(2) do |config|

  serversFromJson = YAML::load(File.open('servers.yml'))

  VagrantHelper.createServers(serversFromJson,config,customArgs.box_type)
  AnsibleHelper.createAnsibleInventory(serversFromJson,'./provisioning/hosts');

  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "provisioning/playbook.yml"
        ansible.inventory_path = "provisioning/hosts"
        ansible.extra_vars = "provisioning/extra_vars.yml"
        ansible.limit=customArgs.ansible_limit
  end
end
