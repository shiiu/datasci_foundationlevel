#Accept a five digit number as input and print the sum of its digits as output.

num = int(input(""))
sumofdigits= sum(int(digit) for digit in str(num))
print(sumofdigits)
