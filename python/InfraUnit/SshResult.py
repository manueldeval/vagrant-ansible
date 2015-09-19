
class SshResult:

	def __init__(self,stdout,stderr,status):
		self.stdout = stdout
		self.stderr = stderr
		self.status = status

	def isStatus(self,value):
		return self.status == value

	def isSuccess(self):
		return self.status == 0

	def isError(self):
		return self.status != 0

	def stdoutContains(self,str):
		return (str in self.stdout)

	def stderrContains(self,str):
		return (str in self.stderr)

	def __str__(self):
		return ('status: ' + str(self.status) +'\n'+ 
     		'stdout #############################\n' + self.stdout +'\n'+ 
			'stderr #############################\n' + self.stderr)
