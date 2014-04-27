class Base():
	def __init__(self, **kwargs):
		for name,value in kwargs.items():
			print(name,value)
			setattr(self,name,value)
	def pprint(self, indent):
		print(indent*' ' + str(self))
		for k,i in vars(self).items():
			if isinstance(i, Base):
				i.pprint(indent+2)
