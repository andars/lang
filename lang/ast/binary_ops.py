from .base import Base
class BinaryOperator(Base):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
	def walk(self):
		print(self)
		self.left.walk()
		self.right.walk()
class Addition(BinaryOperator):
	def s(self):
		return "(+ " + self.left.s() + " " + self.right.s() + " )"
	
class Subtraction(BinaryOperator):
	def s(self):
		return "(- " + self.left.s() + " " + self.right.s() + " )"
	
class Multiplication(BinaryOperator):
	def s(self):
		return "(* " + self.left.s() + " " + self.right.s() + " )"

class Division(BinaryOperator):
	def s(self):
		return "(/ " + self.left.s() + " " + self.right.s() + " )"
