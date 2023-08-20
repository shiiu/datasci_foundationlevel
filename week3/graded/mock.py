def solution(L):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    sorted_L = sorted(L, reverse=True)
    return sorted_L


    ### Enter your solution above this line

sorted_L=[]
while (len(L)>0):
    maximum = L[0]
    for i in range (len(L)):
        if maximum < L[i];
            maximum = L[i]
    sorted_L.append(maximum)
    L.remove(maximum)