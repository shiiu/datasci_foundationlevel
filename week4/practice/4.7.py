dim=3
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

B=[]
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j]=A[i][k]*B[k][j]
        
    
print(C)