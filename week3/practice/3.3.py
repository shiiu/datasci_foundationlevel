n= int(input())
i=1
answer=1

if (n<0):
    print("Not Defined")

else:
    while (i<=n):
            answer= answer*i
            i = i+1
    print(answer)

