# Intro_to_python

```python
variables in python

a = 1
b = 2
c = 3.5
hi = "My name is Neha"

print(hi)
print(a)
print(c)
print(a + b)
``` 

```python
a way to store data within a program -> it becomes a reference to that data.
a variable can change
a = 4 -> variable_name = variable_data```
```
```python
# H/W Get user_name, age, dob, address. Print it back to them.
user_name = input("Your name: ")
age = input("Your age: ")
dob = input("Your DOB: ")
address = input("Your address: ")

print(user_name)

print("Hi " + user_name + "." + "You are " + str(age) + " years old." + "Your dob is" + " " + str(dob) + " ."  + address)
```


```
Dynamically typed language -> python
```

```
strong typed language -> java, C sharp

int a = 1;
int b = 2;
float c = 3.5;#
string hi = "My name is Neha"
```

```python
type () method

print(type(a))
print(type(hi))
```

```python
variables can be over-written
d = 5
print(d)
d = 7
print(d)
```



```python
user input

print("What is your name? ")
name = input()
print("Hi")
print(name)
```

```python
Data types
Numbers -> float, integers, complex, longs
Strings -> characters or text
Booleans -> True or False
```


```python
Operators

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
```
```python
Strings
single_quotes = 'Look, single quotes'
double_quotes = "Look, double quotes"

print(single_quotes)
print(double_quotes)
```
```python
#You will get an error if you use double quotes inside a string 
# that is surrounded by double quotes.
# e.g. txt = "We are the so-called "Vikings" from the north."
#To fix this problem, use the escape character \"

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

escape_example = 'I said \'Wow!\'
print(escape_example)
```
```python
String Slicing
hi = 'Hello World!'

print(hi[0:5])
print(hi[-2:])
```

```python
String methods

len()
print(len(hi))
strip() removes white_space at the end of the text
white_space = "Lots of white spaces at the end of the string................................"
print(len(white_space))

strip()
print(len(white_space.strip()))
```

```python
#.upper(), .lower(), .count(), .replace()

print(white_space.lower())
print(white_space.upper())
print(white_space.count("of"))
print(white_space.replace("of", "red"))
```

```python
Concatenation and Casting

x = 2
y = 5.4
z = "This is a string."
zz = "This contains letters and characters."

#Concatenation
print(z + " " + zz)

Casting -> Adding two different data types together
#There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
#Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

print(str(x) + str(y) + " " + z)

# Concatenation and casting
print(str(x) + str(y) + " " + z + " " + zz)
```

```python
F-strings
#As we learned in the Python Variables chapter, 
#we cannot combine strings and numbers.
#But we can combine strings and numbers by using the format() method!

#The format() method takes the passed arguments, 
#formats them, and places them in the string where the placeholders {} are

name = "lassie"
years = 7
height_cm = 60.5
print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!")

pi = 3.1459265359

print(f"Pi to three decimal places: {pi:.3f}")
```
```
percentages

```


```python
Booleans
a = True
b = False

print(a == b) #False
print(a != b) # True
print(a >= True) # True
print(b <= False) # True
```
```python
Using keywords
print(True and False) # False
print(True or False) # True
```
```python
Booleans with data types

hi = "Hello World!"
print(hi.isalpha()) # False  #Is the content alphabetical...no spaces inbetween text
print(hi.islower()) # False
print(hi.endswith("!")) # True
print(hi.startswith("H")) # True
```

```python
The value of 0.
#Zero is always false. Every other number is always true.

x = 0
y = 10

print(bool(x)) # False
print(bool(y)) # True
```
```python
Value of None
#Not 0, not nothing -------> It is a Placeholder. The None keyword is used to define a null value, or no value at all.

#None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.

x = None
print(bool(None)) # False
print(x == False) # False
print(x == True) # False
```
```python
None is None
print(type(x))
print(x == None) #True
```
```python
best practice for checking if something is None
print(x is None) #True
```





