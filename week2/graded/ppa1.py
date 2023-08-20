a = int(input())
b = int(input())
c = int(input())

# Check if they form the sides of a right triangle
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("YES")
else:
    print("NO")