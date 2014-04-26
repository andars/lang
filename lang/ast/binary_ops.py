from .base import Base
class BinaryOperator(Base):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
	def walk(self):
		print(self)
		self.left.walk()
		self.right.walk()
class Addition(BinaryOperator):
	pass
class Subtraction(BinaryOperator):
	pass
class Multiplication(BinaryOperator):
	pass
class Division(BinaryOperator):
	pass
