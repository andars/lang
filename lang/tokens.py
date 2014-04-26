token_expressions = [
	('\s+', None),
	(r'#[^\s]*', None),
	(r'(?s)/#.*?#/', None),
	(r'\:=', 'ASSIGNMENT'),
	(r'[(]', 'LPAREN'),
	(r'[)]', 'RPAREN'),
	(r'[*]', 'MULT'),
	(r'[/]', 'DIV'),
	(r'[+]', 'PLUS'),
	(r'[-]', 'MINUS'),
	(r'var', 'DECLARATION'),
	(r'perhaps', 'IF'), #such class
	(r'[1-9][0-9]*', 'INTEGER'),
	(r'[a-z]+', 'SYMBOL')
]


	
