n=int(input())
a=[]
b=[]
c=[]
#fora
for i in range(n):
    c.append([0]*n)

for i in range(n):
    row= list(map(int,input().split(',')))
    a.append(row)
    
for j in range(n):
    row= list(map(int,input().split(',')))
    b.append(row)

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]= c[i][j] + a[i][k]*b[k][j]
    
for row in c:
    print(','.join(map(str,row)))