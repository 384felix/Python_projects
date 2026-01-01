import math


first = 'Felix'
last = 'Schiefer'

# print(type(first))
# print(type(first) == str)
# # shift + option + arrow down for shortcut coppiing a line
# print(isinstance(first, str))

# constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# # shift + option + arrow down for shortcut coppiing a line
# print(isinstance(pizza, str))

# Contcatenation
fullname = first + " " + last
fullname += "!"

print(fullname)

# Casting a number to a string
decade = str(384)
print(type(decade))
print(decade)

statement = "I like guys from " + decade + " postal codes"
print(statement)

# Multiple lines

multiline = '''
Hey, how are you?
I was just checking in.
                          All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located?'              # Option + shift + 7 for backslash \\\\\
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                  "
multiline = "             " + multiline
print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("F") | first.startswith("e"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))


# Imported math functions

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attemp to cast incorrect data
# zip_value = int("New York")
