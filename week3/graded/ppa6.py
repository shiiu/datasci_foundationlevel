# Accept the positive integer n as input
n = int(input())

# Print the upper part of the arrow
for i in range(1, n + 1):
    numbers = [str(j) for j in range(1, i + 1)]
    print(','.join(numbers))

# Print the lower part of the arrow
for i in range(n - 1, 0, -1):
    numbers = [str(j) for j in range(1, i + 1)]
    print(','.join(numbers))