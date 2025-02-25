# 6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
# person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

famous_person :str = "Albert Einstein"
message :str = "A person who never made a mistake never tried anything new."
print(f"{famous_person} once said, '{message}'")





# 7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip()
#  .
# Define a name with whitespace around it
name = "   Rabekah   "

# Print the name with whitespace
print(f"Original name with whitespace: '{name}'")

# Using lstrip() to remove leading whitespace
print(f"Using lstrip(): '{name.lstrip()}'")

# Using rstrip() to remove trailing whitespace
print(f"Using rstrip(): '{name.rstrip()}'")

# Using strip() to remove both leading and trailing whitespace
print(f"Using strip(): '{name.strip()}'")



# 8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the flename without
# the fle extension, like some fle browsers do.

filename:str="python_notes.txt"
print(filename.removesuffix(".txt"))

# 9. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results. You should create four lines that look like this:
# print(5+3)
# Your output should be four lines, with the number 8 appearing once on
# each line.

print(5+3)
print(10-2)
print(4*2)
print(16/2)


# 2-10. Favorite Number: Use a variable to represent your favorite number. Then,
# using that variable, create a message that reveals your favorite number. Print
# that message

fav_number:int=input("What is your favorite number? ")
print(f"My favorite number is {fav_number}")