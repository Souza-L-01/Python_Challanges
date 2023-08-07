#tuples = hash in ruby
#list = array in ruby

coordinates = (4, 5) # Tuples are immutable
# coordinates[1] = 10 # This will throw an error, cannot add value
print(coordinates[0])

# List of tuples
coordinates = [(4, 5), (6, 7), (80, 34)]

# List of lists
number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

# print (number_grid[2][0])

for row in number_grid:
  # print(row)
  for col in row:
    print(col)