num_char = len(input("what is your name?"))
# takes the length of the word that the user inputs and assigns it to num_char variable

string_num_char = str(num_char)
# we can only concatenate strings together so the integer needs to be converted to string

print("Your name contains " + string_num_char + " characters.")
# prints the concatenated strings and users input
