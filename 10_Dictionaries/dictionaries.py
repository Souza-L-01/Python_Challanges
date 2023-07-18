# Dictionaries
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.
# Hash in ruby

phonebook = {
  "John" : 938477566,
  "Jack" : 938377264,
  "Jill" : 947662781
}
print(phonebook)

# Iterating over dictionaries
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
  print("Phone number of %s is %d" % (name, number))

# Removing a value
phonebook = {
  "John" : 938477566,
  "Jack" : 938377264,
  "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

phonebook = {
  "John" : 938477566,
  "Jack" : 938377264,
  "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)