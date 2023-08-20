def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini=l[i]
    return mini

def list_max(l):
    maxi=l[0]
    for i in range(len(l)):
        if l[i]>maxi:
            maxi= l[i]
    return maxi

l=[1.0,2.0,3.0,4.0,5.0]
print (list_min(l))
print (list_max(l))
a= int(list_min(l))
b= int(list_max(l))

def get_range(a,b):
    ans= list_max(l)-list_min(l)
    return ans

print (get_range(a,b))
