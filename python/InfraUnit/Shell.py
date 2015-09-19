import subprocess
import sys
import select

class Shell:

	def __init__(self,command):
		self.command = command

	def execute(self):
		stdout = []
		stderr = []
		p = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		while True:
			reads = [p.stdout.fileno(), p.stderr.fileno()]
			ret = select.select(reads, [], [])
			for fd in ret[0]:
				if fd == p.stdout.fileno():
					read = p.stdout.readline()
					sys.stdout.write(read)
					stdout.append(read)
				if fd == p.stderr.fileno():
					read = p.stderr.readline()
					sys.stderr.write(read)
					stderr.append(read)
			if p.poll() != None:
				break
		self.stdout = "".join(stdout)
		self.stderr = "".join(stderr)
		self.status = p.returncode
		return self

