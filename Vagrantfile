# -*- mode: ruby -*-
# vi: set ft=ruby :

#vagrant --custom-option="ansible-limit:all" provision


require 'json'
require 'yaml'
require 'getoptlong'

#custom options
opts = GetoptLong.new(
  [ '--custom-option', GetoptLong::OPTIONAL_ARGUMENT ]
)

customOptions={}

opts.each do |opt, arg|
  case opt
    when '--custom-option'
      customOptions = JSON.parse(arg)
  end
end

# Set the BOX type
$BOX_TYPE="ubuntu/vivid64"

# Create one server
def createServer(srv,config)
  config.vm.define srv["name"] do |server|
    server.vm.hostname=srv["name"]
    server.vm.box = $BOX_TYPE
    server.vm.network "private_network", ip: srv["ip"]
    
    config.vm.provider "virtualbox" do |v|
        v.memory = srv["memory"]
        v.cpus = srv["cpus"]
    end
  end  
end

# Create all servers
def createServers(servers,config)
  servers.each do |srv|
    createServer(srv,config)
  end
end

# Create ansible inventory
def createAnsibleInventory(servers)
  groups = servers.reduce(Hash.new) do |memo,srv| 
    srv["groups"].each do |group|
      if memo.has_key?(group)
        memo[group].push(srv)
      else
        memo[group] = [ srv ]
      end
    end
    memo
  end

  File.open("./provisioning/hosts", 'w') { |file| 
    file.write("# Generated file\n\n")

    servers.each do |srv|
      file.write("#{srv["name"]} ansible_ssh_host=#{srv["ip"]} ansible_ssh_private_key_file=.vagrant/machines/#{srv["name"]}/virtualbox/private_key\n")
    end
    file.write("\n")

    groups.keys.each do |groupName|
      file.write("[#{groupName}]\n")
      servers = groups[groupName].each do |srv|
        file.write("#{srv["name"]}\n")
      end
      file.write("\n")
    end
    file.write("\n")
  }

end

# VAGRANT configuration
Vagrant.configure(2) do |config|

  serversFromJson = YAML::load(File.open('servers.yml'))

  createServers(serversFromJson,config)
  createAnsibleInventory(serversFromJson)

  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "provisioning/playbook.yml"
        ansible.inventory_path = "provisioning/hosts"
        ansible.extra_vars = "provisioning/extra_vars.yml"
        if customOptions.has_key?("ansible_limit")
          ansible.limit=customOptions["ansible_limit"]
        end
  end
end





  #config.vm.define "demo2" do |demo2|
  #  demo2.vm.box = "ubuntu/vivid64"
  #  demo2.vm.network "private_network", ip: "192.168.33.11"
  #end


  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  #config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL