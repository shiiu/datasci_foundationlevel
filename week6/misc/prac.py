def checknums(inputstr,numtocheck):
    print (inputstr)
    print(numtocheck)
    
    numbers= inputstr.split()
    numberset=set(numbers)
    
    if numtocheck in numberset:
        return f"element not found"
    else:
        return f"element found"
    


a= input()
numbertocheck= int(input())

result = checknums(a,numbertocheck)

print(result)

#12,456,122,77864,14,553,15,5346