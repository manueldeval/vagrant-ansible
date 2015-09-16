class VagrantHelper

	def self.createServer(srv,config,boxType)
	  config.vm.define srv["name"] do |server|
	    server.vm.hostname=srv["name"]
	    server.vm.box = boxType
	    server.vm.network "private_network", ip: srv["ip"]
	    config.vm.provider "virtualbox" do |v|
	        v.memory = srv["memory"]
	        v.cpus = srv["cpus"]
	    end
	  end  
	end

	# Create all servers
	def self.createServers(servers,config,boxType)
  		servers.each do |srv|
    		self.createServer(srv,config,boxType)
  		end
	end

end

