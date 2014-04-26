import sys
from lang import VM

if len(sys.argv) < 2:
	print("filename required")
	sys.exit()

with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

print(lines)

vm = VM(lines)
vm.run()


