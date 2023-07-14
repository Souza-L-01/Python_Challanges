# Numbers
# Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). (It also supports complex numbers, which will not be explained in this tutorial).

# To define an integer, use the following syntax:
myint = 7
print(myint)

# To define a floating point number, you may use one of the following notations:
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)