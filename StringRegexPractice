# Create a program to read the contents of the file Urantia.txt and determine the amount of unique words.


import string 	# import the string module
import re 		# import the regular expression module

with open("/users/abrick/resources/urantia.txt", encoding='utf-8') as file: 	# opens (and closes) the Urantia.txt file
	contents = file.read()		# creates a variable for the contents of urantia.txt

words = contents.rstrip() 		# Remove spaces to the right of the string
words = words.lower()		# Returns a copy of the string in which all case-based characters have been lowercased
words = re.sub('['+string.punctuation+']', '', words).split() # A regular expression to remove all punctuation with whitespace and split the string into words

wordCount = dict()				# Initializes the word count dictionary
	
for word in words:		# For loop to add the word to the wordCount dictionary or augment the count value for a duplicate 
	if word not in wordCount: 	# if the word is not found then an entry is added
		wordCount[word] = 1
	else:					# if the word is found (duplicate), then the value is augmented by 1
		wordCount[word] += 1

print("The approximate number of unique words is",len(wordCount), ".") 
# explanatory text with the length of the wordCount dictionary, which indicates the approximate number of unique words
