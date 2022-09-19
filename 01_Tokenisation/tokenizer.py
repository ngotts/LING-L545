import sys
c = sys.stdin.read(1)
while c:
	for char in ',': 
		c = c.replace(char, ' ' + char)
	for char in ':': 
		c = c.replace(char, ' ' + char)
	for char in '(':
		c = c.replace(char, char + ' ')
	for char in ')':
		c = c.replace(char, ' ' + char)
	for char in '.':
		c = c.replace(char, ' ' + char)
	for char in ' ':
		c = c.replace(char, '\n')
	sys.stdout.write(c)
	c = sys.stdin.read(1)

		