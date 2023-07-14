# String Operations

# You can also use single quotes to assign a string. However, you will face problems if the value to be assigned itself contains single quotes. For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))
# lenght of string

astring = "Hello world!"
print(astring.index("o"))
# index of string

astring = "Hello world!"
print(astring.count("l"))
# count of string

astring = "Hello world!"
print(astring[3:7])
# slicing of string

astring = "Hello world!"
print(astring[3:7:2])
# slicing of string

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
# slicing of string
