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

def driving_status(driver_age, test_score):
  if test_score >= 80: 
    if 18 > driver_age >= 16:
      return "Student driver, needs supervision."
    elif driver_age == 18:
      return "Permitted driver, on probation."
    elif driver_age > 18:
      return "Fully licensed driver."
  else:
    return "Unlicensed!"


print driving_status(63, 78)
# 'Unlicsensed!'

print driving_status(16, 81)
# 'Student driver, needs supervision.'

print driving_status(23, 80)
# 'Fully licsensed driver.'