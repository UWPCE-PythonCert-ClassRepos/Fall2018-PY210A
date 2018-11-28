
# The input() function can generate two exceptions: 
# EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.
# Create a wrapper function, perhaps safe_input() that returns 
# None rather rather than raising these exceptions, 
# when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.



def safe_input():
	try:
		name = input("Enter your name here: ")
		return name
	except (KeyboardInterrupt, EOFError):
		return None


if __name__ == '__main__':
	safe_input()