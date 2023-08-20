#Accept two integers a and b as input and print the absolute difference of both the numbers. For example, if 
#a=9,b=8, then the absolute difference is 9−8=1. So, your output should be 1

num1 = int(input(" "))
num2 = int(input(" "))
if num2>num1:
    difference= num2- num1
else:
    difference= num1-num2

print(difference)
