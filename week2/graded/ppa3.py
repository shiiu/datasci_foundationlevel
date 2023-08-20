# Accept string as input
string = input()

# Convert string to lower case
string = string.lower()

# Initialize a set to store unique vowels
vowels = set()

# Iterate over each character in the string
for char in string:
    if char in 'aeiou':
        vowels.add(char)

# Sort the vowels in alphabetical order
sorted_vowels = sorted(vowels)

# Print the sorted vowels or 'none' if no vowels are present
if sorted_vowels:
    print(''.join(sorted_vowels))
else:
    print('none')