import yaml
from Server import Server


class Infrastructure:

	def __init__(self,infraPath,vagrantPath):
		yml = infraPath+"/servers.yml"
		self.config = {}
		self.servers = {}
		with open(yml, 'r') as stream:
			serversYml = yaml.load(stream)
			for serverYml in serversYml:
				self.servers[serverYml["name"]] = Server(serverYml["name"],serverYml["ip"],vagrantPath+"/.vagrant/machines/"+serverYml["name"]+"/virtualbox/private_key")

	def init(self):
		for name in self.servers:
			self.servers[name].init()
		return self

	def server(self,name):
		return self.servers[name]

	def __str__(self):
		str = ""
		for server in self.servers:
			str=str+"---------------------\n"
			str=server.__strs__()
		return str
