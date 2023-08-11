def just_the_buzz(number):
  return 'Buzz!' if number % 5 == 0 else str(number)
    
print just_the_buzz(15)
'Buzz!'

print just_the_buzz(10)
'10'

>>> def truthy_test(thing):
  if thing:
    print('This is Truthy.')
  else:
    print("Nope. It's Falsey.")


# Empty container objects are considered Falsey.
print truthy_test([])
# Nope. It's Falsey.

print truthy_test(['bear', 'pig', 'giraffe'])
# This is Truthy.

# Empty strings are considered Falsey.
print truthy_test('')
# Nope. It 's Falsey.

print truthy_test('yes')
# This is Truthy.

# 0 is also considered Falsey.
print truthy_test(0)
# Nope. It's Falsey.