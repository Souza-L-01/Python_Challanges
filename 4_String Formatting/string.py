# String Formatting
# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# This prints out "Hello, John!"
name = "Lucas"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "Lucas"
age = 31
print("%s is %d years old." % (name, age))

# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string. 
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# Argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Lennon", 77.7)
format_string = "Hello %s %s. Your current balance is $%s."
format_string2 = "Hello"

print(format_string % data)
# or
print("%s %s %s. Your current balance is $%s." % (format_string2, data[0], data[1], data[2]))
