from math import *

character_name = "Tom"
character_age = "50" #can only concatenate str (not "int") to str
is_male = True
print ("There once was a man named " + character_name + ", ")
print ("he was " + character_age + " years old. ")
print ("He really liked the name " + character_name + ", ")
print ("but he didn't like being " + character_age + " years .")

print ("Giraffe\nAcademy")  # \n is a new line
print ("Giraffe\"Academy") # \" is a double quote

phrase = "Giraffe Academy"
print (phrase + " is cool")
print (phrase.lower())
print (phrase.upper())
print (phrase.isupper())
print (phrase.upper().isupper())
print (len(phrase))
print (phrase[0])
print (phrase.index("f"))
print (phrase.replace("Giraffe", "Elephant"))

print (3 * (4.5 + 5))
print (10 % 3) #modulus operator - it gives the remainder = 1

my_num = 5
print (str(my_num) + " is my favorite number") # #str converts number to strin. Need to convert number to string

my_num = -5
print (abs(my_num)) #absolute value
print (pow(3, 2)) #3 to the power of 2  = 9 // also means 3*3 (3 elevetad to the power of 2)
print(round(3.7)) #rounds to the nearest number
print(floor(3.7)) #rounds down
print(ceil(3.7)) #rounds up
print(sqrt(36)) #square root