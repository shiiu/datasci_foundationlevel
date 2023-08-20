num= int(input())

if(num>=0):
    rev= num%10
    num=num//10
    while(num>0):
        r= num%10
        num=num//10
        rev=rev*10+r
    print(rev)

else:
    abs=abs(num)
    rev= abs%10
    abs=abs//10
    while(abs>0):
        r= abs%10
        abs=abs//10
        rev=rev*10+r
    print(rev- 2*rev)