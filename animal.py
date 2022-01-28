import sys

def default():
	print("Hello")
def owl():
	print("Hoot, hoot!")

def main():
	if sys.argv[1] == 'owl':
		owl()
	else:
		default()

if __name__ == '__main__':
	main()
