require 'getoptlong'
require 'json'

class CustomArgs

	attr_accessor :customOptions

	# JSON Attributes
	attr_accessor :box_type
	attr_accessor :playbook_path

	def initialize

		@customOptions={}
		ARGV.each do |a|
			if a.start_with?("--custom-option=")
				json = a.split("=")[1]
				puts "#{json}"
				@customOptions = JSON.parse(json)
			end
		end

		@playbook_path=""
        if @customOptions.has_key?("playbook_path")
			@playbook_path=customOptions["playbook_path"]
		elsif ENV.has_key?("playbook_path")
			@playbook_path=ENV["playbook_path"]
        end

		@box_type=""
        if @customOptions.has_key?("box_type")
			@box_type=customOptions["box_type"]
		elsif ENV.has_key?("box_type")
			@box_type=ENV["box_type"]
        end

        if @playbook_path == "" || @box_type == ""
        	if File.exist?('.config')
        		file = File.read('.config')
				data = JSON.parse(file)
				@playbook_path = data["playbook_path"]
				@box_type = data["box_type"]				
        	else
        		puts "You must provide box_type and playbook_path :"
        		puts " >> As an environment var"
        		puts " $ export box_type=ubuntu/vivid64"
				puts " $ export playbook_path=infrastructures/haproxy_simple"
        		puts " "
				puts " >> or as a vagrant custom-option"
				puts " vagrant --custom-option='{\"box_type\":\"ubuntu/vivid64\",\"playbook_path\":\"infrastructures/haproxy_simple\"}' up/provision/..."
        		puts " "				
				puts " >> or in the .config file"
				puts " $ cat ./.config"
				puts " $ {\"box_type\":\"ubuntu/vivid64\",\"playbook_path\":\"infrastructures/haproxy_simple\"}"
        		exit 
        	end
        end

		File.open(".config", "w") do |f| 
			f.write("{\"box_type\":\""+@box_type+"\",\"playbook_path\":\""+@playbook_path+"\"}")
		end

	end

	def to_s
		s = "=========================================\n"
		s << "Custom arguments: \n"
		s << "	box_type      : #{@box_type}\n"
		s << "	playbook_path : #{@playbook_path}\n"
		s << "=========================================\n"
	end
end