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

astring = "Hello world!"
print(astring[::-1])
# reverse of string

astring = "Hello world!"
print(astring.upper())
print(astring.lower())
# upper and lower case of string

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# start and end of string

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
# split of string

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))