import sys

def default():
	print("Hello")
def owl():
	print("Hoot, hoot!")

def rania():
	print("grrrrrr, i am a tiger!")

def squirrel():
	print("Nutssss")

def main():

	if sys.argv[1] == 'rania':
		rania()
	elif sys.argv[1] == 'owl':
		owl()
	elif sys.argv[1] == 'squirrel':
		squirrel()
	else:
		default()

if __name__ == '__main__':
	main()
