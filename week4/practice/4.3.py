import random
l=[]

for i in range(30):
    l.append(random.randint(1,365))

l.sort()
print(l)
i=0
flag=0
while i<len(l)-1:
    if (l[i]==l[i+1]):
        print("Proves bday paradox",l[i],l[i+1])
        flag=1
        
    i= i+1
    
if(flag==0):
    print("no repetition")