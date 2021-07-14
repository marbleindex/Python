# Write a program that prints the number of palindromes in /users/abrick/resources/english 

with open("/users/abrick/resources/english") as file: 	# opens (and closes) the english file
	contents = file.read()		# creates a variable for the contents of english
	words_list = contents.split("\n") # splits contents into a list by new line delimeter

isPalindrome = [word for word in words_list if len(word) >= 2 and word == word[::-1]]
# list comprehension that takes words list and does palindrome test, and adds to isPalindrome list if true. 
# Palindromes must be greater than or equal to two characters in length as well.

print("The number of palindromes is ",len(isPalindrome), ".") 
# explanatory text with the number of identified palindromes in English file


