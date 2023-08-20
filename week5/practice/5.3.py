def obvious_sort(l):
    a=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if mini>l[i]:
                mini= l[i]
        a.append(mini)
        l.remove(mini)
    return(a)
        
l= [1,2,3,4,98,23,52,-10,-34]
print(obvious_sort(l))