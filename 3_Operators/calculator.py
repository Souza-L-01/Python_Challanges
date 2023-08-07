# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2) #float converts string to number #int converts string to integer
# print(result)

# num1 = float(input("Entrer first number: "))
# op = input("Enter operator: ")
# num2  = float(input("Enter second number: "))

# if op == "+":
#   print(num1 + num2)
# elif op == "-":
#   print(num1 - num2)
# elif  op == "/":
#   print(num1 / num2)
# elif op == "*":
#   print(num1 * num2)
# else:
#   print("Invalid operator")

# exponent 8_Functions

base_num = float(input("Enter base number: "))
pow_num = int(input("Enter power number: "))
def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num 
  return result

print(raise_to_power(base_num, pow_num))