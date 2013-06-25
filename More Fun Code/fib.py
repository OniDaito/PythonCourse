
def fib():
	a, b = 0, 1
	while 1:
		yield b
		a, b = b, a+b
	
f = fib()

for i in range(0,10):
	print (f.next())