def test(f):
	print ("aha")
	return f

@test
def flibble():
	print ("flibble")
	
if __name__ == "__main__":
	flibble()