def main():
	print("Welcome to the palindrome test!")
	string = input("to begin enter a word or sentence that can be read the same way forwards and backwards: ")
	for index,char in enumerate(string):
		if char != string[-index-1]:
			print(string, "is not a palindrome")
			return False
		print(string, "is a palindrome")
		return True
main()