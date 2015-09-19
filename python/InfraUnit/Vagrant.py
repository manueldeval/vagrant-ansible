from Shell import Shell

class Vagrant:

	@staticmethod
	def start(name):
		command = "vagrant up "+name
		print command
		shell = Shell(command).execute()
		return shell.status == 0

	@staticmethod
	def shutdown(name):
		command = "vagrant halt "+name
		print command
		shell = Shell(command).execute()
		return shell.status == 0

	@staticmethod
	def delete():
		command = "vagrant destroy --force"
		print command
		shell = Shell(command).execute()
		return shell.status == 0

	@staticmethod
	def create(box,infra):
		command = "vagrant --custom-option='{\"playbook_path\":\""+infra+"\",\"box_type\":\""+box+"\"}' up --provider=virtualbox ";
		print command
		shell = Shell(command).execute()
		return shell.status == 0		








