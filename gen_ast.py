#! /usr/bin/env python3
import sys
from lang import Lexer
from lang import Parser
filename = sys.argv[1]

with open(filename) as f:
	content = f.read()
print("CONTENT OF FILE:")
print(content)

lexer = Lexer(content)

print("\nLEXED TOKENS:")
tok = lexer.next_token()
while tok != None:
	print(tok.type)
	tok = lexer.next_token()

parser = Parser(Lexer(content))
parser.parse()
print("AST:")
for stmt in parser.statements:
	stmt.pprint(0)
print(len(parser.statements))
