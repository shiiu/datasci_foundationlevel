x=[1,7,3,4]
y=[8,6,3,2]

if len(x)==len(y):
    total=0
    for i in range (len(x)):
        total=total+x[i]*y[i]
        
print(total)