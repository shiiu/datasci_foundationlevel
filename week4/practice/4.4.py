l= [2002,2003,2001,2004,2007,2023,1985,1990]
x=[]

for i in range(len(l)):
    min=l[0]
    for i in range(len(l)):
        if min>l[i]:
            min= l[i]
    x.append(min)
    l.remove(min)
        
    
print(x)