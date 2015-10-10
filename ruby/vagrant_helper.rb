class VagrantHelper

	def self.createServer(srv,config,boxType,playbook_path,doProvision)
	  config.vm.define srv["name"] do |server|
	    server.vm.hostname=srv["name"]
	    server.vm.box = boxType
	    server.vm.network "private_network", ip: srv["ip"]
	    config.vm.provider "virtualbox" do |v|
	        v.memory = srv["memory"]
	        v.cpus = srv["cpus"]
	    end
	    if doProvision
    		server.vm.provision :ansible do |ansible|
				ansible.sudo = true
				ansible.limit = 'all'
				ansible.playbook = "#{playbook_path}/playbook.yml"
				ansible.inventory_path = "#{playbook_path}/hosts"
				if File.exist?("#{playbook_path}/extra_vars.yml")
					ansible.extra_vars = "#{playbook_path}/extra_vars.yml"
				end
    		end 	
	    end
	  end  
	end

	# Create all servers
	def self.createServers(servers,config,boxType,playbook_path)
  		servers.each_with_index do |srv,index|
    		doProvision = (index+1) == servers.length 
    		self.createServer(srv,config,boxType,playbook_path,doProvision)
  		end
	end

end

