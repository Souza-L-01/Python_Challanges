# 1. Try block
try:
  number = int(input("Enter a number: "))
  print(number)
except ValueError:
  print("Invalid input")