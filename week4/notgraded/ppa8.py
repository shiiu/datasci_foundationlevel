n = int(input("Enter the value of n: "))

# Initialize an empty identity matrix
identity_matrix = []

# Generate the identity matrix
for i in range(n):
    row = [1 if j == i else 0 for j in range(n)]
    identity_matrix.append(row)

# Print the identity matrix
for row in identity_matrix:
    print(','.join(map(str, row)))