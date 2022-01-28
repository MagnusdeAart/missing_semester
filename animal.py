import sys

def default():
	print("Hello")

def rania():
	print("grrrrrr, i am a tiger!")

def main():
	if sys.argv[1] == 'rania':
		rania()
	else:
		default()

if __name__ == '__main__':
	main()
