from .base import Base

class Symbol(Base):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def s(self):
		return self.name
