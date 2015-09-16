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

		@playbook_path="infrastructures/haproxy_simple"
        if @customOptions.has_key?("playbook_path")
			@playbook_path=customOptions["playbook_path"]
        end

		@box_type="ubuntu/vivid64"
        if @customOptions.has_key?("box_type")
			@box_type=customOptions["box_type"]
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