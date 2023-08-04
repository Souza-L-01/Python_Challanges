# I wake up
# if I'm hungry:
#   I eat breakfast

# I leave my house
# if it's cloudy:
#   I bring an umbrella
# otherwise:
#   I bring sunglasses

# I'm at a restaurant
# if I want meat:
#   I order a steak
# otherwise if I want pasta:  
#   I order spaghetti & meatballs
# otherwise:
#   I order a salad.

is_male = False
is_tall = False

if is_male or is_tall:
  print("You're a tall man")
elif is_male and not(is_tall):
  print("Your're short")
elif not (is_male) and is_tall:
  print("You're tall woman")
else:
  print ("You're neither")

# or: flase or false = false
# and: true and true = true