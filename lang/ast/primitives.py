from .base import Base
class Primitive(Base):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def walk(self):
		print(str(self) + " with value: " + str(self.value))
	def s(self):
		return str(self.value)
class Number(Primitive):
	pass
