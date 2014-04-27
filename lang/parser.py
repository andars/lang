import lang.ast as ast
class ParseException(Exception):
	pass

op_info = {
	'PLUS': [1, 'LEFT'],
	'MINUS': [1, 'LEFT'],
	'MULT': [2, 'LEFT'],
	'DIV': [2, 'LEFT'],
	'CARET': [3, 'RIGHT']
}
class Parser():
	def __init__(self, lexer):
		self.lexer = lexer
		self.statements = []
		self.peeked = None

	#general parsing utility functions
	def expect(self, types):
		self.next_token()
		if not isinstance(types, list):
			types = [types]
		if not self.token().type in types:
			self.error("unexpected type: "+self.token().type)

	def token(self):
		return self.current or self.error()

	def error(self, msg):
		raise ParseException(msg)

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
			self.error("no next token?!?!")
		return self.peeked

	#save and load allow for more extensive lookahead when necessary
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
		return self.expr(1)

	def expr(self, prec):
		lhs = self.atom()
		while 1:
			if not self.try_peek_token():
				break
			current = self.peek_token()
			if not (current.type in op_info.keys()):
				break
			[op_prec, op_assoc] = op_info[current.type]
			if op_prec < prec:
				break
			self.next_token()
			next_prec = op_prec+1 if op_assoc == 'LEFT' else op_prec
			rhs = self.expr(next_prec)
			lhs = self.op(current, lhs, rhs)
		return lhs
	
	def atom(self):
		peek_type = self.peek_token().type
		if peek_type == 'LPAREN':
			self.expect('LPAREN')
			expr = self.expr(1)
			self.expect('RPAREN')
			return expr
		elif peek_type == 'INTEGER':
			self.expect('INTEGER')
			return ast.Number(value=self.token().value)
		elif peek_type == 'SYMBOL':
			self.expect('SYMBOL')
			return ast.Symbol(name=self.token().value)
		else:
			self.error("unrecognized atom in expression")
	
	def op(self, op, lhs, rhs):
		nodes = {
			'PLUS': ast.Addition,
			'MINUS': ast.Subtraction,
			'MULT': ast.Multiplication,
			'DIV': ast.Division
		}
		return nodes[op.type](left = lhs, right = rhs)

