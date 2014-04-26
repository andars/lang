class VMException(Exception):
    pass

class VM():
	def __init__(self, code):
		self.stack = []
		self.scope = {
			"sweg": 15
		}
		self.code = list(filter(bool,code))
		self.ip = 0

	def run(self):
		while True:
			if self.ip > len(self.code):
				print("end")
				return
			
			line = self.code[self.ip].split(' ')
			
			self.ip += 1 
			op, arg = line[0], line[1:]
			print(str(self.ip) + ": " + op, end=' ')
			try:
				handler = getattr(self, op)
				handler(arg)
			except AttributeError:
				print("invalid opcode: {0}".format(op))
				break
			print(self.stack)
			
	
	#OPCODE HANDLERS
	def rjmp(self, arg):
		self.ip += int(arg[0])
		if self.ip < 0 or self.ip > len(self.code):
			raise VMException("invalid instruction pointer after rjmp")

	def jmp(self, arg):
		print("jumping to {0}".format(int(arg[0])))
		self.ip = int(arg[0])
		if self.ip < 0 or self.ip > len(self.code):
			raise Error
	
	def jmpne(self,arg):
		a = self.stack.pop()
		b = self.stack.pop()
		print(a, b)
		if a != b:
			self.jmp(arg)
	
	def get(self,arg):
		label = arg[0][1:]
		self.stack.append(self.scope[label] if label in self.scope else None)

	def set(self,arg):
		if arg[0][0] != '#':
			print("invalid syntax")
			raise Error

		label = arg[0][1:]
		value = self.stack.pop()
		self.scope[label] = value

	def mul(self,arg):
		left = self.stack.pop()
		right = self.stack.pop()
		self.stack.append(float(right) * float(left))
	
	def add(self,arg):
		left = self.stack.pop()
		right = self.stack.pop()
		self.stack.append(float(left) + float(right))

	def sub(self,arg):
		left = self.stack.pop()
		right = self.stack.pop()
		self.stack.append(float(left) - float(right))

	def push(self,arg):
		val = arg[0]
		if val[0] == '#':
            self.get(arg)
		elif VM.is_number(arg[0]):
			self.stack.append(float(arg[0]))

	def print(self, arg):
		val = arg[0]
		if val[0] == '"':
			print(val)
		else:
			print(self.scope[val])
	# HELPERS
	@staticmethod
	def is_number(val):
		try: 
			float(val)
			return True
		except ValueError:
			return False


