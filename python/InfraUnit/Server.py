import paramiko
from SshResult import SshResult
from Vagrant import Vagrant

class Server:

	def __init__(self,name,ip,privateKey):
		self.name = name
		self.ip = ip
		self.sudo = False
		self.privateKey = privateKey
		self.distribution = ""
		self.release = ""

	def init(self):
		self.initDistribution()
		self.initRelease()
		self.determineSudo()
		return self

	def determineSudo(self):
		#if self.distribution in ["ubuntu","debian","centos"]:
		# always sudo with vagrant
		self.sudo = True

	def initDistribution(self):
		sshResult = self._ssh("cat /etc/*-release | grep '^ID='")
		lines = sshResult.stdout.rstrip("\n").split("\n")
		if len(lines) == 1:
			self.distribution = lines[0].split("=")[1]

	def initRelease(self):
		sshResult = self._ssh("cat /etc/*-release | grep 'VERSION_ID='")
		lines = sshResult.stdout.rstrip("\n").split("\n")
		if len(lines) == 1:
			self.release = lines[0].split("=")[1]

	def _ssh(self,command):
		k = paramiko.RSAKey.from_private_key_file(self.privateKey)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect( hostname = self.ip, username = "vagrant", pkey = k )
		stdin , stdout, stderr = ssh.exec_command(command)
		stdoutStr = stdout.read()
		stderrStr = stderr.read()
		status = stdout.channel.recv_exit_status()
		ssh.close()
		return SshResult(stdoutStr,stderrStr,status)

	def ssh(self,command):
		if self.sudo == False:
			return self._ssh(command)
		else:
			return self._ssh("sudo bash << \"UNIT_EOF\"\n"+command+"\nUNIT_EOF\n")
	
	def shutdown(self):
		return Vagrant.shutdown(self.name)

	def start(self):
		return Vagrant.start(self.name)

	def __str__(self):
		return ('name         : ' + self.name +'\n'+ 
     		'ip           : ' + self.ip +'\n'+ 
			'sudo         : ' + str(self.sudo) +'\n'+ 
			'privateKey   : ' + self.privateKey+'\n'+ 
			'distribution : ' + self.distribution+'\n'+
			'release      : ' + self.release)
