#! /usr/bin/env python3
import sys
from lang.lexer import Lexer
filename = sys.argv[1]

with open(filename) as f:
	content = f.read()
print(content)
lexer = Lexer(content)

tok = lexer.next_token()
while tok != None:
	print(tok.type)
	tok = lexer.next_token()

