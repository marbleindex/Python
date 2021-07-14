import string

# Decorate print() such that (A) it refuses to print anything 
# under ten characters long and (B) only five  calls are allowed, 
# and demonstrate these restrictions when the program is run

def charprint(*args,**kwargs):

		def inner(*args, **kwargs):
			counter = 0  
			while counter <= 5: # added the counter for 5 calls but then the loop terminates after the first iteration
				for arg in args:
					charcount = len(arg) - arg.count(" ") # char count does not include whitespace
					if charcount < 10:   # char count less than ten 
						print("String less than ten characters!")
						counter += 1 # counter incremented
						return counter 

					else:
						print("String: " + arg) # prints arg
						counter += 1  # counter incremented
						return counter
		return inner

def decorated_print(strings):  
	print(strings)

# test strings

# str1 = "do re mi fa so la ti do"  
# str2 = "do re mi fa so la ti"
# str3 = "do re mi fa so la"
# str4 = "do re mi fa so"
# str5 = "do re mi fa"
# str6 = "do re mi"


decorated_print = charprint(decorated_print) # decorated print

# decorated_print(str1,str2,str3,str4,str5)   # test call
# decorated_print(str1,str2,str3,str4,str5,str6)
