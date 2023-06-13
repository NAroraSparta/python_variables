# Data types
#Numbers -> float, integers, complex, longs
# Strings -> characters or text
# Booleans -> True or False


#  Operators

# Arithmetic operators
#  +, -, /, *, %, Remainder

# Comparison operators
#  =, <, >, ==, !=, >=, <=
a = 24
b = 16

print(a + b)
print(a - b)
print(a / b)
print(a * b)

Float_num = 1.356
IntNum = 4

# print(type(Float_Num + IntNum))

one_third = 1/3

print(one_third)
print(one_third * 3)

# Strings
# single_quotes = 'Look, single quotes'
# # double_quotes = "Look, double quotes"
# #
# # print(single_quotes)
# # print(double_quotes)
#
# # escape_example = 'I said \'Wow!\'****************
# # print(escape_example)
#
# # String Slicing
#
# hi = 'Hello World!'
#
# #print(hi[0:5])
# #print(hi[-2:])
#
#
#
# # String methods
# # len()
#
# print(len(hi))
# #strip() removes white_space at the end of the text
#
# white_space = "Lots of white spaces at the end of the string................................"
#
# print(len(white_space))
# #strip()
# print(len(white_space.strip()))
#
# #.upper(), .lower(), .count(), .replace()
# print(white_space.lower())
# print(white_space.upper())
# print(white_space.count("of"))
# print(white_space.replace("of", "red"))

#Concatenation and Casting

x = 2
y = 5.4
z = "This is a string."
zz = "This contains letters and characters."

# Concatenation
# print(z + " " + zz)

# Casting -> Adding two different dat types together
print(str(x) + str(y) + " " + z)

# Concatenation and casting
print(str(x) + str(y) + " " + z + " " + zz)

# F-strings
# name = "lassie"
# years = 7
# height_cm = 60.5
#
# print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!")
#
# pi = 3.1459265359
#
# print(f"Pi to three decimal places: {pi:.3f}")
#
# #percentages




# #Booleans
# a = True
# b = False
# #
# # print(a == b) #False
# # print(a != b) # True
# # print(a >= True) # True
# # print(b <= False) # True
#
# #Using keywords
# print(True and False) # False
# print(True or False) # True

#Booleans with data types

# hi = "Hello World!"
# print(hi.isalpha()) # False  #Is the content alphabetical...no spaces inbetween text
# print(hi.islower()) # False
# print(hi.endswith("!")) # True
# print(hi.startswith("H")) # True

#The value of 0. Zero is always false. Every other number is always true.

# x = 0
# y = 10
#
# print(bool(x)) # False
# print(bool(y)) # True

#Value of None
#Not 0, not nothing -------> It is a Placeholder.

x = None

print(bool(None)) # False

print(x == False) # False
print(x == True) # False

#None is None
print(type(x))
print(x == None) #True

#best practice for checking if something is None
print(x is None) #True






