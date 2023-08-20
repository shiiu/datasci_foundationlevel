def count_digits(x, y):
    power = x ** y
    power_str = str(power)
    num_digits = len(power_str)
    return num_digits

# Example usage
x = int(input(""))
y = int(input(""))

num_digits = count_digits(x, y)
print(num_digits)