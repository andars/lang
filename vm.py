import sys
import linecache

stack = []

def handle_print(x):
	print(">>",end='')
	for l in x:
		print(l,end='')
	print()
def handle_mul(x):
	a = stack.pop()
	b = stack.pop()
	print(a,b) 
	stack.append(int(a) * int(b))	

handlers = {
	"push": lambda x: stack.append(x[0]),
	"mul": handle_mul,
	"print": handle_print

}

def handle(line):
	print(stack)
	tokens = line.split(' ');
	#print token
	handlers[tokens[0]](tokens[1:])

filename = sys.argv[1]
ip = 1
while True:
	cmd = linecache.getline(filename, ip).replace("\n", "")
	if cmd == '':
		print("end")
		break
	print(cmd)
	handle(cmd)
	ip += 1
