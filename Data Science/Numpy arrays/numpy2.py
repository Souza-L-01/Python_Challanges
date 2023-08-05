weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)

# Create an array of ones
ones_array = np.ones((3, 4))
print("Ones Array:")
print(ones_array)
print()

# Create an array of zeros
zeros_array = np.zeros((2, 3, 4), dtype=np.int16)
print("Zeros Array:")
print(zeros_array)
print()

