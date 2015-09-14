class AnsibleHelper

	# Create ansible inventory
	def self.createAnsibleInventory(servers,hostFile)
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

end