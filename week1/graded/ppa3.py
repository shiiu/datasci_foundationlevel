#Accept a sequence of five single digit numbers separated by commas as input. 
#Print the product of all five numbers.

def product(nums):
    num1, num2, num3, num4, num5 = nums.split(',')
    num1= int(num1)
    num2= int(num2)
    num3= int(num3)
    num4= int(num4)
    num5= int(num5)
    print(num1*num2*num3*num4*num5)

nums = input(" ")
product(nums)