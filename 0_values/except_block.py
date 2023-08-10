# 1. Try block
try:
  answer = 10 / 0
  number = int(input("Enter a number: "))
  print(number)
except ZeroDivisionError as err:
  print("Divided by zero")
except ValueError:
  print("Invalid input")