import sys
import re
from .tokens import token_expressions
from .token import Token

class Lexer():
	def __init__(self, content):
		self.content = content
		self.offset = 0;
	
	#Save and Load allow for the parser to look ahead and move back
	def save(self):
		return [self.offset]
	def load(self, state):
		self.offset = state[0]
	def next_token(self):
		#print 'looking for token at:', self.offset
		match = None
		token = None
		for expression in token_expressions:
			pattern, flavor = expression
			#print pattern, flavor
			regex = re.compile(pattern)
			match = regex.match(self.content, self.offset)
			if match:
				#print "matched"
				text = match.group(0)
				#print text
				self.offset = match.end(0)
				if flavor:
					token = Token(flavor, text)
					return token
				else: #ignore whitespace / comments and return real next token
					#print 'skipping whitespace'
					self.offset = match.end(0)
					return self.next_token()
				break

		if self.offset >= len(self.content):
			print('end of input')
			return None
		if not match:
			print(("error: illegal character - {0}".format(self.content[self.offset]), ord(self.content[self.offset])))
			sys.exit(0)

