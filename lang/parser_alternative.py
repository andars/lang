import lang.ast as ast

class AlternativeParser():
	def __init__(self, lexer):
		self.lexer = lexer
		self.statements = []
		self.peeked = None

	def expect(self, types):
		self.next_token()
		if not self.token().type in types:
			self.error("unexpected type: "+self.token().type)

	def token(self):
		return self.current or self.error()
	def error(self, msg):
		print("ERROR: " + msg)
		raise Exception

	def next_token(self):
		self.current = self.peeked or self.lexer.next_token()
		self.peeked = None
		return self.token()
	
	def try_peek_token(self):
		if not self.peeked:
			self.peeked = self.lexer.next_token()
		return self.peeked != None # or just self.peeked?			
	
	def peek_token(self):
		if not self.peeked:
			self.peeked = self.lexer.next_token()
		if not self.peeked:
			raise Error
		return self.peeked
	def save(self):
		return [self.current, self.peeked, self.lexer.save()]

	def load(self, state):
		self.current = state[0]
		self.peeked = state[1]
		self.lexer.load(state[2])
	
	def parse(self):
		while self.try_peek_token():
			expr = self.expression()
			if expr: self.statements.append(expr)

	def expression(self):
		print("looking for expression")
		expr = self.add_sub_expr()
		print("found expr" + str(expr))
		return expr
	
	def add_sub_expr(self):
		nodes = {
			'PLUS': ast.Addition,
			'MINUS': ast.Subtraction
		}
		expr = self.mult_div_expr()
		print("found lhs: "+str(expr))
		
		while self.try_peek_token() and self.peek_token().type in nodes.keys():
			print('looking for plus')
			expr = nodes[self.next_token().type](left=expr, right=self.mult_div_expr())
		return expr

	def mult_div_expr(self):
		nodes  = {
			'MULT': ast.Multiplication,
			'DIV': ast.Division
		}
		expr = self.value_expr()
		while self.try_peek_token() and self.peek_token().type in nodes.keys():
			expr = nodes[self.next_token().type](left=expr, right=self.value_expr())
		return expr

	
	def value_expr(self):
		peek_type = self.peek_token().type
		if peek_type == 'INTEGER':
			self.expect('INTEGER')
			return ast.Number(value=self.token().value)
		elif peek_type == 'LPAREN':
			self.expect('LPAREN')
			expr = self.expression()	
			self.expect('RPAREN')
			return expr
		elif peek_type == 'SYMBOL':
			self.expect('SYMBOL')
			return ast.Symbol(name=self.token().value) 
		else:
			self.error()

