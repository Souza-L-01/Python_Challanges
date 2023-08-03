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