for letter in 'Python':     # First Example
  print (letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
  print ('Current fruit :', fruit[0])

friends = ['Jim', 'Karen', 'Kevin']
for index in range(3, 10):
  print(index)
for index in range(len(friends)):
  print(friends[index])
for index in range(5):
  if index == 0:
    print("First Iteration")
  else:
    print("Not first")
