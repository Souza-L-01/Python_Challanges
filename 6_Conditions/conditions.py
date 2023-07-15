# Conditions
# Python uses boolean logic to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.

x = 2
print (x == 2) # prints out True
print (x == 3) # prints out False
print (x < 3) # prints out True

# Boolean operators
# The "and" and "or" boolean operators allow building complex boolean expressions
name = "John"
age = 23

if name == "John" and age == 23:
  print ("Your name is John, and you are also 23 years old")

if name == "John" or name == "Rick":
  print ("Your name is either John or Rick.")


# The "in" operator
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
name = "John"
if name in ["John", "Rick"]:
  print 

statement = False
another_statement = True
if statement is True:
  # do something
  pass
elif another_statement is True: # else if
	# do something else
	pass
else:
	# do another thing
	pass

x = 2
if x == 2:
	print ("x equals two!")
else:
	print ("X does not equal to two")

# is operator that does not match the values of the variables, but the instances themselves.	
x = [1,2,3]
y = [1,2,3]
print (x == y) # Prints out True
print (x is y) # Prints out False
# Ruby =  puts x.equal?(y) # Prints out false

# The "not" operator
# Using "not" before a boolean expression inverts it:
print (not False) # Prints out True
print ((not False) == (False)) # Prints out False
# Ruby = puts !(false) # Prints out true

