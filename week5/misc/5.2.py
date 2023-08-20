def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini=l[i]
    return l[i]

def list_max(l):
    maxi=l[0]
    for i in range(len(l)):
        if l[i]>maxi:
            maxi=l[i]
    return maxi
                   
def add(a,b):
    ans= a+b
    return ans

l=[1,2,3,4,5,6,100,-99]
print(list_min(l))
print(list_max(l))


x= int(list_min(l))
y= int(list_max(l))
print (add(x,y))