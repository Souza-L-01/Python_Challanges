def just_the_buzz(number):
    return 'Buzz!' if number % 5 == 0 else str(number)
    
print just_the_buzz(15)
'Buzz!'

print just_the_buzz(10)
'10'