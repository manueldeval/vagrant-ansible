require 'getoptlong'
require 'json'

class CustomArgs

	attr_accessor :customOptions
	attr_accessor :ansible_limit
	attr_accessor :box_type

	def initialize
		opts = GetoptLong.new(
		  [ '--custom-option', GetoptLong::OPTIONAL_ARGUMENT ]
		)

		@customOptions={}
		opts.each do |opt, arg|
			case opt
		    	when '--custom-option'
		      		@customOptions = JSON.parse(arg)
			end
		end

		@ansible_limit="all"
        if @customOptions.has_key?("ansible_limit")
			@ansible_limit=customOptions["ansible_limit"]
        end

		@box_type="ubuntu/vivid64"
        if @customOptions.has_key?("box_type")
			@box_type=customOptions["box_type"]
        end
	end

	def to_s
		s = "=========================================\n"
		s << "Custom arguments: \n"
		s << "	ansible_limit : #{@ansible_limit}\n"
		s << "	box_type      : #{@box_type}\n"
		s << "=========================================\n"
	end
end