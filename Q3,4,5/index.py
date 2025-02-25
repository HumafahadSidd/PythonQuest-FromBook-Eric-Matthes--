# Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?

name :str ="Eric"
print(f"Hello {name}, would you like to learn some Python today?")


# q3:
# Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

nameinput:str=(input("Enter your name: "))
print(nameinput.lower())
print(nameinput.upper())
print(nameinput.title())

# . Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”

quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f'{author} once said,"{quote} "')
