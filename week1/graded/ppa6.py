def find_value(M, N):
    if M < N:
        return M

    while M >= N:
        M -= N

    return M

# Example usage
M = int(input(""))
N = int(input(""))

result = find_value(M, N)
print(result)