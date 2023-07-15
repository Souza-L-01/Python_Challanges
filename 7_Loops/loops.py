#  The for loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3,6)
    print(x)

# Prints out 3,5,7 - range(start, stop, step)
for x in range(3,8,2):
    print(x)

# "while" loops
# While loops repeat as long as a certain boolean condition is met.
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count) 
    count += 1  # This is the same as count = count + 1

# "break" and "continue" statements
# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. 
# Prints out 0,1,2,3,4
count = 0
while True:
    print
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

