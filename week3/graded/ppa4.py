#Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
# Accept the string as input
input_str = input()

# Convert the string to lowercase
lowercase_str = input_str.lower()

# Sort the string in alphabetical order
sorted_str = ''.join(sorted(lowercase_str))

# Print the sorted string
print(sorted_str)