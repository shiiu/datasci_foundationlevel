def extractnum(code):
    phonenum,rollnum= code.split(',')
    return phonenum

a= input("enter the code of numbers: ")
print("your phone number is:", extractnum(a))