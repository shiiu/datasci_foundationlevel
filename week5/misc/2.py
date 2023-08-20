import math

# Number of men
num_men = 17

# Number of women
num_women = 4

# Total number of individuals
total_individuals = num_men + num_women

# Number of chairs
num_chairs = 21

# Number of remaining individuals (excluding the group of men)
num_remaining = num_chairs - num_men

# Number of circular permutations
num_permutations = math.factorial(num_remaining - 1)

# Total number of possible seating arrangements
total_arrangements = num_permutations

print("Total number of possible seating arrangements:", total_arrangements)