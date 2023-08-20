l=[1,2,5,90,11,0,97]
maxi=l[0]

N=[]
for i in range(len(l)):
    if maxi<l[i]:
        maxi= l[i]
        N.append(maxi)
        l.remove(maxi)
print(N)