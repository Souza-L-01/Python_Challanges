def say_hi(name, age):
    print("Hello " + name + " your're " + str(age) ) # This is a function, indentation is important

print("Top")
# say_hi() # This is how you call a function
print("Bottom")
# Top
# Hello User
# Bottom

say_hi("Mike", 35)

# Path: 8_Functions/return.py
def cube (num):
  return num*num*num

result = cube(4)
print (result)