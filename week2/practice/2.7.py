alpha= 'abcdefghijklmnopqrstuvwxyz'

s= str(input())

t=''

i=0
k=3
for i in range (0,99):
    t= t+(alpha[((alpha.index(s[i]))+k)%26])
    i =+ 1

print(t)