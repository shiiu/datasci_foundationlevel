#Print the following pattern.
#*
#**
#***
#****
#*****
#There are no spaces between consecutive stars. There are no spaces at the end of each line.

n= int(input())

for i in range(1,n):
    print("*"*i)
    i+=1
