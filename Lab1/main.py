# python HOME
# example
print("Hello, World!")

# Python Syntax

# example
if 5 > 2:
  print("Five is greater than two!")

# example
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

# ex1
print("Hello World")

# ex2
if 5 > 2:
    print("YES")

# python Comments

# example
# This is a comment
print("Hello, World!")

# example
print("Hello, World!") #This is a comment

# example
#print("Hello, World!")
print("Cheers, Mate!")

# example
#This is a comment
#written in
#more than just one line
print("Hello, World!")

# example
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# ex1
# This is a comment

# ex2
"""
This is a comment
written in 
more than just one line
"""

# python Variables

# example
x = 5
y = "John"
print(x)
print(y)

# example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# example
x = 5
y = "John"
print(type(x))
print(type(y))

# example
x = "John"
# is the same as
x = 'John'

# example
a = 4
A = "Sally"
#A will not overwrite a

# example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# example
x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# example
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

# ex1
carname = "Volvo"

# ex2
x = 50

# ex3
x = 5
y = 10
print(x + y)

# ex4
x = 5
y = 10
z = x + y
print(z)

# ex5
x, y, z = "Orange", "Banana", "Cherry"

# ex6
x = y = z = "Orange"

# ex7
def myfunc():
    global x
    x = "fantastic"



# Python data types
# ex1
x = 5
print(type(x))
# int

# ex2
x = "Hello World"
print(type(x))
# str

# ex3
x = 20.5
print(type(x))
# float

# ex4
x = ["apple", "banana", "cherry"]
print(type(x))
# list

# ex5
x = ("apple", "banana", "cherry")
print(type(x))
# tuple

# ex6
x = {"name": "John", "age": 36}
print(type(x))
# dict

# ex7
x = True
print(type(x))
# bool

# Python numbers

# example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# example
import random

print(random.randrange(1, 10))

#ex1
x = 5
x = float(x)

#ex2
x = 5.5
x = int(x)

# ex3
x = 5
x = complex(x)


# Python casting

# example1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# example2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# example3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



# Python strings

# example
a = "Hello"
print(a)

# example
a = "Hello, World!"
print(a[1])

# example
for x in "banana":
  print(x)

# example


# ex1
x = "Hello World"
print(len(x))

# ex2
txt = "Hello World"
x = txt[0]

# ex3
txt = "Hello World" # 5 Not included
x = txt[2:5]

# ex4
txt = "Hello World"
x = txt.strip()

# ex5
txt = "Hello World"
txt = txt.upper()

# ex6
txt = "Hello World"
txt = txt.lower()

# ex7
txt = "Hello World"
txt = txt.replace("H", "J")

# ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

