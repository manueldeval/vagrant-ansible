# -*- mode: ruby -*-
# vi: set ft=ruby :

#vagrant --custom-option='{"ansible_limit":"lb1"}' provision


require 'json'
require 'yaml'
require 'getoptlong'
require_relative 'ruby/vagrant_helper'
require_relative 'ruby/ansible_helper'
require_relative 'ruby/custom_args'

customArgs = CustomArgs.new

# VAGRANT configuration
Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox"

  serversFromJson = YAML::load(File.open("#{customArgs.playbook_path}/servers.yml"))

  AnsibleHelper.createAnsibleInventory(serversFromJson,"#{customArgs.playbook_path}/hosts")
  VagrantHelper.createServers(serversFromJson,config,customArgs.box_type,customArgs.playbook_path)
end
